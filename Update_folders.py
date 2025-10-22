import os
from ftp_connector import Ftp
from json_handler import Handler


class UpdateFolders:
    __slashes={"Windows":"\\", "Linux":"/"}
    localpath = None
    targetpath = None

    def __init__(self, credentials):
        self.sftp_connection = Ftp(credentials)
        self.sftp = self.sftp_connection.connection_to_sftp_with_paramiko()

        self.path_handler = None
        self.local_slash,self.target_slash=self.sftp_connection.who_am_i()

    def update(self, localpath_to_targetpath_file):
        self.path_handler=Handler(localpath_to_targetpath_file)
        from_to_pathes=self.path_handler.get_data().items()
        for key, value in from_to_pathes:
            self.localpath = key
            self.targetpath = value
            self._recursive_folder_update(self.localpath, self.targetpath)

    def _recursive_folder_update(self, localpath, targetpath):
        files = os.listdir(localpath)
        for file in files:
            localpath_file = localpath + self.__slashes[self.local_slash] + file
            targetpath_file = targetpath + self.__slashes[self.target_slash] + file
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
        print('Upload done.')

    def connection_close(self):
        self.sftp_connection.proper_connection_close()
