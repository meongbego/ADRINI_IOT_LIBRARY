from adrini.libs import channels

__version__ = "0.0.1"

class Adrini():
    def __init__(self, url, id_channels, apikey):
        self.url = url
        self.id_channels = id_channels
        self.apikey = apikey

    def get_headers(self):
        headers = {
            "apikey": self.apikey
        }
        return headers

    def get_channels(self, count):
        uri = self.url
        header = self.get_headers()
        id_channels = self.id_channels
        data = channels.get_channels_data(uri, id_channels, count, header)
        return data

    def get_channels_id(self, parameter=None, limit=None):
        if not limit:
            limit = 8
        limit = str(limit)
        uri = self.url
        header = self.get_headers()
        id_channels = self.id_channels
        data = channels.get_channels_by_id(uri, id_channels, parameter, header, limit)
        return data

    def send_channels(self, parameter=None):
        uri = self.url
        header = self.get_headers()
        id_channels = self.id_channels
        data = channels.send_data_to_channels(uri, id_channels, parameter, header)
        return data