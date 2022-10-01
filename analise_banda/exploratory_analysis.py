import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

################
#### ITEM 1 ####
################

df_musicas = pd.read_csv("dataset_acdc.csv")    

def popularidade_album(df):
    albums = df["Álbum"].unique()
    
    lista_albuns = [] 
    musicas = []
    valores = []
    popularidade = []

    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]
        musics_album = musics_album.sort_values(by="Popularidade", ascending=False)
        
        #Mais popular
        mais_popular = musics_album["Música"].head(n=3)
        quantidade_exibicoes_max = musics_album["Popularidade"].head(n=3)
        for musica, quantidade in zip(mais_popular,quantidade_exibicoes_max):
            lista_albuns.append(album)
            musicas.append(musica)
            valores.append(quantidade)
            popularidade.append("Mais Popular")
        
        #Menos popular
        menos_popular = musics_album["Música"].tail(n=3)
        quantidade_exibicoes_min = musics_album["Popularidade"].tail(n=3)
        for musica,quantidade in zip(menos_popular, quantidade_exibicoes_min):
            lista_albuns.append(album)
            musicas.append(musica)
            valores.append(quantidade)
            popularidade.append("Menos Popular")
    popularidade = {"Álbum": lista_albuns ,"Música": musicas, "Popularidade": valores, "Tipo Popularidade": popularidade}
    return popularidade



################
#### ITEM 2 ####
################

def tamanho_musica_album(df):
    albums = df["Álbum"].unique()

    lista_albuns = []
    musicas = []
    duracoes = []
    tipo_duracao = []
    
    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]
        musics_album = musics_album.sort_values(by="Duração", ascending=False)
        
        #Mais longa
        musicas_mais_longas = musics_album["Música"].head(n=3)
        duracoes_max = musics_album["Duração"].head(n=3)
        for musica, duracao in zip(musicas_mais_longas, duracoes_max):
            lista_albuns.append(album)
            musicas.append(musica)
            duracoes.append(duracao)
            tipo_duracao.append("Mais Longas")

        #Mais curta
        musicas_mais_curta = musics_album["Música"].tail(n=3)
        duracoes_min = musics_album["Duração"].tail(n=3)
        for musica, duracao in zip(musicas_mais_curta, duracoes_min):
            lista_albuns.append(album)
            musicas.append(musica)
            duracoes.append(duracao)
            tipo_duracao.append("Mais Curtas")

    tamanhos = {"Álbum": lista_albuns, "Música": musicas, "Duraçao": duracoes, "Tipo Duração": tipo_duracao}
    return tamanhos

################
#### ITEM 3 ####
################

def popularidade_geral(df):
    musicas = []
    popularidade = []
    tipo_popularidade = []
    
    musicas_gerais = df.sort_values(by="Popularidade", ascending=False)
    
    #Mais popular
    mais_popular = musicas_gerais["Música"].head(n=3)
    quantidade_popularidade_max = musicas_gerais["Popularidade"].head(n=3)
    for musica, quantidade in zip(mais_popular,quantidade_popularidade_max):
        musicas.append(musica)
        popularidade.append(quantidade)
        tipo_popularidade.append("Mais Populares")
    
    #Menos popular
    menos_popular = musicas_gerais["Música"].tail(n=3)
    quantidade_popularidade_min = musicas_gerais["Popularidade"].tail(n=3)
    for musica, quantidade in zip(menos_popular, quantidade_popularidade_min):
        musicas.append(musica)
        popularidade.append(quantidade)
        tipo_popularidade.append("Menos Populares")

    popularidade_geral = {"Música": musicas, "Popularidade": popularidade, "Tipo Popularidade": tipo_popularidade}
    return popularidade_geral

################
#### ITEM 4 ####
################

def tamanho_musica_geral(df):
    musicas = []
    duracoes = []
    tipo_duracao = []
    
    musicas_gerais = df.sort_values(by="Duração", ascending=False)
    
    #Mais longa
    musicas_mais_longas = musicas_gerais["Música"].head(n=3)
    duracoes_mais_longas = musicas_gerais["Duração"].head(n=3)
    for musica, duracao in zip(musicas_mais_longas,duracoes_mais_longas):
        musicas.append(musica)
        duracoes.append(duracao)
        tipo_duracao.append("Mais Longas")
    
    #Mais curta
    menos_popular = musicas_gerais["Música"].tail(n=3)
    quantidade_popularidade_min = musicas_gerais["Duração"].tail(n=3)
    for musica, duracao in zip(menos_popular, quantidade_popularidade_min):
        musicas.append(musica)
        duracoes.append(duracao)
        tipo_duracao.append("Mais curtas")

    popularidade_geral = {"Música": musicas, "Duraçao": duracoes, "Tipo Duração": tipo_duracao}
    return popularidade_geral


################
#### ITEM 6 ####
################

def relacao_duracao_popularidade(df):
    df_new = df[["Popularidade", "Duração"]]
    corr_df = df_new.corr(method="pearson")
    return corr_df

