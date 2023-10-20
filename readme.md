
# SMBW Randomizer

SMBW Randomizer is a randomizer for the Super Mario Bros Wonder game.

## Features
### Main Features
- Seed-based randomization: Share a seed for speed competitions on a randomized version of the game
- Randomization profiles: Create, share and choose different randomization methods to create different experiments.
- Automatic export to SimpleModManager format: files are exported to SimpleModManager standard for simplified installation.

### Randomized elements in the game
- Levels
More game ressources will be randomized in future versions.


## How to Install

### Prerequisites
A complete dump of the Super Mario Bros Wonder romfs file, google is your friend for obtain it

### Windows
Simply run the install.bat file to install all the files required for the software to work properly. A list of installed programs and their sources is given before installation.

### Mac OS and Linux
Install python and libyaml, after that run pip install -r requirements.txt for install dependances

## How to Run
### Run with default settings (from run.bat file)
Simply run the run.bat file, it will use a random seed and default settings (stored in config.json file)

### Run with default settings (from command line)
open a terminal in the directory of the randomizer and run "python SMBW_Randomizer.py" it will use a random seed and default settings (stored in config.json file)

### Run with custom settings
open a terminal in the directory of the randomizer and run "python SMBW_Randomizer.py -h" for obtain randomizer help document

