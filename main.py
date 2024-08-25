import os

from dotenv import load_dotenv

from spotcli import App


load_dotenv()

app = App()
app.config(os.getenv('CLIENT_ID'))
app.create_listener()