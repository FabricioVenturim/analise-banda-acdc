import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

birdy_uri = 'spotify:artist:711MCceyCBcFnzjGY4Q7Un'
spotify = sp.Spotify(client_credentials_manager=SpotifyClientCredentials("7e81a5d9c8cc48d8ad1891c5774dd6a6", "da0cee2b1eb74750b08a50ba2f54af1d"))

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

# musics = spotify.arti
todas_musicas = dict()
todos_albuns = dict()
todos_tempos = dict()
todas_exibicoes = dict()
todas_letras = dict()

i = 0
albunsACDC = np.array([])

url = "https://www.letras.mus.br/ac-dc/"

for album in albums:
    musics = spotify.album_tracks('spotify:album:'+ album['id'])
    for cada in musics['items']:
        nome_musica = cada['name'].replace(" ", "-")
        html = urlopen(f"{url}{nome_musica}")
        bs = BeautifulSoup(html, "html.parser")

        exibicao = bs.find("div", {"class": "cnt-info_exib"}).find("b").text
        todas_exibicoes.update({i:exibicao})

        music = ""
        for verse in bs.find("div", {"class", "cnt-letra p402_premium"}).find_all("p"):
            music += " ".join(verse.stripped_strings)
            music += " "
        todas_letras.update({i:music})

        todas_musicas.update({i:cada['name']})
        todos_albuns.update({i:album['name']})
        todos_tempos.update({i:cada['duration_ms']})
        i += 1
    break
# spotify.
musica = {"Música":todas_musicas, "Álbum":todos_albuns, "Duração":todos_tempos, "Letras":todas_letras, "Exibições":todas_exibicoes}
df = pd.DataFrame(musica)
print(df.iloc())
