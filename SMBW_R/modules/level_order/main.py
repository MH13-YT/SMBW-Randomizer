import logging
import os
import json
from SMBW_R.modules.level_order.profiles import profiles
import logging_config  # Importez la configuration de journalisation
from .functions import file_converter, data_manager

module_description = "Change all levels positions"
class level_order_module:
    def __init__(self):
        self.logger = logging.getLogger('SMBW_R Module : level_order')
        self.validate = {
            "Randomize game data": False,
        }

    def randomizing(self,method,seed):
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
        
    def start(self,method,seed,data):
        self.logger.info("Starting process")
        print("\n[level_order]: Starting process")
        self.data = data
        result = (
            self.randomizing(method,seed)
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
        print("[level_order]: End of process")
        return {"result":result, "data":self.data}
    def get_description(self):  
        return(module_description)
    def list_method(self):
        return(profiles.list())
    def get_ressources(self):
        return(file_converter.get_ressources())
    
