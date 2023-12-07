from .profiles import profiles

resources = [
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
            data_dump = profiles.all(data_dump, seed)
            shuffle = True
        if method == "action_only":
            data_dump = profiles.action_only(data_dump, seed)
            shuffle = True
        if method == "bonus_only":
            data_dump = profiles.bonus_only(data_dump, seed)
            shuffle = True
        if method == "expert_only":
            data_dump = profiles.expert_only(data_dump, seed)
            shuffle = True
        if method == "custom":
            data_dump = profiles.custom(data_dump, seed)
            shuffle = True
        if shuffle == True:
            return data_dump
        else:
            raise Exception("Unknown Randomisation Method")
