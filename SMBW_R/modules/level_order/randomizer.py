import json
import random
import re


class randomisation_scripts:
    def lite(data_dump, seed, security):
        random.seed(seed)
        data_config = {}
        try:
            with open( "SMBW_R/modules/level_order/data_config.json", 'r') as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                randomized_stagepath_with_secret_exits = []
                randomized_stagepath = []
                for course in data["file_data"]["CourseTable"]:
                    course_id = str("".join(re.findall(r"\d+", course["StagePath"])))
                    if int(course_id) < 900:
                        if f"Course{course_id}" not in data_config:
                            data_config[f"Course{course_id}"] = {"enabled":True,"hasSecretExit":False}
                        if data_config[f"Course{course_id}"]["enabled"] or security == False:
                            if data_config[f"Course{course_id}"]["hasSecretExit"] and security == True:
                                randomized_stagepath_with_secret_exits.append(course["StagePath"])
                            else:
                                randomized_stagepath.append(course["StagePath"])
                random.shuffle(randomized_stagepath)
                random.shuffle(randomized_stagepath_with_secret_exits)
                for course in data["file_data"]["CourseTable"]:
                    course_id = str("".join(re.findall(r"\d+", course["StagePath"])))
                    if int(course_id) < 900:
                        if data_config[f"Course{course_id}"]["enabled"] or security == False:
                            if data_config[f"Course{course_id}"]["hasSecretExit"] and security == True:
                                course["StagePath"] = randomized_stagepath_with_secret_exits.pop(0)
                            else:
                                course["StagePath"] = randomized_stagepath.pop(0)
        with open("SMBW_R/modules/level_order/data_config.json", 'w') as data_config_file:
                json.dump(data_config, data_config_file, indent=4, sort_keys=True)
        return data_dump

    def full(data_dump, seed, security):
        random.seed(seed)
        randomized_stagepath = []
        randomized_stagepath_with_secret_exits = []
        data_config = {}
        try:
            with open( "SMBW_R/modules/level_order/data_config.json", 'r') as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
            
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                for course in data["file_data"]["CourseTable"]:
                    course_id = str("".join(re.findall(r"\d+", course["StagePath"])))
                    if int(course_id) < 900:
                        if f"Course{course_id}" not in data_config:
                            data_config[f"Course{course_id}"] = {"enabled":True,"hasSecretExit":False}
                        if data_config[f"Course{course_id}"]["enabled"] or security == False:
                            if data_config[f"Course{course_id}"]["hasSecretExit"] and security == True:
                                randomized_stagepath_with_secret_exits.append(course["StagePath"])
                            else:
                                randomized_stagepath.append(course["StagePath"])
        random.shuffle(randomized_stagepath)
        random.shuffle(randomized_stagepath_with_secret_exits)
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                for course in data["file_data"]["CourseTable"]:
                    course_id = str("".join(re.findall(r"\d+", course["StagePath"])))
                    if int(course_id) < 900:
                        if data_config[f"Course{course_id}"]["enabled"] or security == False:
                            if data_config[f"Course{course_id}"]["hasSecretExit"] and security == True:
                                course["StagePath"] = randomized_stagepath_with_secret_exits.pop(0)
                            else:
                                course["StagePath"] = randomized_stagepath.pop(0)
        with open("SMBW_R/modules/level_order/data_config.json", 'w') as data_config_file:
                json.dump(data_config, data_config_file, indent=4, sort_keys=True)
        return data_dump
