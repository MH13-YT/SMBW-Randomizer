import os
import byml
from .profiles import profiles

ressources = [
    # Please select only folders in ressources, you can filter files on randomization procedure
    {
        "romfs": "romfs/",
        "worktable": "SMBW_R/modules/exemple_module/worktable/",
        "output": "SMBW_R/modules/exemple_module/output/romfs/",
    },
]

class file_converter:
    def get_ressources(): #DO NOT EDIT, These script are preconfigured
        return ressources
    def verify_files(): #DO NOT EDIT, These script are preconfigured
        for filepath in ressources:
            target = filepath["romfs"]
            if not os.path.exists(target):
                return False
        return True
    def decompile(): #DO NOT EDIT, These script are preconfigured
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["romfs"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["romfs"], fichier)
                if os.path.isfile(chemin_complet):
                    #shutil.copy(f'{args_pair["romfs"]}/{fichier}', f'{args_pair["worktable"]}/{fichier}')
                    #zs_file_manager.decompress_zs(f'{args_pair["romfs"]}/{fichier}',f'{args_pair["worktable"]}/{fichier.replace(".zs", "")}')
                    pass
    def compile(): #DO NOT EDIT, These script are preconfigured
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                if os.path.isfile(chemin_complet):
                    #shutil.copy(f'{args_pair["worktable"]}/{fichier}', f'{args_pair["output"]}/{fichier}')
                    #zs_file_manager.compress_zs(f'{args_pair["worktable"]}/{fichier}',f'{args_pair["output"]}/{fichier.replace(".byml", ".byml.zs")}'):
                    pass
    def clean(): #DO NOT EDIT, These script are preconfigured
        for args_pair in ressources:
            fichiers = os.listdir(args_pair["worktable"])
            for fichier in fichiers:
                chemin_complet = os.path.join(args_pair["worktable"], fichier)
                os.remove(chemin_complet)

class data_manager:
    def dump(): #DO NOT EDIT, These script are preconfigured
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

    def restore(data): #DO NOT EDIT, These script are preconfigured
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
