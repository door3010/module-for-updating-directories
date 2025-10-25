import os
from JsonToDict import JsonToDict


class PathManager:

    def __init__(self):
        self.slashes = {"Windows": "\\", "Linux": "/"}

    def local_path_file(self, local_path, file):
        return os.path.join(local_path, file)

    def target_path_file(self, local_path, file, target_operating_system):
        return local_path+self.slashes[target_operating_system]+file
