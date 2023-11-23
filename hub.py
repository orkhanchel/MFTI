import json
import random

class Hub:
    @classmethod
    def read_from_json(cls, json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            return cls()

    def save_as_json(self):
        data = {}
        with open("hub.json", 'w') as file:
            json.dump(data, file)
