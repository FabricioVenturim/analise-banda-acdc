"""
Módulo responsável por criar o csv com as informações de cada música dos álbuns da banda
"""
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

def artist_albums(artist_id: str) -> dict:
    """Consulta a API do Spotify para todos os álbuns do artista escolhido
    
    :param artist_id: ID de artistas da API do Spotify
    :type artist_id: str
    :return: retorna um dicionário com informações de todos os álbuns de um artista
    :rtype: dict
    """    
    global spotify
    results = spotify.artist_albums(artist_id, album_type='album')
    albums = results['items']
    
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    return albums


def artist_musics(artist_id: str) -> pd.DataFrame:
    """Cria um data frame com informaçoes sobre todas as músicas do artista
    
    :param artist_id: id do artista na API do Spotify
    :type artist_id: str
    :return: retorna um DataFrame com vários álbums, cada album com várias músicas
    e cada música contém duração em ms, letra, popularidade, se é explicita ou não,
    dançabilidade, exibições, energia, volume,  "speechiness", acústica,
    instrumentalidade, vivacidade, valência e tempo
    :rtype: pd.DataFrame
    """      
    global spotify
    albums = (artist_albums(artist_id))
    
    todas_musicas = list()
    todos_albuns = list()
    todos_tempos = list()
    popularidade = list()
    explicita = list()
    dancabilidade = list()
    energia = list()
    volume = list()
    speechiness = list()
    acustica = list()
    instrumentalidade = list()
    vivacidade = list()
    valencia = list()
    tempo = list()
    for album in albums:
        musics = spotify.album_tracks('spotify:album:'+ album['id'])
        #Adicona as informações nas respectivas listas
        for cada in musics['items']:
            todas_musicas.append(cada['name'])
            todos_albuns.append(album['name'])
            todos_tempos.append(cada['duration_ms'])
            
            #algumas informações não ficam disponível em .albumstrack,
            # portanto temos que recorrer ao .track para conseguir todas as informações necessárias
            track = spotify.track('spotify:track:'+ cada['id'])
            popularidade.append(track['popularity'])
            explicita.append(track['explicit'])
            track = spotify.audio_features('spotify:track:'+ cada['id'])
            dancabilidade.append(track[0]['danceability'])
            energia.append(track[0]['energy'])
            volume.append(track[0]['loudness'])
            speechiness.append(track[0]['speechiness'])
            acustica.append(track[0]['acousticness'])
            instrumentalidade.append(track[0]['instrumentalness'])
            vivacidade.append(track[0]['liveness'])
            valencia.append(track[0]['valence'])
            tempo.append(track[0]['tempo'])
            
    
    musica = {"Álbum": todos_albuns, "Música": todas_musicas,
              "Duração":todos_tempos,'Popularidade': popularidade,
              'Explícita': explicita, 'Dançabilidade': dancabilidade,
              'Energia': energia, 'Volume': volume,
              'Speechiness': speechiness, 'Acustica': acustica,
              'Instrumentalidade': instrumentalidade, 'Vivacidade': vivacidade,
              'Tempo': tempo}
    return pd.DataFrame(musica)

                                ###################################
                                ### FUNÇÕES DO SCRAPING LENTRAS ###
                                ###################################

def get_links(band: str) -> dict:
    """Cria um dataframe com as letras e exibições do site Letras.com.br
    
    :param band: nome da banda que se deseja o dataframe
    :type band: str
    :return: dicionário com os nomes das músicas, letras e exibições
    :rtype: dict
    """       
    try:
        titulo = dict()
        letra = dict()
        popularidade = dict()

        html = urlopen(f"https://www.letras.mus.br/{band}") #Formata a url
        bs = BeautifulSoup(html, "html.parser") # pega todo html
        links = bs.find("div", {"class": "cnt-list--alp"}).find_all("a", "song-name") #Pega os angoras das letras
        
        index = 0
        for link in links: #Acessa cada link das letras e pega a letra/exibioções
            titulo[index] = link.span.text
            letra[index] = get_music(link.attrs["href"])
            popularidade[index] = get_popularity(link.attrs["href"])
            index += 1

        #Cria o dicionário que será usado para criação do df
        musica = {"musica": titulo, "letra": letra, "popularidade": popularidade}
        return musica
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da banda. {erro}")


