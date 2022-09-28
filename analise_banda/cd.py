import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# spotify stores Spotify's API client credentials
spotify = sp.Spotify(client_credentials_manager=SpotifyClientCredentials("7e81a5d9c8cc48d8ad1891c5774dd6a6", "da0cee2b1eb74750b08a50ba2f54af1d"))


def artist_albums(artist_id):
    """Consults Spotify API for all albuns of the choosen artist

    Args:
        artist_id (str): artists id from Spotify api

    Returns:
        dict: returns a dictionary with information of all albuns of an artist
    """    
    global spotify
    results = spotify.artist_albums(artist_id, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    return albums

albums = (artist_albums('spotify:artist:711MCceyCBcFnzjGY4Q7Un'))

for i in albums:
    print(i['name'])
