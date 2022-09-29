import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def separar_palavras(lista_texto: list[str]) -> list[str] :
    """Recebe uma lista de strings, e as separa em palavras

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: lista de todas as palavras contidas nas lista de strings
    :rtype: list[str]
    """    
    palavras = list()
    for texto in lista_texto:
        plv = re.findall('[\'\w]+',texto, flags=re.IGNORECASE)
        for palavra in plv:
            palavras.append(palavra.lower())
    return palavras

def contar_palavras(lista_texto: list[str]) -> pd.Series :
    """conta a frequencia de palavras dentro da lista

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: serie com as palavras e sua contagem 
    :rtype: pd.Series
    """    
    palavras = pd.Series(separar_palavras(lista_texto))
    
    return palavras.value_counts().to_dict()
