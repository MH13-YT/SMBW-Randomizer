from .randomizer import randomisation_functions

class profiles:

    def list():
        return [
            'start_with',
            ]

    def start_with(data_dump, seed):
        ignored_files = [
        ]
        badges = set([]) # Add Badges id who are not forced on a level (Shop Badges and 100% Reward Badge)
        for data in data_dump["levels"]:
            if "level_data" in data and isinstance(data["level_data"], dict):
                try:
                    if data["level_data"]["NeedBadgeIdEnterCourse"] != "Invalid":
                        badges.add(data["level_data"]["NeedBadgeIdEnterCourse"])
                except:
                    pass
        return randomisation_functions.badge_shuffler(data_dump,list(badges),seed)

