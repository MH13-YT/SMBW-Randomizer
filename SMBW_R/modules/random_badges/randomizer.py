import random

class randomisation_functions:
    def badge_shuffler(data_dump,badges_list,seed):
        random.seed(seed)
        for data in data_dump:
            random.shuffle(badges_list)
            if "file_data" in data and isinstance(data["file_data"], dict) and "Stage/CourseInfo" in data["ressource_type"]:
                course_type = ""
                try:
                    course_type = data["file_data"]["CourseKind"]
                except:
                    pass
                if course_type != "BadgeChallenge" and course_type != "BadgeMedley" and course_type != "StaffCredit" and course_type != "StoryTeller" and course_type != "DemoCourse" or data["file_data"]["CourseKind"] == "Opening":
                    data["file_data"].setdefault("NeedBadgeIdEnterCourse", "Invalid")
                    data["file_data"]["NeedBadgeIdEnterCourse"] = badges_list[0]
        return data_dump