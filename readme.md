
# SMBW Randomizer

SMBW Randomizer is a randomizer for the Super Mario Bros Wonder game.

## Features
### Main Features
- Seed-based randomization: Share a seed for speed competitions on a randomized version of the game
- Module Based Randomization : Developpers / Modders can create modules for randomizing more features on the game (use exemple_module as base), feel free to create pull requests for share modules
- Profiles : Every Modules has their own profiles, feel free to create pull requests for improve profiles
- Automatic packaging for Famous Mod Managers: Files are exported to Yuzu, Ryujinx and Simple Mod Manager file structure for simplify installation

### Current Randomization Modules (Things randomized on the game)
- Levels Order : Randomize Every Levels position
- Random Badges : Set a random badge at the start of a level
- Random Wonder : Randomize Wonder Effect (Morph and Player Effects)

More game resources will be randomized in future versions.


## How to Install

### Prerequisites
A complete dump of the Super Mario Bros Wonder romfs file, google is your friend for obtain it

### Windows
Simply run the install.bat file to install all the files required for the software to work properly. A list of installed programs and their sources is given before installation.

### Mac OS and Linux
Install python and libyaml, after that run pip install -r requirements.txt for install dependances

## How to Run
### Run with default settings (from run.bat file)
Simply run the run.bat file, it will use a random seed and default settings (stored in config.json file), if this file isn't present or invalid the configuration UI will open automatically

### Run with default settings (from command line)
Open a terminal in the directory of the randomizer and run "python SMBW_Randomizer.py" it will use a random seed and default settings (stored in config.json file), if this file isn't present or invalid the configuration UI will open automatically

## How to Configure
### From Configuration GUI
Open a terminal in the directory of the randomizer and run "python SMBW_Randomizer.py --configure" for open configuration GUI
### From Configuration CLI
Open a terminal in the directory of the randomizer and run "python SMBW_Randomizer.py -h" for open help

## How to develop modules
- Copy and rename exemple_module with your module name (the module name DOES not have spaces)
- In every files of the module rename 'exemple' to your module name
- Develop every steps and write an description

