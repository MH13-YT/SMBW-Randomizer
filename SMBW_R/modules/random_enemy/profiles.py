import json
from .randomizer import randomisation_functions
from .gui import custom_enemy_gui, custom_enemy_gui


def enemys_filter(ignore):
    try:
        with open("SMBW_R/modules/random_enemy/enemy_config.json", "r") as json_file:
            data = json.load(json_file)
            enemys = []

            for enemy_name, enemy_data in data.items():
                if enemy_name != ignore or ignore == "All":
                    enemys.append({"enemy_name": enemy_data["enemy_name"]})
            return enemys
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


def custom_enemy_selector():
    try:
        with open("SMBW_R/modules/random_enemy/enemy_config.json", "r") as json_file:
            data = json.load(json_file)
            enemys = []

            for enemy_name, enemy_data in data.items():
                if enemy_data.get("enabled", False):
                    enemys.append({"enemy_name": enemy_data["enemy_name"]})
            return enemys
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []


class profiles:
    def list():
        return ["all","all_secured", "custom","custom_secured"]

    def all(data_dump, seed,security):
        enemy_dump = enemys_filter("All")
        data_dump = randomisation_functions.enemy_shuffler(data_dump, enemy_dump, seed,security)
        return data_dump

    def custom(data_dump, seed,security):
        custom_enemy_gui.custom_enemy_list_configurator()
        if len(custom_enemy_selector()) > 0:
            data_dump = randomisation_functions.enemy_shuffler(
                data_dump, custom_enemy_selector(), seed ,security
            )
        return data_dump
