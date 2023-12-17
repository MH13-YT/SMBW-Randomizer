from .randomizer import randomisation_functions


class profiles:
    def list():
        return [
            "all",
            "all_secured",
        ]

    def all(data_dump, seed, areaparam_data,security):
        return randomisation_functions.all(data_dump, seed, areaparam_data, security)
