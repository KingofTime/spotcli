from requests_oauthlib import OAuth2Session


class AuthService:
    def __init__(self):
        self.host = "https://accounts.spotify.com"

    def login(self, client_id) -> str:
        url = f"{self.host}/authorize"
        scope = "user-read-private user-read-email"
        redirect_uri = "http://localhost:8085/callback"

        oauth = OAuth2Session(
            client_id,
            redirect_uri=redirect_uri,
            scope=scope
        )

        authorization_url, state = oauth.authorization_url(url)
        print(f"Authorization URL: {authorization_url}")
