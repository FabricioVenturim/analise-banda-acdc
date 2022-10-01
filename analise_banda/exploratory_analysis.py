import pandas as pd
import numpy as np
import re
palavras_banidas = ['the', 'you', 'and','your','it\'s','she','get',"i'll","you're",'too','that','she\'s','i\'m','are','for','who', 'had','was','can']
def separar_palavras_texto(texto: str) -> list[str]:
    """recebe uma string e a separa em palavras

    :param texto: string contendo o texto
    :type texto: str
    :return: retorna uma lista de palavras com todas as palavras com no minimo 3 letras contidas em texto
    :rtype: list[str]
    """
    
    print(texto)    
    palavras = re.findall('\w{3,}',texto, flags=re.IGNORECASE)
    i=0
    while i < len(palavras):
        palavras[i] = palavras[i].lower()
        if palavras[i] in palavras_banidas:
            palavras.pop(i)
        else:
            i+=1
    return palavras

def separar_palavras_lista(lista_texto: list[str]) -> list[str] :    
    """Recebe uma lista de strings, e as separa em palavras

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: lista de todas as palavras contidas nas lista de strings
    :rtype: list[str]
    """    
    palavras = list()
    for texto in lista_texto:
        print(texto)
        palavras.extend(separar_palavras_texto(texto))
    return palavras

def contar_palavras(lista_texto: list[str]) -> dict :
    """conta a frequencia de palavras dentro da lista

    :param lista_texto: lista de textos
    :type lista_texto: list[str]
    :return: serie com as palavras e suas contagens 
    :rtype: dict
    """    
    palavras = pd.Series(separar_palavras_lista(lista_texto))
    
    return palavras.value_counts().to_dict()

def frequencia_titulo(titulo: str, texto: str) -> dict[str, int]:
    """conta a frequencia de palavras do titulo dentro do texto

    :param titulo: string com palavras a serem pesquisadsas no texto
    :type titulo: str
    :param texto: string onde as palavras do titulo vão ser pesquisadas
    :type texto: str
    :return: dicionario onde a chave são as palavras do título e os items são as
    frequências
    :rtype: dict[str, int]
    """    
    palavras_titulo = separar_palavras_texto(titulo)
    frequencia = dict()
    for palavra in palavras_titulo:
        frequencia_palavra =  re.findall(
            f'\W*({palavra})\W*', texto, flags= re.IGNORECASE)
        frequencia[palavra] = len(frequencia_palavra)
    return frequencia




# musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')

# musicas = musicas[['Álbum','Música','Letra']]

# titulos = np.unique(musicas['Música'])
# titulos = ' '.join(titulos)

# print(separar_palavras_texto(titulos))