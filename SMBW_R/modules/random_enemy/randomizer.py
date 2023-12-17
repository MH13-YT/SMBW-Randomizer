import copy
import json
import random
class randomisation_functions:
    def enemy_shuffler(data_dump,enemy_list,seed,security):
        choose_enemy_list = {}
        data_config = {}
        try:
            with open( "SMBW_R/modules/random_enemy/data_config.json", 'r') as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
        random.seed(seed)
        for data in data_dump:
            course_id = str(data["file_name"].split('_')[0][-3:])
            if isinstance(data["file_data"], dict) and "BancMapUnit" in data["resource_type"] and "World" not in data["file_name"] and "Course.bcett" not in data["file_name"] and int(data["file_name"].split('_')[0][-3:]) < 900:
                if f"Course{course_id}" not in data_config:
                    data_config[f"Course{course_id}"] = {"enabled":True}
                if data_config[f"Course{course_id}"]["enabled"] or security == False:
                    for actors in data["file_data"]["Actors"]:
                        try:
                            if actors["Gyaml"].startswith("Enemy") and "Hanachan" not in actors["Gyaml"]:
                                random.shuffle(enemy_list)
                                actors["Gyaml"] = enemy_list[0]["enemy_name"]
                                choose_enemy_list[data["file_name"].split('_')[0]] = {"BancMapUnit":False, "data":copy.deepcopy(enemy_list[0])}
                        except Exception:
                            pass
        with open("SMBW_R/modules/random_enemy/data_config.json", 'w') as data_config_file:
            json.dump(data_config, data_config_file, indent=4, sort_keys=True)
        return data_dump