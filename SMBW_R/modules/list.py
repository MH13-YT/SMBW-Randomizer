import os
module_folder = "SMBW_R/modules"
def get_module_list():
    # Vérifiez si le chemin existe
    if os.path.exists(module_folder):
    # Utilisez la fonction os.listdir pour obtenir la liste des éléments du répertoire
        elements = os.listdir(module_folder)

    # Filtrez les éléments pour n'inclure que les dossiers (répertoires)
        return [element for element in elements if os.path.isdir(os.path.join(module_folder, element)) and element != '__pycache__' and element != 'exemple_module']
    
    else:
        return []