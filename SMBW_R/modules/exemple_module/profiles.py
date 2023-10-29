import random


class profiles:

    def list():
        return [
            'full',
            ]

    def full(levels_dump, seed):
        ignored_files = [
        ]

        random.seed(seed)
        # Randomise Data and add ignored_files if is necessary
        return levels_dump
