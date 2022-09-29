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
        palavras.extend(re.findall('[\'|\w]+',texto, flags=re.IGNORECASE))
    return palavras

def contar_palavras(lista_texto: list[str]) -> dict :
    """conta a frequencia de palavras dentro da lista

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: dicionário com as palavras e sua contagem 
    :rtype: dict
    """    
    palavras = separar_palavras(lista_texto)
    palavras_unicas = np.unique(palavras)
    contagem_palavras = dict()
    for palavra in palavras_unicas:
        contagem_palavras[palavra] = palavras.count(palavra)
    return contagem_palavras

# musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')

# musicas = musicas[['Álbum','Música','Letra']]
# musica = musicas.iloc[0]
# print(musica['Letra'])
# titulo_albums =  np.unique(musicas['Álbum'].to_numpy())

# print(contar_palavras(separar_palavras(titulo_albums)))