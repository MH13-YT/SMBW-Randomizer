import json
from .randomizer import randomisation_functions
    
def morph_dumper(data_dump):
    morphs = {}
    for data in data_dump:
        if "level_data" in data and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
            try:
                if "Actors" in data["level_data"]:
                    for actors in data["level_data"]["Actors"]:
                        if "Dynamic" in actors and "MorphPlayerType" in actors["Dynamic"] and actors["Dynamic"]["MorphPlayerType"] != 0:
                            course_id = data["file_name"].split("_")[0]
                            # Créer une clé unique basée sur course_id et morph_name
                            key = f"{course_id}"
                            # Vérifier si la clé existe déjà
                            if key in morphs:
                                # Mettre à jour les données
                                morphs[key]["morph_id"] = actors["Dynamic"]["MorphPlayerType"]
                            else:
                                # Ajouter une nouvelle entrée
                                morphs[key] = {
                                    "morph_name": "",
                                    "morph_id": actors["Dynamic"]["MorphPlayerType"]
                                }
                        else:
                            if "Dynamic" in actors and "MorphPlayerType" in actors["Dynamic"]:
                                pass
            except:
                pass
        if "level_data" in data and isinstance(data["level_data"], dict) and "CourseInfo" in data["ressource_type"]:
            try:
                course_id = data["file_name"].split("_")[0]
                # Créer une clé unique basée sur course_id et morph_name
                key = f"{course_id}"
                if str(data["level_data"]["CoursePlayerMorphType"]) != "":
                    # Vérifier si la clé existe déjà
                    if key in morphs:
                        # Mettre à jour les données
                        morphs[key]["morph_name"] = str(data["level_data"]["CoursePlayerMorphType"])
                    else:
                        # Ajouter une nouvelle entrée
                        morphs[key] = {
                            "morph_name": str(data["level_data"]["CoursePlayerMorphType"]),
                            "morph_id": ""
                        }
            except:
                pass
    # Supprimer les doublons en utilisant une liste de compréhension
    morphs_list = [dict(t) for t in {tuple(d.items()) for d in list(morphs.values())} if all(v != '' and v is not None for k, v in t)]
    return morphs_list
            

        
class profiles:

    def list():
        return [
            'all',
            ]

    def all(data_dump, seed):
        return randomisation_functions.morph_shuffler(data_dump,morph_dumper(data_dump),seed)

