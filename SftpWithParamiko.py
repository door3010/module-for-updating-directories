import paramiko
import platform

from JsonToDict import JsonToDict
from user_model import User


class SftpWithParamiko:
    def __init__(self, credentials):
        self.credentials_dict = JsonToDict(credentials)
        self.user = User(**self.credentials_dict.data)

        self.transport = paramiko.Transport(self.user.hostname, self.user.port)
        self.transport.connect(username=self.user.username, password=self.user.password)
        self.sftp_client = paramiko.SFTPClient.from_transport(self.transport)

    def connection(self):
        return self.sftp_client

    def proper_connection_close(self):
        self.sftp_client.close()
        self.transport.close()
