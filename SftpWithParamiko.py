import paramiko
import platform

from JsonToDict import JsonToDict
from user_model import User


class SftpWithParamiko:
    def __init__(self, credentials):
        self.user_data = []
        self.sftp_connector = None

        self.credentials_dict = JsonToDict(credentials)
        self.user = User(**self.credentials_dict.data)
        self.transport = paramiko.Transport(self.user.hostname, self.user.port)
        self.transport.connect(username=self.user.username, password=self.user.password)

    def connection(self):
        self.sftp_connector = paramiko.SFTPClient.from_transport(self.transport)
        return self.sftp_connector

    def identify_os(self):
        return "Windows", "Linux"

    def proper_connection_close(self):
        self.sftp_connector.close()
        self.transport.close()

