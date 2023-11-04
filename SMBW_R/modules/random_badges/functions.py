import subprocess
import os
import yaml
from .profiles import profiles

ressources = [
    {

        "romfs": "romfs/Stage/CourseInfo",
        "worktable": "SMBW_R/modules/random_badges/worktable",
        "output": "SMBW_R/modules/random_badges/output/romfs/Stage/CourseInfo",
    },
]

class file_converter:
    def get_used_files():
        file_list = []
        for filepath in ressources:
            file_list.append(filepath["romfs"])
        return file_list
    def get_output_files():
        file_list = []
        for filepath in ressources:
            file_list.append(filepath["output"])
        return file_list
    def verify_files():
        for filepath in ressources:
            target = filepath["romfs"]
            if not os.path.exists(target):
                return False
        return True
    def decompile():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["romfs"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["romfs"], fichier)
                if os.path.isfile(chemin_complet):
                    subprocess.run(["byml_to_yml"] + [f'{args_pair["romfs"]}/{fichier}',f'{args_pair["worktable"]}/{fichier.replace("bgyml", "yml")}'], check=True)
    def compile():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet) and os.path.splitext(chemin_complet)[1] == '.yml':
                    subprocess.run(["yml_to_byml"] + [f'{args_pair["worktable"]}/{fichier}',f'{args_pair["output"]}/{fichier.replace("yml", "bgyml")}'], check=True)

    def clean():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet) and os.path.splitext(chemin_complet)[1] == '.yml':
                    os.remove(chemin_complet)
        os.remove("SMBW_R/modules/random_badges/worktable/random_data.json")

class data_manager:
    def dump():
        # Dump is at JSON Format
        informations = {}
        informations["levels"] = []
        for ressource in ressources:
            fichiers = os.listdir(ressource["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(ressource["worktable"], fichier)
                if os.path.isfile(chemin_complet):
                    with open(f'{ressource["worktable"]}/{fichier}', "r") as fichier_yaml:  # Vous n'avez pas besoin de os.path.join ici
                        yml_data = yaml.safe_load(fichier_yaml)
                        informations["levels"].append({"file_name":fichier,"level_data":yml_data})              
        return informations
    
    def restore(data):
        # Dump is at JSON Format
        for ressource in ressources:
            for level_info in data["levels"]:
                file_name = level_info["file_name"]
                level_data = level_info["level_data"]
                file_path = os.path.join(ressource["worktable"], file_name)
                with open(file_path, "w") as fichier_yaml:
                    yaml.safe_dump(level_data, fichier_yaml)

   
    def shuffle(data_dump, method, seed):
        shuffle = False
        if method == "start_with":
            data_dump = profiles.start_with(data_dump,seed)
            shuffle = True
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
