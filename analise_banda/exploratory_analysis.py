import pandas as pd

################
#### ITEM 1 ####
################

df_musicas = pd.read_csv("dataset_acdc.csv")    
df_albums = pd.read_csv("premiacoes.csv")

def popularidade_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Popularidade por álbum,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos, depois salva a união dos dois em um terceiro DataFrame
    e enfim retorna a união de todos álbuns
    Args:
        df (pd.DataFrame): DataFrame das informações da banda

    Returns:
        pd.DataFrame: Dataframe contendo álbum, nome da música, popularidade e tipo(Mais Popular ou Menos Popular)
    """    
    albums = df["Álbum"].unique()
    df_final = pd.DataFrame(columns=["Álbum", "Música", "Popularidade", "Tipo"])

    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]
        musics_album = musics_album.sort_values(by="Popularidade", ascending=False)

        mais_populares = musics_album[["Álbum","Música","Popularidade"]].head(n=3).assign(Tipo = ["Mais Popular","Mais Popular","Mais Popular"])
        menos_populares = musics_album[["Álbum","Música","Popularidade"]].tail(n=3).assign(Tipo = ["Menos Popular","Menos Popular","Menos Popular"])

        conjunto_mais_menos_populares = pd.merge(mais_populares,menos_populares, how = "outer")
        df_final = pd.merge(df_final, conjunto_mais_menos_populares, how = "outer")

    return df_final

################
#### ITEM 2 ####
################

def tamanho_musica_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Duração por álbum,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos, depois salva a união dos dois em um terceiro DataFrame
    e enfim retorna a união de todos álbuns

    Args:
        df (pd.DataFrame): DataFrame das informações da banda
    Returns:
        pd.DataFrame: DataFrame contendo álbum, nome da música, duração e tipo(Mais Longas ou Mais Curtas)
    """    
    albums = df["Álbum"].unique()
    df_final = pd.DataFrame(columns=["Álbum","Música","Duração","Tipo"])
    
    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]
        musics_album = musics_album.sort_values(by="Duração", ascending=False)
        
        musicas_mais_longas = musics_album[["Álbum","Música","Duração"]].head(n=3).assign(Tipo=["Mais Longas", "Mais Longas", "Mais longas"])
        musicas_mais_curtas = musics_album[["Álbum","Música","Duração"]].tail(n=3).assign(Tipo=["Mais Curtas", "Mais Curtas", "Mais Curtas"])

        conjunto_maiores_menores = pd.merge(musicas_mais_longas, musicas_mais_curtas, how="outer")
        df_final = pd.merge(df_final, conjunto_maiores_menores, how="outer")

    return df_final

################
#### ITEM 3 ####
################

def popularidade_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Popularidade,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos e depois retorna a união deles
    Args:
        df (pd.DataFrame): DataFrame das informações da banda
    Returns:
        pd.DataFrame: Dataframe contendo nome da música, popularidade e tipo(Mais Popular ou Menos Popular)
    """    
    musicas_gerais = df.sort_values(by="Popularidade", ascending=False)
    
    mais_popular = musicas_gerais[["Música", "Popularidade"]].head(n=3).assign(Tipo=["Mais Popular","Mais Popular","Mais Popular"])
    menos_popular = musicas_gerais[["Música", "Popularidade"]].tail(n=3).assign(Tipo=["Menos Popular","Menos Popular","Menos Popular"])
    df_final = pd.merge(mais_popular, menos_popular, how="outer")
    return df_final

################
#### ITEM 4 ####
################

def tamanho_musica_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Duração,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos e depois retorna a união deles

    Args:
        df (pd.DataFrame): DataFrame das informações da banda

    Returns:
        pd.DataFrame: DataFrame contendo nome da música, duração e tipo(Mais Longas ou Mais Curtas)
    """        
    musicas_gerais = df.sort_values(by="Duração", ascending=False)

    musicas_mais_longas = musicas_gerais[["Música","Duração"]].head(n=3).assign(Tipo=["Mais Longas", "Mais Longas", "Mais longas"])
    musicas_mais_curtas = musicas_gerais[["Música","Duração"]].tail(n=3).assign(Tipo=["Mais Curtas", "Mais Curtas", "Mais Curtas"])
    df_final = pd.merge(musicas_mais_longas,musicas_mais_curtas,how="outer")
    return df_final

################
#### ITEM 5 ####
################

def premiacoes_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro pelos valores da sua soma envolvendo peso com os prêmios em cada
    tipo(prata, ouro, platina e diamante) e retorna um DataFrame contendo as informações dos 3 primeiros
    Args:
        df (pd.DataFrame): DataFrame das premiações dos álbuns da banda
    Returns:
        pd.DataFrame: Dataframe dos 3 álbuns mais premiados e a quantidade de prêmios em cada tipo(prata, ouro, platina e diamante)
    """    
    albums_gerais = df.sort_values(by = "Soma_peso", ascending = False)

    df_final = albums_gerais[["Álbum","Prata","Ouro","Platina","Diamante"]].head(n=3)

    return df_final

################
#### ITEM 6 ####
################

def relacao_duracao_popularidade(df: pd.DataFrame) -> pd.DataFrame:
    """A função cria um novo DataFrame contendo as informações da Popularidade e Duração do parâmetro recebido,
    calcula e retorna a correlação entre os valores das colunas

    Args:
        df (pd.DataFrame): DataFrame das informações da banda
    Returns:
        pd.DataFrame: DataFrame da correlação entre a Popularidade das músicas e sua Duração
    """    
    # Correlação entre a popularidade e a duração
    df_new = df[["Popularidade", "Duração"]]
    corr_df = df_new.corr(method="pearson")
    return corr_df