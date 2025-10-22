import paramiko
import platform

from json_handler import Handler
from user_model import User


class Ftp:
    _shared_state = {}

    def __init__(self, credentials):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            self.handler=Handler(credentials)
            self.user=User()
            self.full_the_model()
            self.local_machine=None
            self.target_machine=None
            self.transport=None
            self.sftp_connector=None

    def full_the_model(self):
        data=self.handler.get_data()
        for key in data.keys():
            setattr(self.user,key,data[key])

    def connection_to_sftp_with_paramiko(self):
        self.transport = paramiko.Transport(self.user.hostname, self.user.port)
        self.transport.connect(username=self.user.username, password=self.user.password)
        self.sftp_connector = paramiko.SFTPClient.from_transport(self.transport)
        return self.sftp_connector

    def who_am_i(self):
        self.local_machine=platform.system()
        try:
            self.sftp_connector.listdir("/")
            self.target_machine = "Linux"
        except IOError:
            try:
                self.sftp_connector.listdir("C:\\")
                self.target_machine="Windows"
            except IOError:
                self.target_machine="Unknown"
        return self.local_machine, self.target_machine

    def proper_connection_close(self):
        self.sftp_connector.close()
        self.transport.close()
