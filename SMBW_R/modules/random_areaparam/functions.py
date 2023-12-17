import json
import os
import byml
from .profiles import profiles

resources = [
    {
        "romfs": "romfs/Stage/AreaParam",
        "worktable": "worktable/romfs/Stage/AreaParam",
        "output": "output/romfs/Stage/AreaParam",
    },
]


class file_converter:
    def get_resources():
        return resources


class data_manager:
    def shuffle(levels_dump, method, seed):
        shuffle = False
        method = str(method)
        seed = str(seed)
        with open(
            "SMBW_R/modules/random_areaparam/areaparam_config.json", "r"
        ) as json_file:
            areaparam_data = json.load(json_file)
        if method == "All" or method == "all":
            levels_dump = profiles.all(levels_dump, seed, areaparam_data ,False)
            shuffle = True
        if method == "All_secured" or method == "all_secured":
            levels_dump = profiles.all(levels_dump, seed, areaparam_data, True)
            shuffle = True
        if shuffle == True:
            return levels_dump
        else:
            raise Exception("Unknown Randomisation Method")
