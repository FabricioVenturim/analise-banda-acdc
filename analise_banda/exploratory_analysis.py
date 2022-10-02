import pandas as pd

################
#### ITEM 1 ####
################

df_musicas = pd.read_csv("dataset_acdc.csv")    
df_albums = pd.read_csv("premiacoes.csv")

def popularidade_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Popularidade por álbum,
    separa em séries as informações dos 3 primeiros e 3 últimos, depois inclue em listas essas 
    informações e enfim cria um dicionário com cada uma delas, após isso faz a transformação em DataFrame

    Args:
        df (pd.DataFrame): DataFrame das informações da banda

    Returns:
        pd.DataFrame: Dataframe contendo álbum, nome da música, popularidade e tipo da popularidade(Mais Populares ou Menos Populares)
    """    
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
    df_popularidade = pd.DataFrame(popularidade)
    return df_popularidade



################
#### ITEM 2 ####
################

def tamanho_musica_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Duração por álbum,
    separa em séries as informações dos 3 primeiros e 3 últimos, depois inclue em listas essas 
    informações e enfim cria um dicionário com cada uma delas, após isso faz a transformação em DataFrame

    Args:
        df (pd.DataFrame): DataFrame das informações da banda
    Returns:
        pd.DataFrame: DataFrame contendo álbum, nome da música, duração e tipo da duração(Mais Longas ou Mais Curtas)
    """    
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

    duracoes_gerais = {"Álbum": lista_albuns, "Música": musicas, "Duração": duracoes, "Tipo Duração": tipo_duracao}
    df_duracoes = pd.DataFrame(duracoes_gerais)
    return df_duracoes

################
#### ITEM 3 ####
################

def popularidade_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Popularidade,
    separa em séries as informações dos 3 primeiros e 3 últimos, depois inclue em listas essas 
    informações e enfim cria um dicionário com cada uma delas, após isso faz a transformação em DataFrame
    Args:
        df (pd.DataFrame): DataFrame das informações da banda
    Returns:
        pd.DataFrame: Dataframe contendo nome da música, popularidade e tipo da popularidade(Mais Populares ou Menos Populares)
    """    
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
    df_popularidade_geral = pd.DataFrame(popularidade_geral)
    return df_popularidade_geral

################
#### ITEM 4 ####
################

def tamanho_musica_geral(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido com parâmetro de acordo com os valores da coluna de Duração,
    separa em séries as informações dos 3 primeiros e 3 últimos, depois inclue em listas essas 
    informações e enfim cria um dicionário com cada uma delas, após isso faz a transformação em DataFrame

    Args:
        df (pd.DataFrame): DataFrame das informações da banda

    Returns:
        pd.DataFrame: DataFrame contendo nome da música, duração e tipo da duração(Mais Longas ou Mais Curtas)
    """        
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
    musicas_menos_longas = musicas_gerais["Música"].tail(n=3)
    duracoes_menos_longas = musicas_gerais["Duração"].tail(n=3)
    for musica, duracao in zip(musicas_menos_longas, duracoes_menos_longas):
        musicas.append(musica)
        duracoes.append(duracao)
        tipo_duracao.append("Mais curtas")

    duracoes_gerais = {"Música": musicas, "Duração": duracoes, "Tipo Duração": tipo_duracao}
    df_duracoes_gerais = pd.DataFrame(duracoes_gerais)
    return df_duracoes_gerais

################
#### ITEM 5 ####
################

def premiacoes_album(df: pd.DataFrame) -> pd.DataFrame:
    """A função ordena o DataFrame recebido como parâmetro pelos valores da sua soma envolvendo peso com os prêmios em cada
    tipo(prata, ouro, platina e diamante), separa em séries as informações dos 3 primeiros, depois inclue em listas essas 
    informações e enfim cria um dicionário com cada uma delas, após isso faz a transformação em DataFrame
    Args:
        df (pd.DataFrame): DataFrame das premiações dos álbuns da banda
    Returns:
        pd.DataFrame: Dataframe dos 3 álbuns mais premiados e a quantidade de prêmios em cada tipo(prata, ouro, platina e diamante)
    """    
    albums = []
    pratas = []
    ouros = []
    platinas = []
    diamantes = []

    albums_geral = df.sort_values(by = "Soma_peso", ascending = False)

    # Informações álbuns mais premiados
    albums_mais_premiados = albums_geral["Álbum"].head(n=3)
    pratas_albums = albums_geral["Prata"].head(n=3)
    ouros_albums = albums_geral["Ouro"].head(n=3)
    platinas_albums = albums_geral["Platina"].head(n=3)
    diamantes_albums = albums_geral["Diamante"].head(n=3)

    for album, prata, ouro, platina, diamante in zip(albums_mais_premiados, pratas_albums, ouros_albums, platinas_albums, diamantes_albums):
        albums.append(album)
        pratas.append(prata)
        ouros.append(ouro)
        platinas.append(platina)
        diamantes.append(diamante)

    premiacoes_gerais = {"Álbum":albums, "Prata":pratas, "Ouro":ouros, "Platina":platinas, "Diamante":diamantes}
    df_premiacoes_gerais = pd.DataFrame(premiacoes_gerais)
    return df_premiacoes_gerais

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

