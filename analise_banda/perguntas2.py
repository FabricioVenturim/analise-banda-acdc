import exploratory_analysis as ea
import pandas as pd
import numpy as np

musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')
musicas = musicas[['Álbum', 'Música', 'Letra']]
musicas = musicas.set_index('Álbum')
def pergunta2_1()-> dict[str, int]:
    """ Cria um dicionario com a frequência de cada palavra nos nomes dos álbuns do ACDC

    :return: retorna um dicionario com a frequencia de cada palavra
    :rtype: dict[str, int]
    """    
    global musicas
    nome_albuns = musicas.index.drop_duplicates()
    dicionario_albuns = ea.contar_palavras(nome_albuns)
    return dicionario_albuns

def pergunta2_2()-> dict[str, int]:
    """ Cria um dicionario com a frequência de cada palavra no nome das músicas do ACDC

    :return: retorna um dicionario com a frequencia de cada palavra
    :rtype: dict[str, int]
    """    
    global musicas
    nome_musicas = musicas['Música'].drop_duplicates()
    dicionario_musicas = ea.contar_palavras(nome_musicas)
    return dicionario_musicas

def pergunta2_3()-> dict[str, dict[str, int]]:
    """ Cria um dicionario com a frequencia de cada palavra em todas as letras
    de um album

    :return: retorna um dicionario com a frequencia de cada palavra categorizada por album
    :rtype: dict[str, dict[str, int]]
    """    
    global musicas
    nome_albuns = np.unique(musicas.index)
    frequencia_letras_album = {}
    for album in nome_albuns:
        musicas_album = musicas.loc[album]
        letras_album =musicas_album['Letra'].drop_duplicates()
        dicionario_letras = ea.contar_palavras(letras_album)
        frequencia_letras_album[album] = dicionario_letras
    return frequencia_letras_album

def pergunta2_4()-> dict[str, int]:
    """ Cria um dicionario com a frequencia de cada palavra em todas as letras

    :return: retorna um dicionario com a frequencia de cada palavra
    :rtype: dict[str, int]
    """    
    global musicas
    letras = musicas['Letra'].drop_duplicates()
    dicionario_frequencia_letras = ea.contar_palavras(letras)
    return dicionario_frequencia_letras

def pergunta2_5()-> dict[str, int]:
    """ Cria um dicionario com a frequencia em que as palavras do nome de todos os
    albúns aparecem em todas as letras

    :return: retorna um dicionario com a frequencia de cada palavra
    :rtype: dict[str, int]
    """    
    global musicas
    nome_albuns = musicas.index.drop_duplicates()
    letras = musicas['Letra'].drop_duplicates()
    frequencia_album_letras= ea.frequencia_titulo(' '.join(nome_albuns),
                                                  ' '.join(letras))
    return frequencia_album_letras

def pergunta2_6()-> dict[str, int]:
    """ Cria um dicionario com a frequencia em que as palavras do nome de todas as
    músicas aparecem em todas as letras

    :return: retorna um dicionario com a frequencia de cada palavra
    :rtype: dict[str, int]
    """    
    global musicas
    nome_musicas = musicas['Música'].drop_duplicates()
    letras = musicas['Letra'].drop_duplicates()
    frequencia_musica_letras= ea.frequencia_titulo(' '.join(nome_musicas),
                                                  ' '.join(letras))
    return frequencia_musica_letras
