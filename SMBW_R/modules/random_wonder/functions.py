from .profiles import profiles

resources = [
    {
        "romfs": "romfs/BancMapUnit",
        "worktable": "worktable/romfs/BancMapUnit",
        "output": "output/romfs/BancMapUnit",
    },
    {
        "romfs": "romfs/Stage/CourseInfo",
        "worktable": "worktable/romfs/Stage/CourseInfo",
        "output": "output/romfs/Stage/CourseInfo",
    },
]


class file_converter:
    def get_resources():
        return resources


class data_manager:
    def shuffle(data_dump, method, seed):
        shuffle = False
        if method == "all":
            data_dump = profiles.all(data_dump, seed, False)
            shuffle = True
        if method == "all_secured":
            data_dump = profiles.all(data_dump, seed, True)
            shuffle = True
        if method == "all_exclude_goomba":
            data_dump = profiles.all_exclude_goomba(data_dump, seed, False)
            shuffle = True
        if method == "all_exclude_goomba_secured":
            data_dump = profiles.all_exclude_goomba(data_dump, seed, True)
            shuffle = True
        if method == "morph_only":
            data_dump = profiles.morph_only(data_dump, seed, False)
            shuffle = True
        if method == "morph_only_secured":
            data_dump = profiles.morph_only(data_dump, seed, True)
            shuffle = True
        if method == "morph_only_exclude_goomba":
            data_dump = profiles.morph_only_exclude_goomba(data_dump, seed, False)
            shuffle = True
        if method == "morph_only_exclude_goomba_secured":
            data_dump = profiles.morph_only_exclude_goomba(data_dump, seed, True)
            shuffle = True
        if method == "effect_only":
            data_dump = profiles.effect_only(data_dump, seed, False)
            shuffle = True
        if method == "effect_only_secured":
            data_dump = profiles.effect_only(data_dump, seed, True)
            shuffle = True
        if method == "custom":
            data_dump = profiles.custom(data_dump, seed, False)
            shuffle = True
        if method == "custom_secured":
            data_dump = profiles.custom(data_dump, seed, True)
            shuffle = True
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
