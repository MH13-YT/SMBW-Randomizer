import json
from .randomizer import randomisation_functions
from .gui import custom_badges_gui

def custom_badge_selector():
    try:
        with open('SMBW_R/modules/random_badges/config.json', 'r') as json_file:
            data = json.load(json_file)
            return [
                badge_data['id']
                for badge_name, badge_data in data.items()
                if badge_data.get('enabled', False)
            ]
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []
    
def badge_filter(type):
    try:
        with open('SMBW_R/modules/random_badges/config.json', 'r') as json_file:
            data = json.load(json_file)
            return [
                badge_data['id']
                for badge_name, badge_data in data.items()
                if badge_data.get('type', "") == type or type == 'All'
            ]
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return []
        
class profiles:

    def list():
        return [
            'all',
            'action_only',
            'bonus_only',
            'expert_only',
            'custom',
            ]

    def all(data_dump, seed):
        return randomisation_functions.badge_shuffler(data_dump,badge_filter('All'),seed)
    def action_only(data_dump, seed):
        return randomisation_functions.badge_shuffler(data_dump,badge_filter('Action'),seed)
    def bonus_only(data_dump, seed):
        return randomisation_functions.badge_shuffler(data_dump,badge_filter('Bonus'),seed)
    def expert_only(data_dump, seed):
        return randomisation_functions.badge_shuffler(data_dump,badge_filter('Expert'),seed)
    def custom(data_dump, seed):
        custom_badges_gui.custom_badge_list_configurator()
        if len(custom_badge_selector()) > 0:
            return randomisation_functions.badge_shuffler(data_dump,custom_badge_selector(),seed)

