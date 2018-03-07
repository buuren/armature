import json


class ConfigParser:
    def __init__(self, path):
        self.path_to_config = path

    def return_json(self) -> dict:
        with open(self.path_to_config) as config_file:
            return json.load(config_file)

    def return_read(self):
        with open(self.path_to_config) as config_file:
            return config_file.read()
