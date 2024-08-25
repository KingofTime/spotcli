
import os

from dotenv import load_dotenv

from spotcli.http.Listener import Listener as HTTPListener
from spotcli.services.AuthService import AuthService


load_dotenv()

class App:
    listener: HTTPListener

    def __init__(self):
        self.auth_service = AuthService()
        self._create_setting_path()

    def _create_setting_path(self):
        setting_path = os.getenv("SETTINGS_PATH")
        if not os.path.exists(setting_path):
            os.mkdir(setting_path)

    def create_listener(self):
        self.listener = HTTPListener(port=8085)
        self.listener.run()

    def config(self, client_id: str):
        self.auth_service.login(client_id)