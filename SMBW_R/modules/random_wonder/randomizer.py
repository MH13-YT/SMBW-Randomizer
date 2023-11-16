import random
import byml

class randomisation_functions:
    def morph_shuffler(data_dump,morph_list,seed):
        list = {}
        random.seed(seed)
        for data in data_dump:
            if not data["file_name"].split('_')[0] in list:
                if "level_data" in data and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
                    morph_type = 0
                    for actors in data["level_data"]["Actors"]:
                        try:
                            if "MorphPlayerType" in actors["Dynamic"] and actors["Dynamic"]["MorphPlayerType"] == 0:
                                random.shuffle(morph_list)
                                list[data["file_name"].split('_')[0]] = {"BancMapUnit":False,"CourseInfo":False, "data":morph_list[0]}
                        except:
                            pass
            if "level_data" in data and data["file_name"].split('_')[0] in list and isinstance(data["level_data"], dict) and "CourseInfo" in data["ressource_type"]:
                data["level_data"].setdefault("CoursePlayerMorphType", "None")
                data["level_data"]["CoursePlayerMorphType"] = list[data["file_name"].split("_")[0]]["data"]["morph_name"]
                list[data["file_name"].split("_")[0]]["CourseInfo"] = True
            if "level_data" in data and data["file_name"].split('_')[0] in list and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
                morph_type = 0
                for actors in data["level_data"]["Actors"]:
                    try:
                        if "MorphPlayerType" in actors["Dynamic"]:
                            morph_type = actors["Dynamic"]["MorphPlayerType"]
                            if morph_type == 0:
                                actors["Dynamic"]["MorphPlayerType"] = byml.Int(list[data["file_name"].split("_")[0]]["data"]["morph_id"])
                                list[data["file_name"].split("_")[0]]["BancMapUnit"] = True
                    except:
                        pass
        return data_dump
    def effect_shuffler(data_dump,effect_list,seed):
        list = {}
        random.seed(seed)
        for data in data_dump:
            if not data["file_name"].split('_')[0] in list:
                if "level_data" in data and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
                    try:
                        for actors in data["level_data"]["Actors"]:
                            if "PlayerWonderType" in actors["Dynamic"]:
                                random.shuffle(effect_list)
                                list[data["file_name"].split('_')[0]] = {"BancMapUnit":False, "data":effect_list[0]}
                    except:
                        pass
            if "level_data" in data and data["file_name"].split('_')[0] in list and isinstance(data["level_data"], dict) and "BancMapUnit" in data["ressource_type"]:
                    try:
                        for actors in data["level_data"]["Actors"]:
                            if "PlayerWonderType" in actors["Dynamic"]:
                                actors["Dynamic"]["PlayerWonderType"] = byml.Int(list[data["file_name"].split("_")[0]]["data"]["effect_id"])
                                list[data["file_name"].split("_")[0]]["BancMapUnit"] = True
                    except:
                        pass
        print(f"Effects Data Modified")
        for course in list.items():
            print(course)
        return data_dump