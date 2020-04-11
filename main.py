import requests
import time
import spotipy
import os
import sys 
import json
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError


SET = "d217fc4b5c4540d0bf2299a6c5a09c9a"
SET ="504db230bc054da896f2c442e1a1f890"

sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])