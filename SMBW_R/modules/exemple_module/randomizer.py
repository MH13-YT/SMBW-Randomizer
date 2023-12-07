import random

class randomisation_functions:
    def exemple(data_dump,seed):
        random.seed(seed) # Configure Seed for Randomization
        print("INPUT")
        input(data_dump) # DEBUG : List Data Dump for helping to create randomizer
        for data in data_dump:
            # You must check resource_type to ensure that the data you are going to manipulate corresponds to the folder to modify 
            if "file_data" in data and isinstance(data["file_data"], dict) and "Stage/WorldMapInfo" in data["resource_type"]: 
                pass # Insert Here Code of Randomization for selected resource
        print("OUTPUT")
        input(data_dump) # DEBUG : List Data Dump for helping to create randomizer
        return data_dump