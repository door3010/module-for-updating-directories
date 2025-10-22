import os
from SftpWithParamiko import SftpWithParamiko
from JsonToDict import JsonToDict


class UpdateFolders:

    def __init__(self, credentials):
        self.slashes = {"Windows": "\\", "Linux": "/"}
        self.localpath = None
        self.targetpath = None
        self.path_dict = None

        self.sftp_connection = SftpWithParamiko(credentials)
        self.sftp = self.sftp_connection.connection()
        self.local_slash, self.target_slash = self.sftp_connection.identify_os()

    def update(self, localpath_to_targetpath_file):
        self.path_dict = JsonToDict(localpath_to_targetpath_file)
        from_to_pathes = self.path_dict.data.items()
        for key, value in from_to_pathes:
            self.localpath = key
            self.targetpath = value
            self.recursive_folder_update(self.localpath, self.targetpath)

    def recursive_folder_update(self, localpath, targetpath):
        files = os.listdir(localpath)
        for file in files:
            localpath_file = localpath + self.slashes[self.local_slash] + file
            targetpath_file = targetpath + self.slashes[self.target_slash] + file
            if not os.path.isfile(localpath_file):
                try:
                    self.sftp.chdir(targetpath_file)
                    self.recursive_folder_update(localpath_file, targetpath_file)
                except IOError:
                    self.sftp.mkdir(targetpath_file)
                    self.sftp.chdir(targetpath_file)
                    self.recursive_folder_update(localpath_file, targetpath_file)
            else:
                self.sftp.put(localpath_file, targetpath_file)

    def connection_close(self):
        self.sftp_connection.proper_connection_close()
