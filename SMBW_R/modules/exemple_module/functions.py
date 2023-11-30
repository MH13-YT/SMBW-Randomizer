import os
import byml
from .profiles import profiles

ressources = [
    # Please select only folders in ressources, you can filter files on randomization procedure
    {
        "romfs": "romfs/",
        "worktable": "worktable/",
        "output": "output/romfs/",
    },
]

class file_converter:
    def get_ressources():
        return ressources

class data_manager:
    def shuffle(levels_dump, method, seed):
        shuffle = False
        method = str(method)
        seed = str(seed)
        if method == "Full" or method == "full":
            levels_dump = profiles.full(levels_dump,seed)
            shuffle = True
        if shuffle == True:
            return levels_dump
        else:
            raise Exception("Unknown Randomisation Method")
