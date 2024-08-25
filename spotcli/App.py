import requests

from spotcli.http.Listener import Listener as HTTPListener
from spotcli.services.AuthService import AuthService


class App:
    listener: HTTPListener

    def __init__(self):
        self.auth_service = AuthService()

    def create_listener(self):
        self.listener = HTTPListener(port=8085)
        self.listener.run()

    def config(self, client_id: str):
        self.auth_service.login(client_id)