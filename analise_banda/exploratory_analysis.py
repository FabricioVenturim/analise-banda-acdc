import pandas as pd

df_musicas = pd.read_csv("dataset_acdc.csv")    
df_albums = pd.read_csv("premiacoes.csv")

################
#### ITEM 1 ####
################

def popularidade_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Popularidade por álbum,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos, depois salva a união dos dois em um terceiro DataFrame
    e enfim retorna a união de todos álbuns

    :param df: DataFrame das informações da banda AC/DC contendo no mínimo as colunas Álbum, Música, Duração, Popularidade, Letra e Exibicoes
    :type df: pd.DataFrame
    :return: Dataframe contendo álbum, nome da música, popularidade e tipo(Mais Popular ou Menos Popular)
    :rtype: pd.DataFrame
    """        
    albums = df["Álbum"].unique() # Separação dos álbuns
    df_final = pd.DataFrame(columns=["Álbum", "Música", "Popularidade", "Tipo"]) # DataFrame vazio para ser usado a frente como armazenamento das informações

    for album in albums:
        musics_album = df.loc[df["Álbum"] == album] # Localização das músicas por álbum
        musics_album = musics_album.sort_values(by="Popularidade", ascending=False) # Ordenação das músicas por Popularidade

        mais_populares = musics_album[["Álbum","Música","Popularidade"]].head(n=3).assign(Tipo = ["Mais Popular","Mais Popular","Mais Popular"]) # DataFrame contendo coluna Música, Popularidade e Tipo das 3 primeiras músicas
        menos_populares = musics_album[["Álbum","Música","Popularidade"]].tail(n=3).assign(Tipo = ["Menos Popular","Menos Popular","Menos Popular"]) # DataFrame contendo coluna Música, Popularidade e Tipo das 3 últimas músicas

        conjunto_mais_menos_populares = pd.merge(mais_populares,menos_populares, how = "outer") # DataFrame concatenando os DataFrames mais_populares e menos_populares
        df_final = pd.merge(df_final, conjunto_mais_menos_populares, how = "outer") # Salvando os valores no DataFrame Final

    return df_final

################
#### ITEM 2 ####
################

def tamanho_musica_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Duração por álbum,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos, depois salva a união dos dois em um terceiro DataFrame
    e enfim retorna a união de todos álbuns

    :param df: DataFrame das informações da banda AC/DC contendo no mínimo as colunas Álbum, Música, Duração, Popularidade, Letra e Exibicoes
    :type df: pd.DataFrame
    :return: DataFrame contendo álbum, nome da música, duração e tipo(Mais Longas ou Mais Curtas)
    :rtype: pd.DataFrame
    """    
    albums = df["Álbum"].unique() # Separação dos álbuns
    df_final = pd.DataFrame(columns=["Álbum","Música","Duração","Tipo"]) # DataFrame vazio para ser usado a frente como armazenamento das informações
    
    for album in albums:
        musics_album = df.loc[df["Álbum"] == album] # Localização das músicas por álbum
        musics_album = musics_album.sort_values(by="Duração", ascending=False) # Ordenação das músicas por valor da Duração
        
        musicas_mais_longas = musics_album[["Álbum","Música","Duração"]].head(n=3).assign(Tipo=["Mais Longas", "Mais Longas", "Mais Longas"]) # DataFrame contendo coluna Música, Duração e Tipo das 3 primeiras músicas
        musicas_mais_curtas = musics_album[["Álbum","Música","Duração"]].tail(n=3).assign(Tipo=["Mais Curtas", "Mais Curtas", "Mais Curtas"]) # DataFrame contendo coluna Música, Duração e Tipo das 3 últimas músicas

        conjunto_maiores_menores = pd.merge(musicas_mais_longas, musicas_mais_curtas, how="outer") # DataFrame concatenando os DataFrames musicas_mais_longas e musicas_mais_curtas
        df_final = pd.merge(df_final, conjunto_maiores_menores, how="outer") # Salvando os valores no DataFrame Final

    return df_final

################
#### ITEM 3 ####
################

