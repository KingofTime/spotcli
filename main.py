from spotcli import App

# spotcli config

app = App()
app.config("d7a429206d744495b506133e0bc1b92b")
app.create_listener()




#
# context = app.create_context()
# context.play()

#
# client_id = "d7a429206d744495b506133e0bc1b92b"
# client_secret = "413ba31f31f64fb1a2a6af327e74b6e4"
#
# import requests
#
# response = requests.post(
#     "https://accounts.spotify.com/api/token",
#     headers={
#         "Content-Type": "application/x-www-form-urlencoded",
#     },
#     data={
#         "grant_type": "client_credentials",
#         "client_id": client_id,
#         "client_secret": client_secret,
#     }
# )
#
# response.raise_for_status()
#
# access_token = response.json()["access_token"]
#
# print(access_token)
#
# response = requests.get(
#     "https://api.spotify.com/v1/recommendations/available-genre-seeds",
#     headers={
#         "Authorization": "Bearer " + access_token
#     }
# )
#
# response.raise_for_status()
#
# print(response.json())