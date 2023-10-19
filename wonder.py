import subprocess
import os
import yaml
import uuid
from randomizer import world_profiles

ressources = [
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World001.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World001.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World001.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World002.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World002.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World002.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World003.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World003.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World003.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World004.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World004.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World004.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World005.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World005.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World005.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World006.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World006.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World006.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World007.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World007.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World007.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World008.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World008.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World008.game__stage__WorldMapInfo.bgyml"
    },
    {
        "type": "world_file",
        "romfs": "romfs/Stage/WorldMapInfo/World009.game__stage__WorldMapInfo.bgyml",
        "worktable": "worktable/World009.game__stage__WorldMapInfo.yml",
        "output": "output/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo/World009.game__stage__WorldMapInfo.bgyml"
    },
]

class file_converter:
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
            print(f"Cleaning: {args_pair['worktable']}")
            os.remove(args_pair["worktable"])
        print(f"Cleaning: worktable/random_levels.json")
        os.remove("worktable/random_levels.json")

class levels_manager:
    def dump():
        # Initialiser un dictionnaire pour stocker les informations
        informations = {}
        count = 0
        for ressource in ressources:
            count = count + 1
            world_id = f"World{count}"  # Utilisation de World-ID formaté
            if world_id not in informations:
                informations[world_id] = []  # Crée une liste vide pour chaque World-ID

            with open(ressource["worktable"], "r") as fichier_yaml:  # Vous n'avez pas besoin de os.path.join ici
                data = yaml.safe_load(fichier_yaml)
                for item in data.get("CourseTable", []):
                    key = item.get("Key", None)
                    stage_path = item.get("StagePath", None)
                    if key is not None and stage_path is not None:
                        # Ajoutez les informations à la liste correspondante
                        if stage_path != "Work/Stage/StageParam/Course900_Course.game__stage__StageParam.gyml":
                            informations[world_id].append({"Key": key, "StagePath": stage_path})               
        return informations
    
    def restore(data):
        # Initialiser un compteur
        count = 0
        # Parcourir chaque monde
        for world_id, courses in data.items():
            count = count + 1
            ressource = ressources[count - 1]  # Les indices en Python commencent à 0
            with open(ressource["worktable"], "r") as fichier_yaml:  # Vous n'avez pas besoin de os.path.join ici
                yml_data = yaml.safe_load(fichier_yaml)
                for i, item in enumerate(yml_data.get("CourseTable", [])):
                    # Définir les nouvelles valeurs pour "Key" et "StagePath"
                    if i < len(courses):  # Vérifiez que nous n'excédons pas la longueur de courses
                        for course in courses:
                            if course["Key"] == item["Key"]:  # Utilisez item["Key"] pour rechercher un correspondant dans courses
                                item["Key"] = course["Key"]
                                item["StagePath"] = course["StagePath"]
                                break
            with open(ressource["worktable"], "w") as fichier_yaml:
                yaml.safe_dump(yml_data, fichier_yaml)

   
    def shuffle(levels_dump, method, seed):
        shuffle = False
        method = str(method)
        seed = str(seed)
        if seed == "" or seed == "None":
            seed = str(uuid.uuid4())
        if method == "Lite" or method == "lite":
            levels_dump = world_profiles.lite(levels_dump,seed)
            shuffle = True
        if method == "Full" or method == "full":
            levels_dump = world_profiles.full(levels_dump,seed)
            shuffle = True
        
        if shuffle == True:
            return levels_dump
        else:
            raise Exception("Unknown Randomisation Method")