def get_music(new_page: str) -> str:

    """Função para pegar as letras das músicas do site letras
    
    :param new_page: link do site da letra que se deseja pegar a letra
    :type new_page: str
    :return: string com a letra da música
    :rtype: str
    """       
    try:
        music = ""
        html = urlopen(f"https://www.letras.mus.br/{new_page}") #Formata a url
        bs = BeautifulSoup(html, "html.parser") # pega todo html
        #encontra todos os parágrafos e pega os versos e coloca em uma única string
        for verse in bs.find("div", {"class": "cnt-letra p402_premium"}).find_all("p"): 
            music += " ".join(verse.stripped_strings)
            music += " "
        return music
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da música. {erro}")

def get_popularity(new_page: str) -> int:
    """Função para pegar as exibições da música do site letra
    
    :param new_page: link da música que se deseja pegar as exibições
    :type new_page: str
    :return: número de exibições que aquela música teve no site letras
    :rtype: int
    """       
    try:
        html = urlopen(f"https://www.letras.mus.br/{new_page}")
        bs = BeautifulSoup(html, "html.parser")
        popularidade = bs.find("div", {"class": "cnt-info_exib"}).find("b").text
        popularidade = popularidade.replace(" ", "") # Necessário para alterar de str para int
        popularidade = popularidade.replace(".", "") # Necessário para alterar de str para int
        return int(popularidade)
    except Exception as erro:
        print(f"Ocorreu algum erro ao tentar acessar o site da música. {erro}") 

def create_dataset_letras(band: str) -> pd.DataFrame:
    """Função responsável por criar um dataframe com os nomes das músicas, letras e exibições do site letras.com.br. 
    
    :param band: nome da banda que se deseja ter um dataframe
    :type band: str
    :return: dataframe com os nomes das músicas, letras e exibições 
    :rtype: pd.DataFrame
    """ 
          
    musicas = get_links(band)
    df_musicas = pd.DataFrame(musicas)
    return df_musicas


                            ######################################
                            ### FUNÇÕES PARA JUNTAR OS DATASET ###
                            ######################################

def join_dataset(spotify: str, nome_letras: str):
    """Função para juntar o dataframe da API do spotify e o dataframe do scraping do site letras.com.br
    
    :param spotify: ID de artistas da API do Spotify
    :type spotify: str
    :param nome_letras: nome da banda que se deseja o dataframe
    :type nome_letras: str
    :return: um arquivo csv com a junção dos dois dataframe
    :rtype: csv
    """     
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
        titulo_site_letras = re.sub(r"[',;!?/.:]","", titulo_site_letras) #Tirar alguns caracteres especiais
        
        for index in range(0, len(albuns["Música"])):
            titulo_spotify = albuns.iloc[index]["Música"].replace(" ", "").lower() #Tirar os espaços e deixa em minúsculo 
            titulo_spotify = re.sub(r"[',;!?/.:]","", titulo_spotify) #Tirar alguns caracteres especiais
            if titulo_site_letras in titulo_spotify: #Compara com as letras do spotify
                albuns["Letra"][index] = letras.loc[index_letra]["letra"]
                albuns["Exibicoes"][index] = letras.loc[index_letra]["popularidade"]
                albuns["Música"][index] = titulo
        index_letra += 1
    return albuns.to_csv("dataset_acdc.csv", index = False)


#PARA ATUALIZAR O CSV
if __name__ == "__main__":
    join_dataset("spotify:artist:711MCceyCBcFnzjGY4Q7Un","ac-dc")