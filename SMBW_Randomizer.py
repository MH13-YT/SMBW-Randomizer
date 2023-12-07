import copy
import importlib
import json
import os
import shutil

import uuid
import zstandard

import logging
import logging_config
from restbl import ResourceSizeTable
import argparse

import tkinter as tk
from tkinter import messagebox

import SMBW_R.tools.main

modules = {}
for module_name in SMBW_R.tools.main.get_module_list():
    try:
        module_path = f"SMBW_R.modules.{module_name}"
        module = importlib.import_module(module_path)
        module_instance = getattr(module, f"{module_name}_module")()
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
                print("        Enabled : True")
                print(f"        Method  : {getattr(args, module_name)}")
            else:
                print(f"Module : {module_name}")
                print("        Enabled : False")
                print("        Method  : ''")
            if (
                input(
                    "Do you want to continue and save the modifications in config file ? (Y/N) : "
                )
                == "Y"
            ):
                with open("config.json", "w") as config_file:
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
                    json.dump(data, config_file)
                print("Modification Saved in configuration file : Starting")
            else:
                input("Modifications has been aborted : Exit App")
                exit()
    elif mode == "GUI":
        for module_name in module_checkboxes:
            try:
                if (
                    int(
                        config_gui.tk.getvar(module_checkboxes[module_name]["variable"])
                    )
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
        with open("config.json", "w") as config_file:
            json.dump(data, config_file)
        messagebox.showinfo(
            "Sauvegarde", "La configuration a été enregistrée avec succès."
        )
        config_gui.destroy()


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
            "Cleaning": False,
        }
        self.resources_metadata = {}
        self.resources_data = {}
        self.modified_files_list = set()
        self.RSTB_DUMP = {}

    def check_config(self, config):
        self.logger.info("STEP 1 : Config Check")
        self.logger.info("Verify config and found potential module conflicts")
        config_is_checked = True
        active_module = 0
        SMBW_R.tools.main.cleaner("output")
        if not os.path.exists("output"):
            os.mkdir("output")
        for module_name in SMBW_R.tools.main.get_module_list():
            if config[module_name]["enable"] == True:
                active_module = active_module + 1
                if module_name in modules:
                    module = modules[module_name]
                    for resource in module.get_resources():
                        self.resources_metadata[
                            resource["romfs"]
                        ] = SMBW_R.tools.main.get_resource_metadata(resource)
                        if not os.path.exists(resource["romfs"]):
                            self.logger.error(
                                "Unable to find 'Super Mario Bros Wonder' romfs files"
                            )
                            input(
                                "Unable to find 'Super Mario Bros Wonder' romfs files, please place a valid romfs dump of 'Super Mario Bros Wonder' in the same location as the executable."
                            )
                            config_is_checked = False
                            self.validate["Check config file"] = config_is_checked
                            return config_is_checked
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
        RSTB_files = os.listdir("romfs/System/Resource")
        for RSTB_file in RSTB_files:
            if not os.path.exists(f"{os.curdir}/worktable/romfs/System/Resource"):
                os.makedirs(
                    f"{os.curdir}/worktable/romfs/System/Resource", exist_ok=True
                )
        shutil.copy(
            os.path.join("romfs/System/Resource", RSTB_file),
            os.path.join("worktable/romfs/System/Resource", RSTB_file),
        )
        worktable_rstb = os.path.join("worktable/romfs/System/Resource", RSTB_file)
        if os.path.isfile(worktable_rstb):
            with open(worktable_rstb, "rb") as RSTB:
                self.RSTB_DUMP[RSTB_file] = ResourceSizeTable.from_binary(RSTB.read())
        data_is_dumped = True
        self.logger.info("STEP 2 : Dump Data")
        self.logger.info("Starting Required Data Dump")
        for resource, metadata in self.resources_metadata.items():
            self.resources_data[resource] = SMBW_R.tools.main.get_resource_data(
                metadata
            )
        self.logger.info("Data Dumped Successfuly")
        self.validate["Data is dumped"] = data_is_dumped
        return data_is_dumped

    def starting_selected_modules(self, config, seed):
        self.logger.info("STEP 3 : Randomizing game with selected modules and config")
        print(f"Randomization will use Seed : '{seed}'")
        self.logger.info(f"Randomization will use Seed : {seed}")
        modules_process_ended_without_error = True
        for module_name in SMBW_R.tools.main.get_module_list():
            if config[module_name]["enable"] == True and module_name in modules:
                self.logger.info(
                    f"Starting {module_name} module with method '{config[module_name]['method']}'"
                )
                module = modules[module_name]
                module_data_input = []
                for name, metadata in self.resources_data.items():
                    module_data_input.extend(copy.deepcopy(metadata))
                module_result = module.start(
                    config[module_name]["method"],
                    seed,
                    copy.deepcopy(module_data_input),
                )
                if module_result["result"] == False:
                    modules_process_ended_without_error = False
                else:
                    for file_data in module_result["data"][0]:
                        for file in self.resources_data[
                            file_data["resource_type"].replace("worktable/", "")
                        ]:
                            if (
                                file["file_name"] == file_data["file_name"]
                                and file["file_data"] != file_data["file_data"]
                            ):
                                self.modified_files_list.add(
                                    f"{file['resource_type']}/{file['file_name']}"
                                )
                                file["file_data"] = copy.deepcopy(
                                    file_data["file_data"]
                                )

        self.logger.info("Randomization Finished")
        self.validate[
            "Randomizing game with selected modules and config"
        ] = modules_process_ended_without_error
        return modules_process_ended_without_error

    def restore_data(self):
        self.logger.info("STEP 4 : Restoring Data and Adapt Resource Size Table")
        data_is_restored = True
        self.logger.info("Starting Data Restoration")
        for resource, metadata in self.resources_metadata.items():
            SMBW_R.tools.main.set_resource_data(
                metadata,
                self.resources_data[resource],
                list(self.modified_files_list),
                self.RSTB_DUMP,
            )
        self.logger.info("Data Restored Successfully")
        self.logger.info("Starting Resource File Table Files Patching")
        RSTB_files = os.listdir("worktable/romfs/System/Resource")
        for RSTB_file in RSTB_files:
            if not os.path.exists(f"{os.curdir}/output/romfs/System/Resource"):
                os.makedirs(f"{os.curdir}/output/romfs/System/Resource", exist_ok=True)
            worktable_rstb = os.path.join("worktable/romfs/System/Resource", RSTB_file)
            if os.path.isfile(worktable_rstb):
                with open(worktable_rstb, "wb") as RSTB:
                    data = self.RSTB_DUMP[RSTB_file].to_binary(compress=False)
                    cctx = zstandard.ZstdCompressor(level=16)
                    RSTB.write(cctx.compress(data))
                shutil.copy(
                    os.path.join("worktable/romfs/System/Resource", RSTB_file),
                    os.path.join("output/romfs/System/Resource", RSTB_file),
                )
        self.logger.info("Resource File Table Files Successfully")
        self.validate["Data is restored"] = data_is_restored

        return data_is_restored

    def packaging_output(self):
        self.logger.info("STEP 5 : Packaging as a mod for all platforms")
        self.logger.info("Starting Data Packaging")
        for folder in self.path_list:
            shutil.copytree("output/romfs", folder)
        packaged_with_success = True
        self.logger.info("Randomized data Packaged Successfully")
        self.validate["Packaging as a mod for all platforms"] = packaged_with_success
        return packaged_with_success

    def cleaning(self):
        self.logger.info("STEP 6 : Cleaning Residual Data")
        SMBW_R.tools.main.cleaner("worktable")
        cleaned = True
        self.validate["Cleaning"] = cleaned
        return cleaned

    def main(self, config, seed):
        (
            self.check_config(config)
            and self.dump_data()
            and self.starting_selected_modules(config, seed)
            and self.restore_data()
            and self.packaging_output()
            and self.cleaning()
        )
        print("\nSummary of randomization process:")
        for key, value in enumerate(self.validate):
            if self.validate[value]:
                print(f"Step {key + 1}: {value} => SUCCESS")
            else:
                print(f"Step {key + 1}: {value} => FAIL")


