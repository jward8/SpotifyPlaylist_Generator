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

current_user = Spotify.current_user(spotify)
user_id = current_user.id
print(user_id)

# track_id = []
# tracks = spotify.current_user_top_tracks(limit=20)
# for track in tracks.items:
#     track_id.append(track.id)
for set in range(0,1000,20):
    library = spotify.saved_tracks(None,limit=20,offset=set).items
    track_list = []
    for track in library:
        track_item = track.track
        track_list.append(track_item)

    not_pop = []
    for track in track_list:
        if track.popularity <= 40:
            not_pop.append(track)

    for track in not_pop:
        count = 0
        artists_name = ""
        for artists in track.artists:
            n = artists.name
            if count == 0:
                artists_name = n
                count += 1
                continue
            artists_name = artists_name + " & " + n
        print(track.name + " by " + artists_name) 

# post = spotify.playback_currently_playing