def popularidade_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro de acordo com os valores da coluna de Popularidade,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos e depois retorna a união deles

    :param df:  DataFrame das informações da banda AC/DC contendo no mínimo as colunas Álbum, Música, Duração, Popularidade, Letra e Exibicoes
    :type df: pd.DataFrame
    :return: Dataframe contendo nome da música, popularidade e tipo(Mais Popular ou Menos Popular)
    :rtype: pd.DataFrame
    """    
    try:  
        musicas_gerais = df.sort_values(by="Popularidade", ascending=False) # Dataframe com a ordenação do parâmetro seguindo a Popularidade
        
        mais_popular = musicas_gerais[["Música", "Popularidade"]].head(n=3).assign(Tipo=["Mais Popular","Mais Popular","Mais Popular"]) # DataFrame contendo coluna Música, Popularidade e Tipo das 3 primeiras músicas
        menos_popular = musicas_gerais[["Música", "Popularidade"]].tail(n=3).assign(Tipo=["Menos Popular","Menos Popular","Menos Popular"]) # DataFrame contendo coluna Música, Popularidade e Tipo das 3 últimas músicas
        df_final = pd.merge(mais_popular, menos_popular, how="outer") # DataFrame concatenando os DataFrames mais_popular e menos_popular
    except KeyError:
        return ("Parâmetro não contendo as colunas especificadas")
    except AttributeError:
        return ("Tipo incorreto de parâmetro")
    return df_final

################
#### ITEM 4 ####
################

def tamanho_musica_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Duração,
    separa em DataFrames as informações dos 3 primeiros e 3 últimos e depois retorna a união deles

    :param df: DataFrame das informações da banda AC/DC contendo no mínimo as colunas Álbum, Música, Duração, Popularidade, Letra e Exibicoes
    :type df: pd.DataFrame
    :return: DataFrame contendo nome da música, duração e tipo(Mais Longas ou Mais Curtas)
    :rtype: pd.DataFrame
    """    
    try:       
        musicas_gerais = df.sort_values(by="Duração", ascending=False) # DataFrame com a ordenação do parâmetro seguindo seus valores da Duração

        musicas_mais_longas = musicas_gerais[["Música","Duração"]].head(n=3).assign(Tipo=["Mais Longas", "Mais Longas", "Mais Longas"]) # DataFrame contendo coluna Música, Duração e Tipo das 3 primeiras músicas
        musicas_mais_curtas = musicas_gerais[["Música","Duração"]].tail(n=3).assign(Tipo=["Mais Curtas", "Mais Curtas", "Mais Curtas"]) # DataFrame contendo coluna Música, Duração e Tipo das 3 últimas músicas
        df_final = pd.merge(musicas_mais_longas,musicas_mais_curtas,how="outer") # DataFrame concatenando os DataFrames musicas_mais_longas e musicas_mais_curtas
    except KeyError:
        return ("Parâmetro não contendo as colunas especificadas")
    except AttributeError:
        return ("Tipo incorreto de parâmetro")
    return df_final

################
#### ITEM 5 ####
################

def premiacoes_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro pelos valores da sua soma envolvendo peso com os prêmios em cada
    tipo(prata, ouro, platina e diamante) e retorna um DataFrame contendo as informações dos 3 primeiros

    :param df: DataFrame das premiações dos álbuns da banda AC/DC contendo as colunas Álbum, Prata, Ouro, Platina, Diamante e Soma_peso
    :type df: pd.DataFrame
    :return: Dataframe dos 3 álbuns mais premiados e a quantidade de prêmios em cada tipo(prata, ouro, platina e diamante)
    :rtype: pd.DataFrame
    """    
    try:
        albums_gerais = df.sort_values(by = "Soma_peso", ascending = False) # Ordenação do DataFrame pela soma dos pesoas de suas premiações
        premios = ["Prata", "Ouro", "Platina", "Diamante"] # Lista de cada tipo de prêmio
        df_final = pd.DataFrame(columns=["Álbum", "Quantidade","Tipo"]) # DataFrame vazio para ser usado a frente como armazenamento das informações

        for premio in premios: 
            df_premio = albums_gerais[["Álbum",premio]].head(n=3) # Álbum e seu respectivo tipo de prêmio dos três primeiros Álbuns no quesito de premiação
            df_premio.rename(columns={premio:"Quantidade"}, inplace=True) # Renomeação da coluna do respectivo prêmio para Quantidade
            df_premio.insert(2, "Tipo", premio, allow_duplicates=False) # Inserção de uma nova coluna Tipo com valores do tipo do prêmio
            df_final = pd.merge(df_final, df_premio, how="outer") # Salvando os valores no DataFrame Final
    except KeyError:
        return ("Parâmetro não contendo as colunas especificadas")
    except AttributeError:
        return ("Tipo incorreto de parâmetro")
    return df_final

################
#### ITEM 6 ####
################

def relacao_duracao_popularidade(df: pd.DataFrame) -> pd.DataFrame:
    """A função cria um novo DataFrame contendo as informações da Popularidade e Duração do parâmetro recebido,
    calcula e retorna a correlação entre os valores das colunas

    :param df: DataFrame das informações da banda AC/DC contendo no mínimo as colunas Álbum, Música, Duração, Popularidade, Letra e Exibicoes 
    :type df: pd.DataFrame
    :return: DataFrame da correlação entre a Popularidade das músicas e sua Duração
    :rtype: pd.DataFrame
    """            
    try:
        df_new = df[["Popularidade", "Duração"]] # Criação de um DataFrame contendo apenas as colunas Popularidade e Duração do parâmetro passado
        corr_df = df_new.corr(method="pearson") # Correlação entre as colunas e seus valores
    except KeyError:
        return ("Parâmetro não contendo as colunas especificadas")
    except AttributeError:
        return ("Tipo incorreto de parâmetro")
    return corr_df