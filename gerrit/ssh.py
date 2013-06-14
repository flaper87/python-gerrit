import paramiko


class Client(object):

    def __init__(self, host, port=29418, user=None, key=None):
        self.host = host
        self.port = port
        self.user = user
        self.key = key

    @property
    def client(self):
        if not hasattr(self, "_client"):
            self._client = paramiko.SSHClient()
            self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._client.load_system_host_keys()
            self._client.connect(self.host,
                                 port=self.port,
                                 username=self.user,
                                 key_filename=self.key)
        return self._client
