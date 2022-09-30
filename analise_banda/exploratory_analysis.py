import pandas as pd

df_musics = pd.read_csv("dataset_acdc.csv")

def popularidade_album(df):
    albums = df["Álbum"].unique()

    mais_populares = []
    menos_populares = []
    lista_albums = []
    valores_mais_ouvidas = []
    valores_menos_ouvidas = []

    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]

        index_max = musics_album["Popularidade"].idxmax()
        mais_popular = df["Música"].iloc[index_max]
        quantidade_exibicoes_max = df["Popularidade"].iloc[index_max]

        index_min = musics_album["Popularidade"].idxmin()
        menos_popular = df["Música"].iloc[index_min]
        quantidade_exibicoes_min = df["Popularidade"].iloc[index_min]

        mais_populares.append(mais_popular)
        valores_mais_ouvidas.append(quantidade_exibicoes_max)
        menos_populares.append(menos_popular)
        valores_menos_ouvidas.append(quantidade_exibicoes_min)
        lista_albums.append(album)

    popularidade = {"Álbum": lista_albums, "Mais Popular": mais_populares, "Valor Mais Popular": valores_mais_ouvidas, "Menos Populares": menos_populares, "Valor Menos Popular": valores_menos_ouvidas}
    return popularidade
        
# print(popularidade_album(df_musics))

def tamanho_musica_album(df):
    albums = df["Álbum"].unique()

    nomes_maiores = []
    nomes_menores = []
    lista_albums = []
    valores_maiores = []
    valores_menores = []

    for album in albums:
        musics_album = df.loc[df["Álbum"] == album]

        index_max = musics_album["Duração"].idxmax()
        maior = df["Música"].iloc[index_max]
        tamanho_maior = df["Duração"].iloc[index_max]

        index_min = musics_album["Duração"].idxmin()
        menor = df["Música"].iloc[index_min]
        tamanho_menor = df["Duração"].iloc[index_min]

        nomes_maiores.append(maior)
        valores_maiores.append(tamanho_maior)
        nomes_menores.append(menor)
        valores_menores.append(tamanho_menor)
        lista_albums.append(album)

    tamanhos = {"Álbum": lista_albums, "Música Maior": nomes_maiores, "Tamanho Maior": valores_maiores, "Música Menor": nomes_menores, "Tamanho Menor": valores_menores}
    return tamanhos

# print(tamanho_musica_album(df_musics))