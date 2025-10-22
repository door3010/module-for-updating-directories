import json


class JsonToDict:
    __slots__ = "_data"

    def __init__(self, filepath):
        if not filepath:
            raise AttributeError("Filepath can't be None")
        else:
            with open(filepath, "r") as f:
                self._data = json.load(f)

    @property
    def data(self):
        return self._data
