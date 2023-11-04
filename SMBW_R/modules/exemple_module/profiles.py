from .randomizer import randomisation_functions


class profiles:

    def list():
        return [
            'full',
            ]

    def full(levels_dump, seed):
        ignored_files = [
        ]

        # Randomise Data and add ignored_files if is necessary
        return randomisation_functions.exemple(levels_dump,seed)
