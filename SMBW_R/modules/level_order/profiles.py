from .randomizer import randomisation_scripts


class profiles:
    def list():
        return [
            "full",
            "full_secured",
            "lite",
            "lite_secured",
        ]

    def full(data, seed, security):
        ignored_stages_files = []
        return randomisation_scripts.full(data, seed, security)

    def lite(data, seed, security):
        ignored_stages_files = []
        return randomisation_scripts.lite(data, seed, security)
