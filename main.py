import requests
import time
import spotipy
import os
import sys 
import json
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = 'd217fc4b5c4540d0bf2299a6c5a09c9a'
CLIENT_SECRET = '504db230bc054da896f2c442e1a1f890'
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None


# try:
#     token = util.prompt_for_user_token(username)
# except:
#     os.remove(f".cachce{username}")
#     token = util.prompt_for_user_token(username)

# print(token)

# spotifyObject = spotipy.Spotify(auth=token) 

# user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

for artist in sp.current_user_followed_artists():
    print("Artist: " + artist)