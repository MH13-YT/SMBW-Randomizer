import random


class profiles:

    def list():
        return [
            'start_with',
            ]

    def start_with(data_dump, seed):
        ignored_files = [
        ]
        random.seed(seed)
        badges = set([]) # Add Badges id who are not forced on a level (Shop Badges and 100% Reward Badge)
        for data in data_dump["levels"]:
            if "level_data" in data and isinstance(data["level_data"], dict):
                try:
                    if data["level_data"]["NeedBadgeIdEnterCourse"] != "Invalid":
                        badges.add(data["level_data"]["NeedBadgeIdEnterCourse"])
                except:
                    pass
        badges_list = list(badges)
        for data in data_dump["levels"]:
            random.shuffle(badges_list)
            if "level_data" in data and isinstance(data["level_data"], dict):
                data["level_data"].setdefault("NeedBadgeIdEnterCourse", "Invalid")
                data["level_data"]["NeedBadgeIdEnterCourse"] = badges_list[0]
        return data_dump
