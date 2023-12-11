from .randomizer import randomisation_functions


class profiles:
    def list():
        return [
            "all",
        ]

    def all(data_dump, seed, areaparam_data):
        ignored_files = []

        return randomisation_functions.all(data_dump, seed, areaparam_data)
