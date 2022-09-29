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
def artist_musics(artist_id):
    """Cria um data frame com informaçoes sobre todas as músicas do artista

    Args:
        artist_id (str): id do artista na API do Spotify

    Returns:
        DataFrame: retorna um DataFrame com vários álbums, cada album com várias músicas e cada música contém duração em ms, letra, e exibições
    """    
    global spotify
    albums = (artist_albums(artist_id))
    
    todas_musicas = list()
    todos_albuns = list()
    todos_tempos = list()
    todas_exibicoes = list()
    todas_letras = list()
    popularidade = list()
    explicita = list()
    url = "https://www.letras.mus.br/ac-dc/"

    for album in albums:
        musics = spotify.album_tracks('spotify:album:'+ album['id'])
        for cada in musics['items']:
            nome_musica = cada['name'].replace(" ", "-")
            html = urlopen(f"{url}{nome_musica}")
            bs = BeautifulSoup(html, "html.parser")

            exibicao = bs.find("div", {"class": "cnt-info_exib"}).find("b").text
            todas_exibicoes.append(exibicao)

            music = ""
            for verse in bs.find("div", {"class", "cnt-letra p402_premium"}).find_all("p"):
                music += " ".join(verse.stripped_strings)
                music += " "
            todas_letras.append(music)
            todas_musicas.append(cada['name'])
            todos_albuns.append(album['name'])
            todos_tempos.append(cada['duration_ms'])
            
            #algumas informações não ficam disponível em .albumstrack, portanto temos que recorrer ao .treck para conseguir todas as informações necessárias
            track = spotify.track('spotify:track:'+ cada['id'])
            popularidade.append(track['popularity'])
            explicita.append(track['explicit'])
    index = pd.MultiIndex.from_tuples(list(zip(*[todos_albuns,todas_musicas])), names=["Álbum", "Música"])
    musica = {"Duração":todos_tempos, "Letras":todas_letras, "Exibições":todas_exibicoes, 'Popularidade': popularidade, 'Explícita': explicita}
    return pd.DataFrame(musica, index= index)
# print(artist_musics('spotify:artist:711MCceyCBcFnzjGY4Q7Un'))
# artist_musics('spotify:artist:711MCceyCBcFnzjGY4Q7Un').to_csv('ac-dc_musicas.csv', encoding='utf-8')