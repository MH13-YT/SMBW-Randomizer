import shutil
import os
import byml
from .profiles import profiles
from ...tools.zstandard import zs_file_manager

ressources = [
    {

        "romfs": "romfs/BancMapUnit",
        "worktable": "SMBW_R/modules/random_wonder/worktable/romfs/BancMapUnit",
        "output": "SMBW_R/modules/random_wonder/output/romfs/BancMapUnit",
    },
    {

        "romfs": "romfs/Stage/CourseInfo",
        "worktable": "SMBW_R/modules/random_wonder/worktable/romfs/Stage/CourseInfo",
        "output": "SMBW_R/modules/random_wonder/output/romfs/Stage/CourseInfo",
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
            print(f'Process {args_pair["romfs"]}')
            fichiers = os.listdir(args_pair["romfs"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["romfs"], fichier)
                if os.path.isfile(chemin_complet) and "BancMapUnit" in chemin_complet and "World" not in chemin_complet and "Course.bcett" not in chemin_complet and os.path.splitext(chemin_complet)[1] == '.zs':
                    zs_file_manager.decompress_zs(f'{args_pair["romfs"]}/{fichier}',f'{args_pair["worktable"]}/{fichier.replace(".zs", "")}')
                if os.path.isfile(chemin_complet) and "CourseInfo" in chemin_complet and os.path.splitext(chemin_complet)[1] == '.bgyml':
                    shutil.copy(f'{args_pair["romfs"]}/{fichier}', f'{args_pair["worktable"]}/{fichier}')
                    pass
    def compile():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet) and "BancMapUnit" in chemin_complet and "Course.bcett" not in chemin_complet and os.path.splitext(chemin_complet)[1] == '.byml':
                    if not zs_file_manager.compress_zs(f'{args_pair["worktable"]}/{fichier}',f'{args_pair["output"]}/{fichier.replace(".byml", ".byml.zs")}'):
                       raise ValueError(f"Cannot compress file : {chemin_complet}") 
                if os.path.isfile(chemin_complet) and "CourseInfo" in chemin_complet and os.path.splitext(chemin_complet)[1] == '.bgyml':
                    shutil.copy(f'{args_pair["worktable"]}/{fichier}', f'{args_pair["output"]}/{fichier}')
                    pass

    def clean():
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet) and os.path.splitext(chemin_complet)[1] != '.json':
                    pass
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
        if method == "all":
            data_dump = profiles.all(data_dump,seed)
            shuffle = True
        if method == "all_exclude_goomba":
            data_dump = profiles.all_exclude_goomba(data_dump,seed)
            shuffle = True
        if method == "morph_only":
            data_dump = profiles.morph_only(data_dump,seed)
            shuffle = True
        if method == "morph_only_exclude_goomba":
            data_dump = profiles.morph_only_exclude_goomba(data_dump,seed)
            shuffle = True
        if method == "effect_only":
            data_dump = profiles.effect_only(data_dump,seed)
            shuffle = True
        if method == "custom":
            data_dump = profiles.custom(data_dump,seed)
            shuffle = True
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
