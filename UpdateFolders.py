import os
from SftpWithParamiko import SftpWithParamiko
from JsonToDict import JsonToDict
from PathManager import PathManager


class UpdateFolders:

    def __init__(self, credentials):
        self.sftp_connection = SftpWithParamiko(credentials)
        self.sftp = self.sftp_connection.connection()

    def update(self, local_path_to_target_path_file):
        path_dict = JsonToDict(local_path_to_target_path_file)
        from_to_paths = path_dict.data.items()
        for pure_local_path, pure_target_path in from_to_paths:
            self.recursive_folder_update(pure_local_path, pure_target_path)

    def recursive_folder_update(self, pure_local_path, pure_target_path):
        path_manager=PathManager()
        files = os.listdir(pure_local_path)
        for file in files:
            local_path_with_file = path_manager.local_path_file(pure_local_path, file)
            target_path_with_file = path_manager.target_path_file(pure_target_path,
                                                                  file, self.sftp_connection.user.target_os)
            if not os.path.isfile(local_path_with_file):
                try:
                    self.sftp.chdir(target_path_with_file)
                    self.recursive_folder_update(local_path_with_file, target_path_with_file)
                except IOError:
                    self.sftp.mkdir(target_path_with_file)
                    self.sftp.chdir(target_path_with_file)
                    self.recursive_folder_update(local_path_with_file, target_path_with_file)
            else:
                self.sftp.put(local_path_with_file, target_path_with_file)

    def connection_close(self):
        self.sftp_connection.proper_connection_close()
