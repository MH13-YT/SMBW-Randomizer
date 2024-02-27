import os
import shutil
import hashlib

from tqdm import tqdm

modded_file_list = []

def generate_folder_hash(folder):
    # Initialise un objet de hachage
    folder_hash = hashlib.sha256()

    # Liste les fichiers et sous-dossiers dans le dossier
    file_list = sorted(os.listdir(folder))

    # Parcours tous les fichiers et sous-dossiers dans le dossier
    for file in file_list:
        file_path = os.path.join(folder, file)
        
        # Si le chemin est un dossier, appelle récursivement la fonction sur ce dossier
        if os.path.isdir(file_path):
            folder_hash.update(generate_folder_hash(file_path).encode())
        else:
            # Si le chemin est un fichier, lit le contenu du fichier et met à jour le hachage
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    folder_hash.update(data)

    # Retourne le hachage hexadécimal
    return folder_hash.hexdigest()

mods_folder = "mods"

def synchronize_romfs():
    # Génère les hachages pour chaque dossier
    if os.path.isdir(os.path.join("romfs_backup")):
        print("Generating Hashes From romfs and romfs_backup folder")
        romfs_hash = generate_folder_hash(os.path.join("romfs"))
        print("romfs folder hash Generated ")
        romfs_backup_hash = generate_folder_hash(os.path.join("romfs_backup"))
        print("romfs_backup folder hash Generated")
        # Compare les hachages
        if romfs_hash != romfs_backup_hash:
            print("Hashes isn't corresponding")
            backup_romfs()
    else:
        backup_romfs()

def get_mods_list():
    mods_list = []
    mod_file_list = []
    for mod in os.listdir(mods_folder):
        mod_path = os.path.join(mods_folder, mod)
        mod_romfs_path = os.path.join(mod_path, "romfs")
        if os.path.isdir(mod_romfs_path):
            for root, dirs, filenames in os.walk(mod_romfs_path):
                for filename in filenames:
                    if "rsizetable" not in filename:
                        mod_file_list.append({"filename":filename, "path":os.path.join(root, filename)})
            mods_list.append({"mod_name": mod, "mod_file_list": mod_file_list.copy()})
            mod_file_list.clear()
    return mods_list

def get_modded_file_list():
    return modded_file_list

def backup_romfs():
    if os.path.isdir("romfs_backup"):
        print("Removing Old Backup")
        shutil.rmtree("romfs_backup")
        print("Old Backup Removed")
        input()
    print("Starting RomFS Backup")
    shutil.copytree("romfs", "romfs_backup")
    print("RomFS Backup Complete")

def restore_romfs():
    modded_file_list.clear()
    print("Removing Patched RomFS")
    shutil.rmtree("romfs")
    print("Patched RomFS Removed")
    input()
    print("Recreating RomFS Folder From Backup")
    shutil.copytree("romfs_backup", "romfs")
    print("RomFS Restore Complete")

def patch_game(selected_mod_list):
    print(selected_mod_list)
    input()
    synchronize_romfs()
    mod_list = get_mods_list()
    for mod_name in selected_mod_list:
        print(f"Processing : {mod_name}")
        for mod in mod_list:
            if mod["mod_name"] == mod_name:
                for mod_file in mod["mod_file_list"]:
                    print(f'Processing File : {os.path.join(mod_file["path"])}')
                    shutil.copyfile(mod_file["path"], os.path.join(*mod_file["path"].split(os.sep)[2:]))
                    modded_file_list.append(os.path.join(*mod_file["path"].split(os.sep)[2:]))
        print(f"Processed : {mod_name}")
    return
    