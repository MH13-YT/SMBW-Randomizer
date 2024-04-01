from .randomizer import randomisation_scripts


class profiles:

    def list():
        return [
            'full',
            ]

    def full(data_dump, seed):
        ignored_files = [
        ]

        # Randomise Data and add ignored_files if is necessary
        return randomisation_scripts.exemple(data_dump,seed)
