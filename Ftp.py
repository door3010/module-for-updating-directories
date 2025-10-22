import paramiko
import platform

from json_handler import Handler
from user_model import User


class Ftp:
    _user_data = []
    _user=None
    _transport = None
    _sftp_connector = None

    def __init__(self, credentials):
        self.handler = Handler(credentials)
        self.local_machine = None
        self.target_machine = None
        self._fill_the_model()

    def _fill_the_model(self):
        data = self.handler.data
        for key in data.keys():
            self._user_data.append(data[key])
        self._user = User(*self._user_data)

    def connection_to_sftp_with_paramiko(self):
        self._transport = paramiko.Transport(self._user.hostname, self._user.port)
        self._transport.connect(username=self._user.username, password=self._user.password)
        self._sftp_connector = paramiko.SFTPClient.from_transport(self._transport)
        return self._sftp_connector

    def who_am_i(self):
        self.local_machine = platform.system()
        try:
            self._sftp_connector.listdir("/")
            self.target_machine = "Linux"
        except IOError:
            try:
                self._sftp_connector.listdir("C:\\")
                self.target_machine = "Windows"
            except IOError:
                self.target_machine = "Unknown"
        return self.local_machine, self.target_machine

    def proper_connection_close(self):
        self._sftp_connector.close()
        self._transport.close()