randomise = SMBW_Randomizer()

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
    with open("config.json", "r") as config_file:
        data = json.load(config_file)

        active_modules = 0
        for module_name in module_list:
            if module_name in modules and data[module_name]["enable"] == True:
                active_modules = active_modules + 1
        if active_modules == 0:
            print(
                "0 Modules are enabled in current configuration. Opening Configuration UI"
            )
            args.configure = "FORCE"
if args.configure_cli:
    save_configuration("CLI")
if args.configure:
    config_gui = tk.Tk()
    config_gui.title("SMBW_Randomizer : Configuration")

    config_gui.minsize(400, 25 + 25 * len(module_list))

    try:
        with open("config.json", "r") as config_file:
            data = json.load(config_file)
    except FileNotFoundError:
        data = {}

    module_checkboxes = {}
    module_methods = {}

    row = 0

    for module_name in module_list:
        if module_name in modules:
            module = modules[module_name]

            status_var = tk.BooleanVar()
            method_var = tk.StringVar()
            try:
                if data[module_name] != None:
                    method_var.set(module.list_method()[0])
                    status_var.initialize(False)
            except Exception:
                method_var.set(module.list_method()[0])
                status_var.initialize(False)
            for i in range(3):
                config_gui.grid_columnconfigure(i, weight=1)
            module_frame = tk.Frame(config_gui, borderwidth=1, relief="solid")
            module_frame.grid(row=row, column=0, columnspan=3, sticky="we")
            module_frame.grid_columnconfigure(0, minsize=200)
            module_frame.grid_columnconfigure(3, minsize=50)
            for i in range(3):
                module_frame.grid_columnconfigure(i, weight=1)
            module_checkboxes[module_name] = tk.Checkbutton(
                module_frame, text=module_name, variable=status_var
            )
            module_checkboxes[module_name].grid(row=row, column=0, sticky="w")

            method_label = tk.Label(module_frame, text="Method:")
            method_label.grid(row=row, column=1, sticky="e")

            method_options = module.list_method()
            method_option_menu = tk.OptionMenu(
                module_frame, method_var, *method_options
            )
            method_option_menu.config(width=20)
            method_option_menu.grid(row=row, column=2, sticky="w")
            module_methods[module_name] = method_var

            row += 1

            description_label = tk.Label(module_frame, text=module.get_description())
            description_label.grid(row=row, column=0, columnspan=4, sticky="w")
    save_button = tk.Button(
        config_gui,
        text="Save configuration and exit",
        command=lambda: save_configuration("GUI"),
    )
    save_button.grid(row=row, column=0, columnspan=3, sticky="we")
    config_gui.mainloop()

randomise.main(data, args.seed)
