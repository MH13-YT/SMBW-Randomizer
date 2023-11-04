import subprocess
import os
import yaml
import random
from .profiles import profiles

ressources = [
    {

        "romfs": "romfs/",
        "worktable": "SMBW_R/modules/exemple_module/worktable/",
        "output": "SMBW_R/modules/exemple_module/output/romfs/",
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
            subprocess.run(["byml_to_yml"] + [args_pair["romfs"],args_pair["worktable"]], check=True)
    def compile():
        for args_pair in ressources:
            subprocess.run(["yml_to_byml"] + [args_pair["worktable"],args_pair["output"]], check=True)
    def clean():
        for args_pair in ressources:
            os.remove(args_pair["worktable"])
        os.remove("SMBW_R/modules/exemple_module/worktable/random_data.json")

class data_manager:
    def dump():
        # Dump is at JSON Format
        informations = {}
        count = 0
        for ressource in ressources:
            count = count + 1
            # Write Ressource Dumping               
        return informations
    
    def restore(data):
        # Dump is at JSON Format
        # Initialize Counter
        count = 0
        # Parcourir chaque monde
        for id, courses in data.items():
            count = count + 1
            ressource = ressources[count - 1]  # Les indices en Python commencent à 0
            with open(ressource["worktable"], "r") as fichier_yaml:  # Vous n'avez pas besoin de os.path.join ici
                yml_data = yaml.safe_load(fichier_yaml)
                # Use JSON Data for replace value on yml_data
            with open(ressource["worktable"], "w") as fichier_yaml:
                yaml.safe_dump(yml_data, fichier_yaml)

   
    def shuffle(levels_dump, method, seed):
        shuffle = False
        method = str(method)
        seed = str(seed)
        if method == "Full" or method == "full":
            levels_dump = profiles.full(levels_dump,seed)
            shuffle = True
        if shuffle == True:
            return levels_dump
        else:
            raise Exception("Unknown Randomisation Method")
