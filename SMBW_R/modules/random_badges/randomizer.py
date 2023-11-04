import random

class randomisation_functions:
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