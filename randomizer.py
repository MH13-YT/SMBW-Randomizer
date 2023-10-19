import random


class world_profiles:
    def list():
        return [
            {
                "method": "full", 
                "description": "All levels are randomized"
            },
            {
                "method": "lite",
                "description": "Levels are grouped by world and then randomized between them",
            },
        ]

    def full(levels_dump, seed):
        ignored_stages_files = [
            "Work/Stage/StageParam/Course590_Course.game__stage__StageParam.gyml",
        ]
        print(f"Use 'Full' Randomisation with seed: '{seed}'")
        print(f'Description of method: {world_profiles.list()[0]["description"]}')

        # Fusionnez tous les niveaux de différents mondes en un seul tableau
        all_levels = []
        for monde_num in range(
            1, 10
        ):  # J'ai changé la limite à 10 pour inclure le monde 9
            monde_a_randomiser = f"World{monde_num}"
            if monde_a_randomiser in levels_dump:
                niveaux_monde = levels_dump[monde_a_randomiser]
                all_levels.extend(niveaux_monde)

        # Extrayez les stage_paths des niveaux à ignorer
        stage_paths_ignored = [
            course["StagePath"]
            for course in all_levels
            if course["StagePath"] in ignored_stages_files
        ]

        # Filtrer les stage_paths à randomiser (ceux qui ne sont pas dans la liste des ignore)
        stage_paths_randomises = [
            course["StagePath"]
            for course in all_levels
            if course["StagePath"] not in ignored_stages_files
        ]

        # Mélangez les stage_paths à randomiser
        random.shuffle(stage_paths_randomises)

        # Reconstruct the courses list with the shuffled stage_paths and the ignored stage_paths in their original order
        for course in all_levels:
            if course["StagePath"] in stage_paths_ignored:
                continue  # Ignorez les niveaux à ignorer
            course["StagePath"] = stage_paths_randomises.pop(0)

        # Répartissez les niveaux randomisés dans leurs mondes d'origine
        index = 0
        for monde_num in range(1, 10):
            monde_a_randomiser = f"World{monde_num}"
            if monde_a_randomiser in levels_dump:
                niveaux_monde = levels_dump[monde_a_randomiser]
                num_levels = len(niveaux_monde)
                levels_dump[monde_a_randomiser] = all_levels[index : index + num_levels]
                index += num_levels
        return levels_dump

    def lite(levels_dump, seed):
        ignored_stages_files = [
            "Work/Stage/StageParam/Course590_Course.game__stage__StageParam.gyml",
        ]
        print(f"Use 'Lite' Randomisation with seed: '{seed}'")
        print(f'Description of method: {world_profiles.list()[1]["description"]}')

        # random.seed(seed)
        for monde_num in range(
            1, 10
        ):  # J'ai changé la limite à 10 pour inclure le monde 9
            monde_a_randomiser = f"World{monde_num}"
            if monde_a_randomiser in levels_dump:
                niveaux_monde = levels_dump[monde_a_randomiser]

            # Extrayez les stage_paths des niveaux à ignorer
            stage_paths_ignored = [
                course["StagePath"]
                for course in niveaux_monde
                if course["StagePath"] in ignored_stages_files
            ]

            # Filtrer les stage_paths à randomiser (ceux qui ne sont pas dans la liste des ignore)
            stage_paths_randomises = [
                course["StagePath"]
                for course in niveaux_monde
                if course["StagePath"] not in ignored_stages_files
            ]

            # Mélangez les stage_paths à randomiser
            random.shuffle(stage_paths_randomises)

            # Reconstruct the courses list with the shuffled stage_paths and the ignored stage_paths in their original order
            for course in niveaux_monde:
                if course["StagePath"] in stage_paths_ignored:
                    continue  # Ignorez les niveaux à ignorer
                course["StagePath"] = stage_paths_randomises.pop(0)
            levels_dump[monde_a_randomiser] = niveaux_monde
        else:
            print(
                f"Le monde {monde_a_randomiser} n'existe pas dans votre fichier JSON et sera ignoré de la randomisation"
            )
        return levels_dump
