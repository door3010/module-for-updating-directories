import json


class Handler:
    __slots__ = "_data"

    def __init__(self, filepath):
        self._load(filepath)

    @property
    def data(self):
        return self._data

    def _load(self, value: str):
        if not value:
            raise AttributeError("Filepath can't be None")
        else:
            with open(value, "r") as f:
                self._data = json.load(f)
