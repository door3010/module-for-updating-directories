"""Copy folders from the local machine to a remote machine over SFTP."""

import json
import os
import posixpath

import paramiko


def load_json(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


class UpdateFolders:
    """Upload local directories to a remote host, keeping their layout."""

    def __init__(self, credentials):
        credentials = load_json(credentials)
        self._transport = paramiko.Transport((credentials["hostname"], credentials["port"]))
        self._transport.connect(
            username=credentials["username"],
            password=credentials["password"],
        )
        self.sftp = paramiko.SFTPClient.from_transport(self._transport)

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()

    def update(self, local_path_to_target_path_file):
        for local_path, target_path in load_json(local_path_to_target_path_file).items():
            self._sync(local_path, target_path)

    def _sync(self, local_root, target_root):
        if not os.path.isdir(local_root):
            raise FileNotFoundError(local_root)
        for directory, _subdirectories, files in os.walk(local_root):
            relative = os.path.relpath(directory, local_root)
            target_dir = target_root if relative == "." else posixpath.join(
                target_root, *relative.split(os.sep)
            )
            self._make_directories(target_dir)
            for name in files:
                self.sftp.put(
                    os.path.join(directory, name),
                    posixpath.join(target_dir, name),
                )

    def _make_directories(self, target_dir):
        current = "/" if target_dir.startswith("/") else ""
        for part in filter(None, target_dir.split("/")):
            current = posixpath.join(current, part)
            try:
                self.sftp.stat(current)
            except OSError:
                self.sftp.mkdir(current)

    def close(self):
        self.sftp.close()
        self._transport.close()

    connection_close = close
