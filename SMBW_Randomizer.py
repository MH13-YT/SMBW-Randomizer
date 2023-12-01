import copy
import importlib
import json
import os
import shutil
from tkinter import ttk
import uuid
import logging
import logging_config  # Importez la configuration de journalisation

# Import CLI Tools
import argparse

# Import GUI Tools
import tkinter as tk
from tkinter import messagebox

# Import SMBW_R Tools
import SMBW_R.tools.main
import SMBW_R.tools.zstandard
import SMBW_R.tools.byml

# ------------------------------

# Dictionnaire pour stocker les instances de modules
modules = {}
# Importez automatiquement les modules à partir de chaque dossier
for module_name in SMBW_R.tools.main.get_module_list():
    try:
        module_path = f"SMBW_R.modules.{module_name}"
        module = importlib.import_module(module_path)
        module_instance = getattr(
            module, f"{module_name}_module"
        )()  # Assurez-vous que le nom de la classe est correct
        modules[module_name] = module_instance
        print(f"Module '{module_name}' importé avec succès.")
    except (ImportError, AttributeError) as e:
        print(f"Impossible d'importer le module '{module_name}': {e}")


def save_configuration(mode):
    if mode == "CLI":
        print("The settings of randomizer has been modified")
        for module_name in SMBW_R.tools.main.get_module_list():
            if hasattr(args, module_name) and getattr(args, module_name) != None:
                print(f"Module : {module_name}")
                print(f"        Enabled : {True}")
                print(f"        Method  : {getattr(args, module_name)}")
            else:
                print(f"Module : {module_name}")
                print(f"        Enabled : {False}")
                print(f"        Method  : ''")
            if (
                input(
                    "Do you want to continue and save the modifications in config file ? (Y/N) : "
                )
                == "Y"
            ):
                with open("config.json", "w") as fichier:
                    for module_name in SMBW_R.tools.main.get_module_list():
                        if (
                            hasattr(args, module_name)
                            and getattr(args, module_name) != None
                        ):
                            data[module_name] = {
                                "enable": True,
                                "method": str(getattr(args, module_name)),
                            }
                        else:
                            data[module_name] = {"enable": False, "method": ""}
                    json.dump(data, fichier)
                print("Modification Saved in configuration file : Starting")
            else:
                input("Modifications has been aborted : Exit App")
                exit()
    elif mode == "GUI":
        for module_name in module_checkboxes:
            try:
                if (
                    int(fenetre.tk.getvar(module_checkboxes[module_name]["variable"]))
                    == 1
                    and str(module_methods[module_name].get()) != ""
                ):
                    data[module_name] = {
                        "enable": True,
                        "method": module_methods[module_name].get(),
                    }
                else:
                    data[module_name] = {"enable": False, "method": ""}
            except:
                data[module_name] = {"enable": False, "method": ""}
        with open("config.json", "w") as fichier:
            json.dump(data, fichier)
        messagebox.showinfo(
            "Sauvegarde", "La configuration a été enregistrée avec succès."
        )
        fenetre.destroy()


def module_merger(output_folder):
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(
                "output/romfs", os.path.relpath(source_path, output_folder)
            )
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy2(source_path, destination_path)


def module_cleaner(output_folder):
    # Supprimez tous les fichiers et sous-répertoires du répertoire
    for root, dirs, files in os.walk(output_folder, topdown=False):
        for file in files:
            fichier_path = os.path.join(root, file)
            os.remove(fichier_path)
        for rep in dirs:
            rep_path = os.path.join(root, rep)
            os.rmdir(rep_path)
    # Supprimez le répertoire lui-même
    os.rmdir(output_folder)

def get_resource_metadata(ressource):
    if os.path.isdir(ressource['romfs']):
        files_metadata = []
        for filename in os.listdir(ressource['romfs']):
            romfs_file_path = os.path.join(ressource['romfs'], filename)
            worktable_file_path = os.path.join(ressource['worktable'], filename)
            output_file_path = os.path.join(ressource['output'], filename)
            if os.path.isfile(romfs_file_path):
                # Utiliser os.path.splitext pour séparer le nom du fichier et l'extension
                file_name, file_extension = os.path.splitext(filename)
                compression_extension = ""
                if file_extension == '.zs':
                    compression_extension = '.zs'
                    file_name = os.path.splitext(os.path.splitext(os.path.basename(romfs_file_path))[0])[0]
                    decompressed_file_name, file_extension = os.path.splitext(worktable_file_path.replace(".zs", ""))
                
                if compression_extension == "":
                    file_name = os.path.splitext(os.path.basename(romfs_file_path))[0]

                file_metadata = {
                    "file_name":file_name,
                    "romfs_file_folder": os.path.dirname(romfs_file_path),
                    "output_file_folder": os.path.dirname(output_file_path),
                    "worktable_file_folder": os.path.dirname(worktable_file_path),
                    "compressed": True if compression_extension != '' else False,
                    "compression_metadata": {
                        "compression_extension": compression_extension,
                    } if compression_extension != '' else None,
                    "data_file_extension": file_extension
                }

                files_metadata.append(file_metadata)
        return files_metadata
    
