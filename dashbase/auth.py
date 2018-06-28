import requests


class AuthClient(object):
    def __init__(self, host: str):
        self.headers = {'Accept': 'application/json'}
        self.host = host

    def get_token(self, user, password):
        path = "/basic"

        res = requests.post("{}{}".format(self.host, path), auth=(user, password))
        try:
            res.raise_for_status()
        except requests.HTTPError:
            return ""

        return res.content
