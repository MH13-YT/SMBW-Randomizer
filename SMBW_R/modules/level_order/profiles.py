from .randomizer import randomisation_scripts

class profiles:

    def list():
        return [
            'full',
            'full_secured',
            'lite',
            'lite_secured',
            ]

    def full_secured(levels_dump, seed):
        ignored_stages_files = [
            "Work/Stage/StageParam/Course150_Course.game__stage__StageParam.gyml", # W1
            "Work/Stage/StageParam/Course151_Course.game__stage__StageParam.gyml", # W2
            "Work/Stage/StageParam/Course531_Course.game__stage__StageParam.gyml", # W3
            "Work/Stage/StageParam/Course152_Course.game__stage__StageParam.gyml", # W4
            "Work/Stage/StageParam/Course551_Course.game__stage__StageParam.gyml", # W5
            "Work/Stage/StageParam/Course153_Course.game__stage__StageParam.gyml", # W6
            # "Work/Stage/StageParam/Course290_Course.game__stage__StageParam.gyml", # Final Boss
        ]
        return randomisation_scripts.full(levels_dump,seed,ignored_stages_files)
    
    def full(levels_dump, seed):
        ignored_stages_files = []
        return randomisation_scripts.full(levels_dump,seed,ignored_stages_files)
    
    
    def lite_secured(levels_dump, seed):
        ignored_stages_files = [
            "Work/Stage/StageParam/Course150_Course.game__stage__StageParam.gyml", # W1
            "Work/Stage/StageParam/Course151_Course.game__stage__StageParam.gyml", # W2
            "Work/Stage/StageParam/Course531_Course.game__stage__StageParam.gyml", # W3
            "Work/Stage/StageParam/Course152_Course.game__stage__StageParam.gyml", # W4
            "Work/Stage/StageParam/Course551_Course.game__stage__StageParam.gyml", # W5
            "Work/Stage/StageParam/Course153_Course.game__stage__StageParam.gyml", # W6
            # "Work/Stage/StageParam/Course290_Course.game__stage__StageParam.gyml", # Final Boss

        ]
        return randomisation_scripts.lite(levels_dump,seed,ignored_stages_files)
    
    def lite(levels_dump, seed):
        ignored_stages_files = []
        return randomisation_scripts.lite(levels_dump,seed,ignored_stages_files)

        
