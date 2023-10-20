import os
import argparse
import json
import sys
from wonder import file_converter, levels_manager
from randomizer import world_profiles



config_file_path = 'config.json'
config_world_method = ""
try:
    with open(config_file_path, 'r') as config_file:
        world_config_data = json.load(config_file)["randomizer_default_method"]
        config_world_method = world_config_data.get('world_method')
except Exception as error:
    print(f"Unable to read '{config_file_path}' : {error}")

class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _split_lines(self, text, width):
        return text.splitlines()
    
class Randomise:
    def __init__(self):
        self.path_list = [
            "worktable",
            "output/SMM/mods/Super Mario Bros Wonder/Randomized/contents/010015100B514000/romfs/Stage/WorldMapInfo",
            "output/ROMFS/romfs/Stage/WorldMapInfo",
            "output/YUZU/load/010015100B514000/Randomized/romfs/Stage/WorldMapInfo",
            "output/RYUJINX/mods/contents/010015100B514000/Randomized/romfs/Stage/WorldMapInfo",
        ]
        self.validate = {
            "Check files and folders": False,
            "Decompile and copy necessary games files": False,
            "Read game data from game files": False,
            "Randomize game data": False,
            "Generating patched game files": False,
            "Game files recompilation and packaging as a mod": False,
            "Cleaning Worktable folder":False
        }

        self.levels = {}

    def check_files(self):
        print("")
        print("STEP 1: Check files and folders")
        files_is_created = True
        print("Verify folders required to run the application")
        for folder in self.path_list:
            if not os.path.exists(f"{os.curdir}/{folder}"):
                print(f"{os.curdir}/{folder} isn't exist, trying to create it")
                try:
                    os.makedirs(f"{os.curdir}/{folder}", exist_ok=True)
                    print(f"{os.curdir}/{folder} is created")
                except Exception as error:
                    print(f"Cannot create necessary folders {os.curdir}/{folder}:")
                    input(f"{error}")
                    files_is_created = False
            else:
                print(f"{os.curdir}/{folder} folder : OK")
        print("Verify 'Super Mario Bros Wonder' romfs files")
        if not file_converter.verify_files():
            input("Unable to find 'Super Mario Bros Wonder' romfs files"
                  "please place a valid romfs dump of 'Super Mario Bros Wonder' in the same location as the executable.")
            files_is_created = False
        
        self.validate["Check files and folders"] = files_is_created
        return files_is_created

    def decompilation(self):
        print("")
        print("STEP 2: Decompile and copy necessary games files")
        decompilation_is_work = True
        try:
            print(f"Starting World Files Decompilation")
            file_converter.decompile()

            print(f"World Files Decompilation is Finished")

        except Exception as error:
            print(f"Cannot Decompile World Files: {error}")
            decompilation_is_work = False

        self.validate["Decompile and copy necessary games files"] = decompilation_is_work
        return decompilation_is_work

    def get_levels(self):
        print("")
        print("STEP 3: Read game data from game files")
        levels_is_get = True
        print("Get levels data from decompiled files")

        try:
            if not os.path.exists("worktable/levels.json"):
                with open("worktable/levels.json", "w") as levels_file:
                    print("Starting game level dump from YML")
                    self.levels = levels_manager.dump()
                    json.dump(self.levels, levels_file, indent=4)

            else:
                with open("worktable/levels.json", "r") as levels_file:
                    print("Loading levels dump from levels.json file")
                    self.levels = json.load(levels_file)

        except Exception as error:
            print(f"Levels dump is corrupted or levels data cannot be dumped: {error}")
            levels_is_get = False

        self.validate["Read game data from game files"] = levels_is_get
        return levels_is_get

    def randomizing(self, args):
        print("")
        print("STEP 4: Randomize game data")
        game_is_randomized = True

        try:
            print("Starting randomisation of Levels")

            with open("worktable/random_levels.json", "w") as file:
                print("Creating Random Levels JSON File")
                json.dump(
                    levels_manager.shuffle(self.levels, args.world_method, args.seed),
                    file,
                    indent=4
                )
                print("Randomisation of Levels Complete")

                

        except Exception as error:
            print(f"Error occured on file randomizing: {error}")
            game_is_randomized = False
        self.validate["Randomize game data"] = game_is_randomized
        return game_is_randomized
        
    def patching(self):
        print("")
        print("STEP 5: Generating patched game files")
        game_is_patched = True
        try:
            with open("worktable/random_levels.json", "r") as random_levels_file:
                data = json.load(random_levels_file)
                print("Starting Patched Level Restoration to YML")
                levels_manager.restore(data)
                print("Patched Levels are Restored to YML")

        except Exception as error:
            print(f"Cannot patch files: {error}")
            game_is_patched = False

        self.validate["Generating patched game files"] = game_is_patched
        return game_is_patched
    
    def recompilation(self):
        print("")
        print("STEP 6: Game files recompilation and packaging as a mod")
        patched_game_files_are_compiled = True
        try:
            print(f"Starting Patched World Files Compilation")
            file_converter.compile()
            print(f"Patched World Files Compilation is Finished")
            print("")
        except Exception as error:
            print(f"Cannot compile patched files: {error}")
            patched_game_files_are_compiled = False
        self.validate["Game files recompilation and packaging as a mod"] = patched_game_files_are_compiled
        return patched_game_files_are_compiled
    
    def cleaning(self):
        print("")
        print("STEP 7: Cleaning Worktable")
        worktable_is_cleaned = True
        try:
            print(f"Starting Worktable Cleaning")
            file_converter.clean()
            print(f"Worktable Has Been Cleaned with success")
        except Exception as error:
            print(f"Cannot compile patched files: {error}")
            worktable_is_cleaned = False
        self.validate["Cleaning Worktable folder"] = worktable_is_cleaned
        return worktable_is_cleaned
    
    print("Randomisation Complete, Randomized Files are on 'output' folder")
    print("Randomized files are packaged for multiples platforms (Simple Mod Manager, Atmosphere RomFS, Yuzu and Ryujinx)")

    def main(self,args):
        (
            self.check_files() and
            self.decompilation() and
            self.get_levels() and
            self.randomizing(args) and
            self.patching() and
            self.recompilation() and
            self.cleaning()
        )

        print("\nSummary of randomization process:")
        for key, value in enumerate(self.validate):
            if self.validate[value]:
                print(f"Step {key + 1}: {value} => SUCCESS")
            else: 
                print(f"Step {key + 1}: {value} => FAIL")

parser = argparse.ArgumentParser(description='A randomizer for Super Mario Bros Wonder Game', formatter_class=CustomHelpFormatter)

# Ajout de l'argument optionnel pour la méthode "world"
world_method_choices = [profile["method"] for profile in world_profiles.list()]
world_method_choices_str = ', '.join(world_method_choices)
parser.add_argument('-w_m', type=str, dest='world_method',metavar='world_method', choices=world_method_choices, help=f"define 'world' method to use. [{world_method_choices_str}]")
parser.add_argument('-s', type=str, dest='seed', metavar='seed', help="define a seed for randomization")

args = parser.parse_args()
if args.world_method is None:
    args.world_method = config_world_method

randomise = Randomise()
randomise.main(args)
