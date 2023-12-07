from .profiles import profiles

resources = [
    {
        "romfs": "romfs/Stage/WorldMapInfo",
        "worktable": "worktable/romfs/Stage/WorldMapInfo",
        "output": "output/romfs/Stage/WorldMapInfo",
    },
]


class file_converter:
    def get_resources():
        return resources


class data_manager:
    def shuffle(data_dump, method, seed):
        shuffle = False
        method = str(method)
        if method == "lite":
            data_dump = profiles.lite(data_dump, seed)
            shuffle = True
        if method == "full":
            data_dump = profiles.full(data_dump, seed)
            shuffle = True
        if method == "lite_secured":
            data_dump = profiles.lite_secured(data_dump, seed)
            shuffle = True
        if method == "full_secured":
            data_dump = profiles.full_secured(data_dump, seed)
            shuffle = True

        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
