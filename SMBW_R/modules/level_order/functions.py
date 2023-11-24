import shutil
import os
import byml
from .profiles import profiles

ressources = [
    {
        "romfs": "romfs/Stage/WorldMapInfo",
        "worktable": "SMBW_R/modules/level_order/worktable/romfs/Stage/WorldMapInfo",
        "output": "SMBW_R/modules/level_order/output/romfs/Stage/WorldMapInfo",
    },
]

class file_converter:
    def get_ressources():
        return ressources
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
                    shutil.copy(f'{args_pair["romfs"]}/{fichier}', f'{args_pair["worktable"]}/{fichier}')
    def compile():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet):
                    shutil.copy(f'{args_pair["worktable"]}/{fichier}', f'{args_pair["output"]}/{fichier}')
    def clean():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                os.remove(chemin_complet)

class data_manager:
    def dump():
        data = []
        for ressource in ressources:
            print(f'Processing : {ressource["worktable"]}')
            fichiers = os.listdir(ressource["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(ressource["worktable"], fichier)
                if os.path.isfile(chemin_complet):
                        with open(f'{ressource["worktable"]}/{fichier}', "rb") as fichier_byml:
                            parser = byml.Byml(fichier_byml.read())
                            document = parser.parse()
                            data.append({
                                "file_name": fichier,
                                "ressource_type": ressource["worktable"],
                                "file_data": document
                            })
        return data

    def restore(data):
        for file in data[0]:
            if "file_name" in file and "ressource_type" in file and "file_data" in file:
                file_name = file["file_name"]
                ressources_type = file["ressource_type"]
                level_data = file["file_data"]
                file_path = os.path.join(ressources_type, file_name)
                with open(file_path, 'wb') as fichier:
                    writer = byml.Writer(level_data, be=False, version=4)
                    writer.write(fichier)
            else:
                print("Missing necessary information in level_info.")

   
    def shuffle(data_dump, method, seed):
        shuffle = False
        method = str(method)
        if method == "lite":
            data_dump = profiles.lite(data_dump,seed)
            shuffle = True
        if method == "full":
            data_dump = profiles.full(data_dump,seed)
            shuffle = True
        if method == "lite_secured":
            data_dump = profiles.lite_secured(data_dump,seed)
            shuffle = True
        if method == "full_secured":
            data_dump = profiles.full_secured(data_dump,seed)
            shuffle = True
        
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
