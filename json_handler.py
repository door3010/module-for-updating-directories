import json


class Handler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = {}
        self.load()

    def load(self):
        with open(self.filepath, "r") as f:
            self.data = json.load(f)

    def get_data(self):
        return self.data
