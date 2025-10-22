class User:
    __slots__ = ("_hostname", "_username", "_password", "_port")

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def __repr__(self):
        return f"User: hostname={self.hostname}, username={self.username}," \
               f"password = {self.password},port={self.port}"

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value: str):
        if not value:
            raise AttributeError("Hostname can't be None")
        else:
            self._hostname = value

    @property
    def username(self):
        return self._hostname

    @username.setter
    def username(self, value: str):
        if not value:
            raise AttributeError("Username can't be None")
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        if not value:
            raise AttributeError("Password can't be None")
        else:
            self._password = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value: int):
        if not value:
            raise AttributeError("Port can't be None")
        else:
            self._port = value
