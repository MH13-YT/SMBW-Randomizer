import random

def badge_shuffler(data_dump,badges_list,seed):
    random.seed(seed)
    for data in data_dump["levels"]:
        random.shuffle(badges_list)
        if "level_data" in data and isinstance(data["level_data"], dict):
            course_type = ""
            try:
                course_type = data["level_data"]["CourseKind"]
            except:
                pass
            if course_type != "BadgeChallenge" and course_type != "BadgeMedley":
                data["level_data"].setdefault("NeedBadgeIdEnterCourse", "Invalid")
                data["level_data"]["NeedBadgeIdEnterCourse"] = badges_list[0]
    return data_dump

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
        return badge_shuffler(data_dump,list(badges),seed)

