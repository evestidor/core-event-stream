import pika


class ConnectionHandler:

    def __init__(self, host=None):
        self._parameters = pika.ConnectionParameters(host=host)
        self._connection = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = pika.BlockingConnection(self._parameters)
        return self._connection

    def __enter__(self):
        return self.connection

    def __exit__(self, *args):
        self.connection.close()
