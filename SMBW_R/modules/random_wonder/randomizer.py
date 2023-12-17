import copy
import json
import random
import byml


class randomisation_functions:
    def morph_shuffler(data_dump, morph_list, seed, security):
        data_config = {}
        try:
            with open(
                "SMBW_R/modules/random_wonder/data_config.json", "r"
            ) as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
        choose_morph_list = {}
        random.seed(seed)
        for data in data_dump:
            if (
                not data["file_name"].split("_")[0] in choose_morph_list
                and (
                    "file_data" in data
                    and isinstance(data["file_data"], dict)
                    and "BancMapUnit" in data["resource_type"]
                    and "World" not in data["file_name"]
                    and "Course.bcett" not in data["file_name"]
                )
                and int(data["file_name"].split("_")[0][-3:]) < 900
            ):
                course_id = str(data["file_name"].split("_")[0][-3:])
                for actors in data["file_data"]["Actors"]:
                    try:
                        if (
                            "MorphPlayerType" in actors["Dynamic"]
                            and actors["Dynamic"]["MorphPlayerType"] == 0
                        ):
                            if f"Course{course_id}" not in data_config:
                                data_config[f"Course{course_id}"] = {
                                    "Morph": True,
                                    "Effect": True,
                                }
                                if (
                                    data_config[f"Course{course_id}"]["Morph"]
                                    or security == False
                                ):
                                    random.shuffle(morph_list)
                                    choose_morph_list[
                                        data["file_name"].split("_")[0]
                                    ] = {
                                        "BancMapUnit": False,
                                        "CourseInfo": False,
                                        "data": copy.deepcopy(morph_list[0]),
                                    }
                    except Exception:
                        pass
        for data in data_dump:
            course_id = str(data["file_name"].split("_")[0][-3:])
            if (
                "file_data" in data
                and data["file_name"].split("_")[0] in choose_morph_list
                and isinstance(data["file_data"], dict)
                and "CourseInfo" in data["resource_type"]
            ):
                test_course_kind = False
                try:
                    test_course_kind = (
                        data["file_data"]["CourseKind"] == "StaffCredit"
                        or data["file_data"]["CourseKind"] == "StoryTeller"
                        or data["file_data"]["CourseKind"] == "DemoCourse"
                        or data["file_data"]["CourseKind"] == "Opening"
                    )
                except Exception:
                    pass
                if test_course_kind == False:
                    data["file_data"].setdefault("CoursePlayerMorphType", "None")
                    data["file_data"]["CoursePlayerMorphType"] = copy.deepcopy(
                        choose_morph_list[data["file_name"].split("_")[0]]["data"][
                            "morph_name"
                        ]
                    )
                    choose_morph_list[data["file_name"].split("_")[0]][
                        "CourseInfo"
                    ] = True
            if (
                "file_data" in data
                and data["file_name"].split("_")[0] in choose_morph_list
                and isinstance(data["file_data"], dict)
                and "BancMapUnit" in data["resource_type"]
                and "World" not in data["file_name"]
                and "Course.bcett" not in data["file_name"]
            ):
                morph_type = 0
                for actors in data["file_data"]["Actors"]:
                    try:
                        if (
                            "MorphPlayerType" in actors["Dynamic"]
                            and actors["Dynamic"]["MorphPlayerType"] == 0
                        ):
                            actors["Dynamic"]["MorphPlayerType"] = byml.Int(
                                copy.deepcopy(
                                    choose_morph_list[data["file_name"].split("_")[0]][
                                        "data"
                                    ]["morph_id"]
                                )
                            )
                            choose_morph_list[data["file_name"].split("_")[0]][
                                "BancMapUnit"
                            ] = True
                    except Exception:
                        pass
        with open(
            "SMBW_R/modules/random_wonder/data_config.json", "w"
        ) as data_config_file:
            json.dump(data_config, data_config_file, indent=4, sort_keys=True)
        return data_dump

    def effect_shuffler(data_dump, effect_list, seed, security):
        data_config = {}
        try:
            with open(
                "SMBW_R/modules/random_wonder/data_config.json", "r"
            ) as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
        choose_effect_list = {}
        random.seed(seed)
        for data in data_dump:
            course_id = str(data["file_name"].split("_")[0][-3:])
            if (
                isinstance(data["file_data"], dict)
                and "BancMapUnit" in data["resource_type"]
                and "World" not in data["file_name"]
                and "Course.bcett" not in data["file_name"]
                and int(data["file_name"].split("_")[0][-3:]) < 900
            ):
                for actors in data["file_data"]["Actors"]:
                    try:
                        if "PlayerWonderType" in actors["Dynamic"]:
                            if (
                                data_config[f"Course{course_id}"]["Effect"]
                                or security == False
                            ):
                                random.shuffle(effect_list)
                                actors["Dynamic"]["PlayerWonderType"] = byml.Int(
                                    copy.deepcopy(effect_list[0]["effect_id"])
                                )
                                choose_effect_list[data["file_name"].split("_")[0]] = {
                                    "BancMapUnit": False,
                                    "data": copy.deepcopy(effect_list[0]),
                                }
                    except Exception:
                        pass
        return data_dump
