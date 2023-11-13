import random

class randomisation_functions:
    def morph_shuffler(data_dump,morph_list,seed):
        list = {}
        random.seed(seed)
        for data in data_dump:
            if not data["file_name"].split('_')[0] in list:
                random.shuffle(morph_list)
                list[data["file_name"].split('_')[0]] = morph_list[0]
            if "level_data" in data and isinstance(data["level_data"], dict) and "CourseInfo" in data["ressource_type"]:
                morph_type = ""
                try:
                    morph_type = data["level_data"]["CoursePlayerMorphType"]
                except:
                    pass
                if morph_type == "":
                    data["level_data"].setdefault("CoursePlayerMorphType", "None")
                    data["level_data"]["CoursePlayerMorphType"] = list[data["file_name"].split("_")[0]]["morph_name"]
            if "level_data" in data and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
                morph_type = 0
                try:
                    for actors in data["level_data"]["Actors"]:
                        if "MorphPlayerType" in actors["Dynamic"]:
                            morph_type = actors["Dynamic"]["MorphPlayerType"]
                except:
                    pass
                if morph_type == 0:
                    try:
                        for actors in data["level_data"]["Actors"]:
                            if "MorphPlayerType" in actors["Dynamic"]:
                                actors["Dynamic"]["MorphPlayerType"] = list[data["file_name"].split("_")[0]]["morph_id"]
                    except:
                        pass
        return data_dump