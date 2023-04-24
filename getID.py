#https://spotipy.readthedocs.io/en/2.22.1/

# Import libraries
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import pandas as pd
from tqdm import tqdm
import time


#Required credentials
#Spotify Developer credentials from developers.spotify.com
client_id = '2920ec1af7074a2f96e859b0246257f3'
client_secret = 'c986a95cc7f54a9a869ca9969eff9459'
redirect_uri = 'http://localhost:8888/callback/' #Not using this though 

#Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#5 This function will search tracks based on your input

limit = 10
keyword = str(input("Please enter some keywords to search tracks"))
results = sp.search(q=keyword, type='track', limit=10)

count = 0
while count < limit:
    for artist in results['tracks']['items'][count]['artists']:
        print(artist['id'])
        print(artist['name'])
        count += 1
