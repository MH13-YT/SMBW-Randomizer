import json
import random

class randomisation_functions:
    def all(data_dump,seed,areaparam_data, security):
        random.seed(seed)
        data_config = {}
        try:
            with open( "SMBW_R/modules/random_areaparam/data_config.json", 'r') as data_config_file:
                data_config = json.load(data_config_file)
        except:
            pass
        for data in data_dump:
            if "file_data" in data and isinstance(data["file_data"], dict) and "Stage/AreaParam" in data["resource_type"]: 
                if data['file_name'] not in data_config:
                    data_config[data['file_name']] = {"BgmType":True,"EnvironmentSound":True,"EnvironmentSoundEfx":True,"WonderBgmType":True,"EnvPaletteSetting":True,"FieldA":True,"FieldB":True,"Object":True}
                if "BgmType" in data["file_data"] and data["file_data"]["BgmType"] in areaparam_data["BgmType"]:
                    if data_config[data['file_name']]["BgmType"] or security == False:
                        data["file_data"]["BgmType"] = random.choice(areaparam_data["BgmType"])
                if "EnvironmentSound" in data["file_data"] and data["file_data"]["EnvironmentSound"] in areaparam_data["EnvironmentSound"]:
                    if data_config[data['file_name']]["EnvironmentSound"] or security == False:
                        data["file_data"]["EnvironmentSound"] = random.choice(areaparam_data["EnvironmentSound"])
                if "EnvironmentSoundEfx" in data["file_data"] and data["file_data"]["EnvironmentSoundEfx"] in areaparam_data["EnvironmentSoundEfx"]:
                    if data_config[data['file_name']]["WonderBgmType"] or security == False:
                        data["file_data"]["EnvironmentSoundEfx"] = random.choice(areaparam_data["EnvironmentSoundEfx"])
                if "WonderBgmType" in data["file_data"] and data["file_data"]["WonderBgmType"] in areaparam_data["WonderBgmType"]:
                    if data_config[data['file_name']]["WonderBgmType"] or security == False:
                        data["file_data"]["WonderBgmType"] = random.choice(areaparam_data["WonderBgmType"])
                if "EnvPaletteSetting" in data["file_data"] and data_config[data['file_name']]:
                    if data_config[data['file_name']]["EnvPaletteSetting"] or security == False:
                        if "InitPaletteBaseName" in data["file_data"]["EnvPaletteSetting"] and data["file_data"]["EnvPaletteSetting"]["InitPaletteBaseName"] in areaparam_data["EnvPaletteSetting"]:
                            data["file_data"]["EnvPaletteSetting"]["InitPaletteBaseName"] = random.choice(areaparam_data["EnvPaletteSetting"])
                if "SkinParam" in data["file_data"]:
                    if "FieldA" in data["file_data"]["SkinParam"] and data["file_data"]["SkinParam"]["FieldA"] in areaparam_data["SkinParam"]:
                        if data_config[data['file_name']]["FieldA"] or security == False:
                            data["file_data"]["SkinParam"]["FieldA"] = random.choice(areaparam_data["SkinParam"])
                    if "FieldB" in data["file_data"]["SkinParam"] and data["file_data"]["SkinParam"]["FieldB"] in areaparam_data["SkinParam"]:
                        if data_config[data['file_name']]["FieldB"] or security == False:
                            data["file_data"]["SkinParam"]["FieldB"] = random.choice(areaparam_data["SkinParam"])
                    if "Object" in data["file_data"]["SkinParam"] and data["file_data"]["SkinParam"]["Object"] in areaparam_data["SkinParam"]:
                        if data_config[data['file_name']]["Object"] or security == False:
                            data["file_data"]["SkinParam"]["Object"] = random.choice(areaparam_data["SkinParam"])
        with open("SMBW_R/modules/random_areaparam/data_config.json", 'w') as data_config_file:
                json.dump(data_config, data_config_file, indent=4, sort_keys=True)
        return data_dump