from tekore.util import request_client_token
from tekore import Spotify
from tekore.scope import read
from tekore.util import prompt_for_user_token
import tekore

def non_pop_list(spotify):
    track_list = []
    for set in range(0,40,20):
        library = spotify.saved_tracks(None,limit=20,offset=set).items
        for track in library:
            track_item = track.track
            if track_item.popularity <= 40:
                track_list.append(track_item)
    return track_list

def non_pop_recommended(track_list, spotify):
    top_5 = []
    reco_list = []
    for set in range(0,4):
        top_5.append(track_list[set])
    id_list = [track.id for track in top_5]
    recommended = spotify.recommendations(track_ids=id_list).tracks
    for track in recommended:
        reco_list.append(track)
    return reco_list

def set_up():
    client_id = 'd217fc4b5c4540d0bf2299a6c5a09c9a'
    client_secret = '504db230bc054da896f2c442e1a1f890'
    redirect_uri = 'https://google.com/'

    user_token = prompt_for_user_token(
        client_id,
        client_secret,
        redirect_uri,
        scope= read
    )

    app_token = request_client_token(client_id,client_secret)

    spotify = Spotify(app_token)
    spotify.token = user_token

    track_list = non_pop_list(spotify)
    recommended = non_pop_recommended(track_list,spotify)

    for track in recommended:
        artists = track.artists
        name = ""
        for artist in artists:
            if len(artists) == 1:
                name = artist.name
                break
            name += " & " + artist.name
        print(track.name + " by " + name)
    return 

if __name__ == "__main__":
    set_up()




# post = spotify.playback_currently_playing