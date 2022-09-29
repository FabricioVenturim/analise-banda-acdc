from posixpath import sep
import pandas as pd
import numpy as np
import re

def separar_palavras(lista_texto: list[str]) -> list[str] :
    """Recebe uma lista de strings, e as separa em palavras

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: lista de todas as palavras contidas nas lista de strings
    :rtype: list[str]
    """    
    palavras = list()
    for texto in lista_texto:
        palavras.extend(re.findall('[\'\w]+',texto, flags=re.IGNORECASE))
    return palavras

def contar_palavras(lista_texto: list[str]) -> pd.Series :
    """conta a frequencia de palavras dentro da lista

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: serie com as palavras e sua contagem 
    :rtype: pd.Series
    """    
    palavras = pd.Series(separar_palavras(lista_texto))
    
    return palavras.value_counts()

# musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')

# musicas = musicas[['Álbum','Música','Letra']]
# musica = musicas.iloc[0]
# print(musica['Letra'])
# titulo_albums =  np.unique(musicas['Álbum'])
# print(titulo_albums)
# print(contar_palavras(separar_palavras(titulo_albums)))