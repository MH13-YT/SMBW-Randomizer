import logging
import os
import json
from SMBW_R.modules.random_badges.profiles import profiles
import logging_config  # Importez la configuration de journalisation
from .functions import data_manager, file_converter

module_description = "Choose a random badge at Level Start (You can change it but is cheating)"
class random_badges_module:
    def __init__(self):
        self.logger = logging.getLogger('SMBW_R Module : random_badges')
        self.path_list = [
            "SMBW_R/modules/random_badges/worktable/",
            "SMBW_R/modules/random_badges/output/romfs/Stage/CourseInfo"
        ]
        self.validate = {
            "Check files and folders": False,
            "Decompile and copy necessary games files": False,
            "Read game data from game files": False,
            "Randomize game data": False,
            "Generating patched game files": False,
            "Game files recompilation": False,
            "Cleaning Worktable folder":False
        }

        self.data = {}

    def check_files(self):
        self.logger.info("STEP 1 : Check Required Files and folder")
        files_is_created = True
        for folder in self.path_list:
            if not os.path.exists(f"{os.curdir}/{folder}"):
                self.logger.info(f"Required Folder '{os.curdir}/{folder}' isn't exist, trying to create it")
                try:
                    os.makedirs(f"{os.curdir}/{folder}", exist_ok=True)
                    self.logger.info(f"Required Folder '{os.curdir}/{folder}' created successfuly")
                except Exception as error:
                    self.logger.error(f"Cannot create necessary folders {os.curdir}/{folder}: {error}")
                    print(f"Cannot create necessary folders {os.curdir}/{folder}:")
                    input(f"{error}")
                    files_is_created = False
        if not file_converter.verify_files():
            self.logger.error(f"Unable to find 'Super Mario Bros Wonder' romfs files")
            input("Unable to find 'Super Mario Bros Wonder' romfs files"
                  "please place a valid romfs dump of 'Super Mario Bros Wonder' in the same location as the executable.")
            files_is_created = False
        self.logger.info(f"Required Files and folder are verified")
        self.validate["Check files and folders"] = files_is_created
        self.logger.info("")
        return files_is_created

    def decompilation(self):
        self.logger.info("STEP 2 : Decompile and copy necessary games files")
        decompilation_is_work = True
        try:
            self.logger.info("Starting World Files Decompilation")
            file_converter.decompile()
            self.logger.info("World Files Decompilation is Finished")
        except Exception as error:
            self.logger.error(f"Cannot Decompile World Files: {error}")
            print(f"Cannot Decompile World Files: {error}")
            decompilation_is_work = False

        self.validate["Decompile and copy necessary games files"] = decompilation_is_work
        self.logger.info("")
        return decompilation_is_work

    def get_data(self):
        self.logger.info("STEP 3: Read game data from game files")
        data_is_get = True
        self.logger.info("Get data from decompiled files")
        try:
            self.data = data_manager.dump()
        except Exception as error:
            self.logger.error(f"Data cannot be dumped: {error}")
            print(f"Data cannot be dumped: {error}")
            data_is_get = False
        self.validate["Read game data from game files"] = data_is_get
        self.logger.info("")
        return data_is_get

    def randomizing(self,method,seed):
        self.logger.info("STEP 4: Randomize game data")
        game_is_randomized = True
        try:
            self.logger.info("Starting data randomization")
            with open("SMBW_R/modules/random_badges/worktable/random_data.json", "w") as file:
                self.logger.info("Creating Random Data JSON File")
                json.dump(
                    data_manager.shuffle(self.data,method,seed),
                    file,
                    indent=4
                )
                self.logger.info("Data Randomisation Complete")
        except Exception as error:
            self.logger.error(f"Error occured on file randomizing: {error}")
            print(f"Error occured on file randomizing: {error}")
            game_is_randomized = False
        self.validate["Randomize game data"] = game_is_randomized
        self.logger.info("")
        return game_is_randomized
        
    def patching(self):
        self.logger.info("STEP 5: Generating patched game files")
        game_is_patched = True
        try:
            with open("SMBW_R/modules/random_badges/worktable/random_data.json", "r") as random_data_file:
                data = json.load(random_data_file)
                self.logger.info("Starting Patched data Restoration to YML")
                data_manager.restore(data)
                self.logger.info("Patched data are restored to YML")

        except Exception as error:
            self.logger.error(f"Cannot patch files: {error}")
            print(f"Cannot patch files: {error}")
            game_is_patched = False

        self.validate["Generating patched game files"] = game_is_patched
        self.logger.info("")
        return game_is_patched
    
    def recompilation(self):
        self.logger.info("STEP 6: Game files recompilation")
        patched_game_files_are_compiled = True
        try:
            self.logger.info(f"Starting Patched Files Compilation")
            file_converter.compile()
            self.logger.info(f"Patched Files Compilation is Finished")
        except Exception as error:
            self.logger.error(f"Cannot compile patched files: {error}")
            print(f"Cannot compile patched files: {error}")
            patched_game_files_are_compiled = False
        self.validate["Game files recompilation"] = patched_game_files_are_compiled
        self.logger.info("")
        return patched_game_files_are_compiled
    
    def cleaning(self):
        self.logger.info("STEP 7: Cleaning Worktable")
        worktable_is_cleaned = True
        try:
            self.logger.info(f"Starting Worktable Cleaning")
            file_converter.clean()
            self.logger.info(f"Worktable Has Been Cleaned with success")
        except Exception as error:
            self.logger.error(f"Cannot clean worktable: {error}")
            print(f"Cannot clean worktable: {error}")
            worktable_is_cleaned = False
        self.validate["Cleaning Worktable folder"] = worktable_is_cleaned
        self.logger.info("")
        return worktable_is_cleaned

    def start(self,method,seed):
        self.logger.info("Starting process")
        print("\n[random_badges]: Starting process")
        result = (
            self.check_files() and
            self.decompilation() and
            self.get_data() and
            self.randomizing(method,seed) and
            self.patching() and
            self.recompilation() and
            self.cleaning()
        )
        self.logger.info("Summary of module process:")
        print("Summary of module process:")
        for key, value in enumerate(self.validate):
            if self.validate[value]:
                self.logger.info(f"Step {key + 1}: {value} => SUCCESS")
                print(f"Step {key + 1}: {value} => SUCCESS")
            else:
                self.logger.warn(f"Step {key + 1}: {value} => FAIL")
                print(f"Step {key + 1}: {value} => FAIL")
        self.logger.info("End of process")
        print("[random_badges]: End of process")
        return result
    def get_description(self):  
        return(module_description)
    def list_method(self):
        return(profiles.list())
    def get_used_files(self):
        return(file_converter.get_used_files())
    def get_output_files(self):
        return(file_converter.get_output_files())
    
