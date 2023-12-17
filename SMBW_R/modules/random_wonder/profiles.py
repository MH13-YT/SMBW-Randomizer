import json
from .randomizer import randomisation_functions
from .gui import custom_effect_gui, custom_morph_gui


def morphs_filter(data_dump):
    morphs = {}
    for data in data_dump:
        if (
            "level_data" in data
            and isinstance(data["level_data"], dict)
            and "BancMapUnit" in data["resource_type"]
        ):
            try:
                if "Actors" in data["level_data"]:
                    for actors in data["level_data"]["Actors"]:
                        if (
                            "Dynamic" in actors
                            and "MorphPlayerType" in actors["Dynamic"]
                            and actors["Dynamic"]["MorphPlayerType"] != 0
                        ):
                            course_id = data["file_name"].split("_")[0]

                            key = f"{course_id}"

                            if key in morphs:
                                morphs[key]["morph_id"] = actors["Dynamic"][
                                    "MorphPlayerType"
                                ]
                            else:
                                morphs[key] = {
                                    "morph_name": "",
                                    "morph_id": actors["Dynamic"]["MorphPlayerType"],
                                }
                        else:
                            if (
                                "Dynamic" in actors
                                and "MorphPlayerType" in actors["Dynamic"]
                            ):
                                pass
            except:
                pass
        if (
            "level_data" in data
            and isinstance(data["level_data"], dict)
            and "CourseInfo" in data["resource_type"]
        ):
            try:
                course_id = data["file_name"].split("_")[0]

                key = f"{course_id}"
                if str(data["level_data"]["CoursePlayerMorphType"]) != "":
                    if key in morphs:
                        morphs[key]["morph_name"] = str(
                            data["level_data"]["CoursePlayerMorphType"]
                        )
                    else:
                        morphs[key] = {
                            "morph_name": str(
                                data["level_data"]["CoursePlayerMorphType"]
                            ),
                            "morph_id": "",
                        }
            except:
                pass

    morphs_list = [
        dict(t)
        for t in {tuple(d.items()) for d in list(morphs.values())}
        if all(v != "" and v is not None for k, v in t)
    ]
    print("Wonder Morph List")
    print(morphs_list)
    return morphs_list


def custom_morph_selector():
    try:
        with open("SMBW_R/modules/random_wonder/morph_config.json", "r") as json_file:
            data = json.load(json_file)
            morphs = []

            for morph_name, morph_data in data.items():
                if morph_data.get("enabled", False):
                    morphs.append(
                        {
                            "morph_name": morph_data["codename"],
                            "morph_id": morph_data["id"],
                        }
                    )

            return morphs
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


def morphs_filter(ignore):
    try:
        with open("SMBW_R/modules/random_wonder/morph_config.json", "r") as json_file:
            data = json.load(json_file)
            morphs = []

            for morph_name, morph_data in data.items():
                if morph_data.get("codename", "") != ignore or ignore == "All":
                    morphs.append(
                        {
                            "morph_name": morph_data["codename"],
                            "morph_id": morph_data["id"],
                        }
                    )

            return morphs
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


def effects_filter(ignore):
    try:
        with open("SMBW_R/modules/random_wonder/effect_config.json", "r") as json_file:
            data = json.load(json_file)
            effects = []

            for effect_name, effect_data in data.items():
                if effect_name != ignore or ignore == "All":
                    effects.append({"effect_id": effect_data["id"]})
            return effects
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


def custom_effect_selector():
    try:
        with open("SMBW_R/modules/random_wonder/effect_config.json", "r") as json_file:
            data = json.load(json_file)
            effects = []

            for effect_name, effect_data in data.items():
                if effect_data.get("enabled", False):
                    effects.append({"effect_id": effect_data["id"]})
            return effects
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


class profiles:
    def list():
        return [
            "all",
            "all_secured",
            "all_exclude_goomba",
            "all_exclude_goomba_secured",
            "morph_only",
            "morph_only_secured",
            "morph_only_exclude_goomba",
            "morph_only_exclude_goomba_secured",
            "effect_only",
            "effect_only_secured",
            "custom",
            "custom_secured",
        ]

    def all(data_dump, seed, security):
        morph_dump = morphs_filter("All")
        effect_dump = effects_filter(data_dump)
        data_dump = randomisation_functions.morph_shuffler(
            data_dump, morph_dump, seed, security
        )
        data_dump = randomisation_functions.effect_shuffler(
            data_dump, effect_dump, seed, security
        )
        return data_dump

    def all_exclude_goomba(data_dump, seed, security):
        morph_dump = morphs_filter("Kuribo")
        effect_dump = effects_filter("All")
        data_dump = randomisation_functions.morph_shuffler(
            data_dump, morph_dump, seed, security
        )
        data_dump = randomisation_functions.effect_shuffler(
            data_dump, effect_dump, seed, security
        )
        return data_dump

    def morph_only(data_dump, seed, security):
        morph_dump = morphs_filter("All")
        data_dump = randomisation_functions.morph_shuffler(
            data_dump, morph_dump, seed, security
        )
        return data_dump

    def morph_only_exclude_goomba(data_dump, seed, security):
        morph_dump = morphs_filter("Kuribo")
        data_dump = randomisation_functions.morph_shuffler(
            data_dump, morph_dump, seed, security
        )
        return data_dump

    def effect_only(data_dump, seed, security):
        effect_dump = effects_filter("All")
        data_dump = randomisation_functions.effect_shuffler(
            data_dump, effect_dump, seed, security
        )
        return data_dump

    def custom(data_dump, seed, security):
        custom_morph_gui.custom_morph_list_configurator()
        custom_effect_gui.custom_effect_list_configurator()
        if len(custom_morph_selector()) > 0:
            data_dump = randomisation_functions.morph_shuffler(
                data_dump, custom_morph_selector(), seed, security
            )
        if len(custom_effect_selector()) > 0:
            data_dump = randomisation_functions.effect_shuffler(
                data_dump, custom_effect_selector(), seed, security
            )
        return data_dump
