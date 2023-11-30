import logging
import os
import json
from SMBW_R.modules.exemple_module.profiles import profiles
import logging_config  # Importez la configuration de journalisation
from .functions import data_manager, file_converter

module_description = "Exemple Module (DO NOT USE FOR RANDOMIZING)"
class exemple_module:
    def __init__(self):
        self.logger = logging.getLogger('SMBW_R Module : exemple_module')
        self.validate = {
            "Randomize game data": False,
        }

    def randomizing(self,method,seed): #DO NOT EDIT, These script are preconfigured
        self.logger.info("STEP 4: Randomize game data")
        game_is_randomized = True
        try:
            self.logger.info("Starting data randomisation")
            self.data = data_manager.shuffle(self.data,method,seed),
            self.logger.info("Randomisation Complete")
        except Exception as error:
            self.logger.error(f"Error occured on file randomizing: {error}")
            print(f"Error occured on file randomizing: {error}")
            game_is_randomized = False
        self.validate["Randomize game data"] = game_is_randomized
        self.logger.info("")
        return game_is_randomized

    def start(self,method,seed,data): #DO NOT EDIT, These script are preconfigured
        self.logger.info("Starting process")
        print("\n[exemple_module]: Starting process")
        self.data = data
        result = (
            self.randomizing(method,seed)
        )
        data = self.data
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
        print("[exemple_module]: End of process")
        return {"result":result, "data":data}
    def get_description(self):  
        return(module_description)
    def list_method(self):
        return(profiles.list())
    
