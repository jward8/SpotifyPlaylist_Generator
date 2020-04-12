from tekore.util import request_client_token
from tekore import Spotify
from tekore.scope import every
from tekore.util import prompt_for_user_token

client_id = 'd217fc4b5c4540d0bf2299a6c5a09c9a'
client_secret = '504db230bc054da896f2c442e1a1f890'
redirect_uri = 'https://google.com/'

user_token = prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=every
)

app_token = request_client_token(client_id,client_secret)

spotify = Spotify(app_token)
spotify.token = user_token

tracks = spotify.current_user_top_tracks(limit=20)
for track in tracks.items:
    print(track.name)