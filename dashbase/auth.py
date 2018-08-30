import requests
import click
import logging
from dashbase import utils


class AuthClient(object):
    def __init__(self, host: str):
        self.headers = {'Accept': 'application/json'}
        self.host = self.auto_add_schema(host)

    def get_token(self, user, password) -> bytes:
        path = "/basic"

        res = requests.post("{}{}".format(self.host, path), auth=(user, password))
        try:
            res.raise_for_status()
        except requests.HTTPError:
            return b""

        return res.content

    def get_auth_support_mode(self):
        req = requests.get(self.host)
        if "saml" in req.text:
            return ["saml"]
        elif "loginRest" in req.text:
            return ["rest"]
        elif "ldap" in req.text:
            return ["ldap"]
        return []

    def auto_add_schema(self, url):
        if requests.utils.urlparse(url).scheme:
            return url

        return requests.utils.urlparse("//" + url, scheme="https").geturl()

    @staticmethod
    def get_dashbase_token_in_local(api_host, ignore_input: bool = False, auth_host=None) -> str:
        path = utils.get_setting_path().joinpath("dashbase.token")

        if not path.exists() and not ignore_input:
            y = click.confirm("Can't found token in local, do you want input your dashbase account to get token",
                              default=True)
            if not y:
                return ""
            if not auth_host:
                _api_host = requests.utils.urlparse(api_host, scheme="https")
                if not _api_host.netloc:
                    _api_host = requests.utils.urlparse("//" + api_host, scheme="https")
                default_auth_host = _api_host._replace(netloc="{}:{}".format(_api_host.hostname, "9678")).geturl()
                auth_host = click.prompt("please input your dashbase auth host", default=default_auth_host)

            click.echo("\nnow use auth_host: {}\n".format(click.style(auth_host, fg="green")))
            auth_client = AuthClient(auth_host)
            click.echo("checking dashbase_auth mode", nl=False)
            mode = auth_client.get_auth_support_mode()
            if len(mode) == 0:
                click.echo("\rCan't get dashbase_auth mode, plz check your input auth host")
                return ""

            if "rest" not in mode:
                click.echo("\rYour dashbase_auth mode is:{}".format(mode))
                click.echo("Can't auto get your dashbase auth token information, please enter token manually.")
                return ""

            while y:
                user = click.prompt("your dashbase account")
                password = click.prompt("your dashbase password", hide_input=True)

                token = auth_client.get_token(user, password)
                if not token:
                    click.secho("get token failed, please check your account info\n", fg="yellow")
                    continue

                with path.open("wb") as f:
                    f.write(token)
                click.secho("get token success, saved token to:{}".format(path), fg="green")
                break

        if path.exists():
            logging.debug("use local token, path:{}".format(path))
            return path.open().readline()

        logging.debug("not use local token".format(path))
        return ""


if __name__ == '__main__':
    AuthClient("https://staging.dashbase.io").get_dashbase_token_in_local("https://staging.dashbase.io:9876")
