import copy
import random
class randomisation_functions:
    def enemy_shuffler(data_dump,enemy_list,seed):
        choose_enemy_list = {}
        random.seed(seed)
        for data in data_dump:
            if isinstance(data["file_data"], dict) and "BancMapUnit" in data["resource_type"] and "World" not in data["file_name"] and "Course.bcett" not in data["file_name"] and int(data["file_name"].split('_')[0][-3:]) < 900:
                for actors in data["file_data"]["Actors"]:
                    try:
                        if actors["Gyaml"].startswith("Enemy") and "Hanachan" not in actors["Gyaml"]:
                            random.shuffle(enemy_list)
                            actors["Gyaml"] = enemy_list[0]["enemy_name"]
                            choose_enemy_list[data["file_name"].split('_')[0]] = {"BancMapUnit":False, "data":copy.deepcopy(enemy_list[0])}
                    except Exception:
                        pass
        return data_dump