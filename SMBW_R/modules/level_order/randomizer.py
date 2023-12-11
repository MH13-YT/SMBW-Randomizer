import random
import re


class randomisation_scripts:
    def lite(data_dump, seed, ignored_stages_files):
        random.seed(seed)
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                randomized_stagepath = []
                for course in data["file_data"]["CourseTable"]:
                    if (
                        not course["StagePath"] in ignored_stages_files
                        and int(''.join(re.findall(r'\d+', course["StagePath"])))
                        < 900
                    ):
                        randomized_stagepath.append(course["StagePath"])
                random.shuffle(randomized_stagepath)
                for course in data["file_data"]["CourseTable"]:
                    if (
                        not course["StagePath"] in ignored_stages_files
                        and int(''.join(re.findall(r'\d+', course["StagePath"]))) < 900
                    ):
                        course["StagePath"] = randomized_stagepath.pop(0)
        return data_dump

    def full(data_dump, seed, ignored_stages_files):
        random.seed(seed)
        randomized_stagepath = []
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                for course in data["file_data"]["CourseTable"]:
                    if (
                        not course["StagePath"] in ignored_stages_files
                        and int(''.join(re.findall(r'\d+', course["StagePath"]))) < 900
                    ):
                        randomized_stagepath.append(course["StagePath"])
        random.shuffle(randomized_stagepath)
        for data in data_dump:
            if (
                "file_data" in data
                and isinstance(data["file_data"], dict)
                and "Stage/WorldMapInfo" in data["resource_type"]
            ):
                for course in data["file_data"]["CourseTable"]:
                    if (
                        not course["StagePath"] in ignored_stages_files
                        and int(''.join(re.findall(r'\d+', course["StagePath"]))) < 900
                    ):
                        course["StagePath"] = randomized_stagepath.pop(0)
        return data_dump