def get_ressource_data(files_metadata):
    files_data = []
    for file_metadata in files_metadata:
        # Verify if every folders exist
        if not os.path.exists(f"{os.curdir}/{file_metadata['worktable_file_folder']}"):
            os.makedirs(f"{os.curdir}/{file_metadata['worktable_file_folder']}", exist_ok=True)
        # Create Worktable
        if file_metadata["compressed"] == True:
            # Decompression Required
            if file_metadata["compression_metadata"]["compression_extension"] == ".zs":
                # Use ZStandard Decompression Algorithm
                SMBW_R.tools.zstandard.zstandard_tools.decompress(f"{file_metadata['romfs_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}{file_metadata['compression_metadata']['compression_extension']}", f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}")
        else:
            shutil.copy(f"{file_metadata['romfs_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}", f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}")
        # Read Data from Worktable
        data = None
        if file_metadata['data_file_extension'] == ".byml" or file_metadata['data_file_extension'] == ".bgyml":
            data = SMBW_R.tools.byml.byml_tools.dump(f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}")
        files_data.append({
            "file_name": file_metadata['file_name'],
            "ressource_type": file_metadata['worktable_file_folder'],
            "file_data": data
            }) 
    return files_data

def set_ressource_data(files_metadata, files_data, modified_files_list):
    for file_metadata in files_metadata:
        # Write Data to Worktable
        for file_data in files_data:
            if file_data["file_name"] == file_metadata["file_name"] and file_data["ressource_type"] == file_metadata["worktable_file_folder"]:
                if file_metadata['data_file_extension'] == ".byml" or file_metadata['data_file_extension'] == ".bgyml":
                    SMBW_R.tools.byml.byml_tools.restore(f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}",file_data["file_data"])
        # Copy Files to Output
        if f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}" in modified_files_list:
            if not os.path.exists(f"{os.curdir}/{file_metadata['output_file_folder']}"):
                os.makedirs(f"{os.curdir}/{file_metadata['output_file_folder']}", exist_ok=True)
            if file_metadata["compressed"] == True:
                # Decompression Required
                if file_metadata["compression_metadata"]["compression_extension"] == ".zs":
                    # Use ZStandard Decompression Algorithm
                    SMBW_R.tools.zstandard.zstandard_tools.compress(f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}", f"{file_metadata['output_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}{file_metadata['compression_metadata']['compression_extension']}")
            else:
                shutil.copy(f"{file_metadata['worktable_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}", f"{file_metadata['output_file_folder']}/{file_metadata['file_name']}{file_metadata['data_file_extension']}") 
    return files_data                
    

class SMBW_Randomizer:
    def __init__(self):
        self.path_list = [
            "output/SMM/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs",
            "output/YUZU/load/010015100B514000/Randomized/romfs",
            "output/RYUJINX/mods/contents/010015100B514000/Randomized/romfs",
        ]
        self.logger = logging.getLogger("SMBW_Randomizer")
        self.validate = {
            "Check config file": False,
            "Data is dumped": False,
            "Randomizing game with selected modules and config": False,
            "Data is restored": False,
            "Packaging as a mod for all platforms": False,
        }
        self.ressources_metadata = {}
        self.ressources_data = {}
        self.modified_files_list = set()

    def check_config(self, config):
        self.logger.info("STEP 1 : Config Check")
        self.logger.info("Verify config and found potential module conflicts")
        config_is_checked = True
        active_module = 0
        if (not os.path.exists('output')):
            os.mkdir("output")
        for root, dirs, files in os.walk("output", topdown=False):
            for file in files:
                fichier_path = os.path.join(root, file)
                os.remove(fichier_path)
            for rep in dirs:
                rep_path = os.path.join(root, rep)
                os.rmdir(rep_path)
        for module_name in SMBW_R.tools.main.get_module_list():
            if config[module_name]["enable"] == True:
                active_module = active_module + 1
                if module_name in modules:
                    module = modules[module_name]
                    for ressource in module.get_ressources():
                        self.ressources_metadata[ressource['romfs']] = get_resource_metadata(ressource)
        if active_module == 0:
            config_is_checked = False
            self.logger.error("All randomization modules are inactive")
            print("All randomization modules are inactive")
            print(
                "Please modify your configuration with --configure or by modifying config.json"
            )
        self.validate["Check config file"] = config_is_checked
        return config_is_checked
    
    def dump_data(self):
        data_is_dumped = True
        for ressource, metadata in self.ressources_metadata.items():
            self.ressources_data[ressource] = get_ressource_data(metadata)
        self.validate["Data is dumped"] = data_is_dumped
        return data_is_dumped

    def starting_selected_modules(self, config, seed):
        self.logger.info("STEP 2 : Randomizing game with selected modules and config")
        print(f"Randomization will use Seed : '{seed}'")
        self.logger.info(f"Randomization will use Seed : {seed}")
        modules_process_ended_without_error = True
        for module_name in SMBW_R.tools.main.get_module_list():
            if config[module_name]["enable"] == True:
                self.logger.info(
                    f"Starting {module_name} module with method '{config[module_name]['method']}'"
                )
                if module_name in modules:
                    module = modules[module_name]
                    module_data = []
                    for ressource in module.get_ressources():
                        with open(f"{module_name}_{str(ressource['romfs']).replace('/','.')}-input.json", "w") as file_data:
                            json.dump(self.ressources_data[ressource['romfs']], file_data)
                        module_data.extend(copy.deepcopy(self.ressources_data[ressource['romfs']]))
                    module_result = module.start(config[module_name]["method"], seed, copy.deepcopy(module_data))   
                    if module_result['result'] == False:
                        modules_process_ended_without_error = False
                    else:
                        for file_data in module_result['data'][0]:
                            for file in self.ressources_data[file_data['ressource_type'].replace("worktable/", "")]:
                                if file["file_name"] == file_data["file_name"]:
                                    if file["file_data"] != file_data["file_data"]:
                                        self.modified_files_list.add(f"{file['ressource_type']}/{file['file_name']}")
                                        file["file_data"] = copy.deepcopy(file_data["file_data"])
                        for ressource in module.get_ressources():
                            with open(f"{module_name}_{str(ressource['romfs']).replace('/','.')}-output.json", "w") as file_data:
                                json.dump(self.ressources_data[ressource['romfs']], file_data)
                                            
        self.validate[
            "Randomizing game with selected modules and config"
        ] = modules_process_ended_without_error
        return modules_process_ended_without_error
    
    def restore_data(self):
        data_is_restored = True
        for ressource, metadata in self.ressources_metadata.items():
            set_ressource_data(metadata, self.ressources_data[ressource], list(self.modified_files_list))
        self.validate["Data is restored"] = data_is_restored
        return data_is_restored

    def packaging_output(self):
        self.logger.info("STEP 4 : Packaging as a mod for all platforms")
        for folder in self.path_list:
            shutil.copytree("output/romfs", folder)
        packaged_with_success = True
        self.validate["Packaging as a mod for all platforms"] = packaged_with_success
        return packaged_with_success

    def main(self, config, seed):
        (
            self.check_config(config)
            and self.dump_data()
            and self.starting_selected_modules(config, seed)
            and self.restore_data()
            and self.packaging_output()
        )
        print("\nSummary of randomization process:")
        for key, value in enumerate(self.validate):
            if self.validate[value]:
                print(f"Step {key + 1}: {value} => SUCCESS")
            else:
                print(f"Step {key + 1}: {value} => FAIL")


randomise = SMBW_Randomizer()

# Create ArgParse and Read Arguments

parser = argparse.ArgumentParser(
    description="Description générale de votre programme",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100),
)
parser.add_argument("--seed", help="Choisir une Seed a utiliser pour la randomization")
parser.add_argument(
    "--configure", action="store_true", help="Configurer le randomiseur avec la GUI"
)
parser.add_argument(
    "--configure_cli",
    action="store_true",
    help="Configurer le randomiseur avant de le lancer",
)
dependant_group = parser.add_argument_group("--configure_cli : Available modules")
for module_name in SMBW_R.tools.main.get_module_list():
    if module_name in modules:
        module = modules[module_name]
        dependant_group.add_argument(
            f"--{module_name}",
            choices=module.list_method(),
            help=f"Activer le module {module_name} avec la methode choisie",
        )
args = parser.parse_args()
module_list = SMBW_R.tools.main.get_module_list()
if args.seed is None:
    args.seed = str(uuid.uuid4())
if not os.path.exists("config.json"):
    print("Cannot found config.json file. Opening Configuration UI")
    args.configure = "FORCE"
if not args.configure or args.configure_cli:
    with open("config.json", "r") as fichier:
        data = json.load(fichier)
        # Module Status Checker : verify if at least 1 module is active 
        active_modules = 0
        for module_name in module_list:
            # Verify if module are enabled 
            if module_name in modules and data[module_name]["enable"] == True:
                active_modules = active_modules + 1
        if active_modules == 0:
            # If 0 Module are enabled : Open Configuration GUI Automatically
            print("0 Modules are enabled in current configuration. Opening Configuration UI")
            args.configure = "FORCE"
if args.configure_cli:
    save_configuration("CLI")
if args.configure:
    # Créer une fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("SMBW_Randomizer : Configuration")

    # Ajustez la largeur minimale (100 dans cet exemple)
    fenetre.minsize(
        400, 25 + 25 * len(module_list)
    )  # Ajustez les valeurs à vos besoins

    # Charger la configuration depuis un fichier (ou créez un fichier de configuration par défaut)
    try:
        with open("config.json", "r") as fichier:
            data = json.load(fichier)
    except FileNotFoundError:
        data = {}

    # Créer des cases à cocher pour activer/désactiver les modules (juste à côté)
    module_checkboxes = {}
    module_methods = {}

    row = 0

    for module_name in module_list:
        if module_name in modules:
            module = modules[module_name]

            status_var = tk.BooleanVar()  # Utilisez BooleanVar pour les cases à cocher
            method_var = tk.StringVar()
            try:
                if data[module_name] != None:
                    method_var.set(module.list_method()[0])
                    status_var.initialize(False)
            except:
                method_var.set(module.list_method()[0])
                status_var.initialize(False)
            for i in range(3):
                fenetre.grid_columnconfigure(i, weight=1)
            # Créez un cadre pour chaque module qui occupera 2 lignes
            module_frame = tk.Frame(fenetre, borderwidth=1, relief="solid")
            module_frame.grid(row=row, column=0, columnspan=3, sticky="we")
            module_frame.grid_columnconfigure(0, minsize=200)
            module_frame.grid_columnconfigure(3, minsize=50)
            for i in range(3):
                module_frame.grid_columnconfigure(i, weight=1)
            # Colonne 0 du cadre : Case à cocher pour activer/désactiver le module
            module_checkboxes[module_name] = tk.Checkbutton(
                module_frame, text=module_name, variable=status_var
            )
            module_checkboxes[module_name].grid(
                row=row, column=0,sticky="w"
            )
            
            # Colonne 1 du cadre : Étiquette "Méthode:"
            method_label = tk.Label(module_frame, text="Method:")
            method_label.grid(row=row, column=1, sticky="e")

            # Colonne 2 du cadre : Menu déroulant pour la méthode
            method_options = (
                module.list_method()
            )  # Vous devez ajuster cette ligne en fonction de votre structure de module
            method_option_menu = tk.OptionMenu(
                module_frame, method_var, *method_options
            )
            method_option_menu.config(width=20)
            method_option_menu.grid(row=row, column=2,sticky="w")
            module_methods[module_name] = method_var

            row += 1

            # Colonne 0 du cadre de la deuxième ligne : Label pour la description du module
            description_label = tk.Label(
                module_frame, text=module.get_description()
            )  # Assurez-vous d'ajuster la source de description
            description_label.grid(
                row=row, column=0,columnspan=4,sticky="w"
            )
    # Bouton de sauvegarde en bas
    bouton_enregistrer = tk.Button(
        fenetre,
        text="Save configuration and exit",
        command=lambda: save_configuration("GUI"),
    )
    bouton_enregistrer.grid(row=row, column=0, columnspan=3, sticky="we")
    # Lancer la boucle principale de l'application
    fenetre.mainloop()

# Starting Randomization
randomise.main(data, args.seed)
