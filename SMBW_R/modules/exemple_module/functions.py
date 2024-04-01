from .profiles import profiles

resources = [
    # Please select only folders in resources, you can filter files on randomization procedure
    {
        "romfs": "romfs/",
        "worktable": "worktable/",
        "output": "output/romfs/",
    },
]


class file_converter:
    def get_resources():
        return resources


class data_manager:
    def shuffle(data_dump, method, seed):
        shuffle = False
        method = str(method)
        seed = str(seed)
        if method == "Full" or method == "full":
            data_dump = profiles.full(data_dump, seed)
            shuffle = True
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
