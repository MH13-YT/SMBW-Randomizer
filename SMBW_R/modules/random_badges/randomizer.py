import random

class randomisation_functions:
    def badge_shuffler(data_dump,badges_list,seed):
        random.seed(seed)
        for data in data_dump:
            random.shuffle(badges_list)
            if "file_data" in data and isinstance(data["file_data"], dict):
                course_type = ""
                try:
                    course_type = data["file_data"]["CourseKind"]
                except:
                    pass
                if course_type != "BadgeChallenge" and course_type != "BadgeMedley":
                    data["file_data"].setdefault("NeedBadgeIdEnterCourse", "Invalid")
                    data["file_data"]["NeedBadgeIdEnterCourse"] = badges_list[0]
        return data_dump