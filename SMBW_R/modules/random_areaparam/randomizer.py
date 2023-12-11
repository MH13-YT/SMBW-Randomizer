import json
import random

class randomisation_functions:
    def all(data_dump,seed,areaparam_data):
        random.seed(seed)
        for data in data_dump:
            if "file_data" in data and isinstance(data["file_data"], dict) and "Stage/AreaParam" in data["resource_type"]: 
                if "BgmType" in data["file_data"]:
                    data["file_data"]["BgmType"] = random.choice(areaparam_data["BgmType"])
                if "EnvironmentSound" in data["file_data"]:
                    data["file_data"]["EnvironmentSound"] = random.choice(areaparam_data["EnvironmentSound"])
                if "EnvironmentSoundEfx" in data["file_data"]:
                    data["file_data"]["EnvironmentSoundEfx"] = random.choice(areaparam_data["EnvironmentSoundEfx"])
                if "WonderBgmType" in data["file_data"]:
                    data["file_data"]["WonderBgmType"] = random.choice(areaparam_data["WonderBgmType"])
                if "EnvPaletteSetting" in data["file_data"]:
                    if "InitPaletteBaseName" in data["file_data"]["EnvPaletteSetting"]:
                        data["file_data"]["EnvPaletteSetting"]["InitPaletteBaseName"] = random.choice(areaparam_data["EnvPaletteSetting"])
                if "SkinParam" in data["file_data"]:
                    if "FieldA" in data["file_data"]["SkinParam"]:
                        data["file_data"]["SkinParam"]["FieldA"] = random.choice(areaparam_data["SkinParam"])
                    if "FieldB" in data["file_data"]["SkinParam"]:
                        data["file_data"]["SkinParam"]["FieldB"] = random.choice(areaparam_data["SkinParam"])
                    if "Object" in data["file_data"]["SkinParam"]:
                        data["file_data"]["SkinParam"]["Object"] = random.choice(areaparam_data["SkinParam"])
        return data_dump