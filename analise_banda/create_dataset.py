import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd

##########################
### FUNÇÕES DO SPOTIFY ###
##########################

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
    popularidade = list()
    explicita = list()


    for album in albums:
        musics = spotify.album_tracks('spotify:album:'+ album['id'])
        for cada in musics['items']:
            todas_musicas.append(cada['name'])
            todos_albuns.append(album['name'])
            todos_tempos.append(cada['duration_ms'])
            
            #algumas informações não ficam disponível em .albumstrack, portanto temos que recorrer ao .treck para conseguir todas as informações necessárias
            track = spotify.track('spotify:track:'+ cada['id'])
            popularidade.append(track['popularity'])
            explicita.append(track['explicit'])
    #index = pd.MultiIndex.from_tuples(list(zip(*[todos_albuns,todas_musicas])), names=["Álbum", "Música"])
    musica = {"Álbum": todos_albuns, "Música": todas_musicas, "Duração":todos_tempos,'Popularidade': popularidade, 'Explícita': explicita}
    return pd.DataFrame(musica) #, index= index
# print(artist_musics('spotify:artist:711MCceyCBcFnzjGY4Q7Un'))
# artist_musics('spotify:artist:711MCceyCBcFnzjGY4Q7Un').to_csv('ac-dc_musicas.csv', encoding='utf-8')
#artist_musics('spotify:artist:711MCceyCBcFnzjGY4Q7Un')

###################################
### FUNÇÕES DO SCRAPING LENTRAS ###
###################################

def get_links(band):
    try:
        titulo = dict()
        letra = dict()
        popularidade = dict()

        html = urlopen(f"https://www.letras.mus.br/{band}")
        bs = BeautifulSoup(html, "html.parser") #todo html
        links = bs.find("div", {"class": "cnt-list--alp"}).find_all("a", "song-name")
        
        index = 0
        for link in links: 
            titulo[index] = link.span.text
            letra[index] = get_music(link.attrs["href"])
            popularidade[index] = get_popularity(link.attrs["href"])
            index += 1

        musica = {"musica": titulo, "letra": letra, "popularidade": popularidade}
        return musica
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da banda. {erro}")


def get_music(new_page):
    try:
        music = ""
        html = urlopen(f"https://www.letras.mus.br/{new_page}")
        bs = BeautifulSoup(html, "html.parser")
        for verse in bs.find("div", {"class": "cnt-letra p402_premium"}).find_all("p"):
            music += " ".join(verse.stripped_strings)
            music += " "
        return music
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da música. {erro}")

def get_popularity(new_page):
    try:
        html = urlopen(f"https://www.letras.mus.br/{new_page}")
        bs = BeautifulSoup(html, "html.parser")
        popularidade = bs.find("div", {"class": "cnt-info_exib"}).find("b").text
        return popularidade
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da música. {erro}") 

def create_dataset_letras(band):
    musicas = get_links(band)
    df_musicas = pd.DataFrame(musicas)
    return df_musicas

#create_dataset_letras('ac-dc')

######################################
### FUNÇÕES PARA JUNTAR OS DATASET ###
######################################

def join_dataset(spotify, nome_letras):
    #df do spotify
    albuns = artist_musics(spotify)

    #csv do site letras
    letras = create_dataset_letras(nome_letras)

    #Criar as duas colunas no df albuns
    albuns["Letra"] = ""
    albuns["Exibicoes"] = ""

    #Percorrer os nomes e encontrar os semelhantes para fazer o join
    index_letra = 0 
    nomes_site_letra = list(letras["musica"]) #Deixa todas as musicas em uma lista 
    for titulo in nomes_site_letra:
        titulo_site_letras = titulo.replace(" ", "").lower() #Tirar os espaços e deixa em minúsculo 
        titulo_site_letras = re.sub(r"[,;!?/.:]","", titulo_site_letras) #Tirar alguns caracteres especiais
        
        for index in range(0, len(albuns["Música"])):
            titulo_spotify = albuns.iloc[index]["Música"].replace(" ", "").lower() #Tirar os espaços e deixa em minúsculo 
            titulo_spotify = re.sub(r"[,;!?/.:]","", titulo_spotify) #Tirar alguns caracteres especiais
            if titulo_site_letras in titulo_spotify: #Compara com as letras do spotify
                albuns["Letra"][index] = letras.loc[index_letra]["letra"]
                albuns["Exibicoes"][index] = letras.loc[index_letra]["popularidade"]
        index_letra += 1
    return albuns.to_csv("dataset_acdc.csv")

join_dataset("spotify:artist:711MCceyCBcFnzjGY4Q7Un","ac-dc")