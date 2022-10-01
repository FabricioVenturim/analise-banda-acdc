import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
        
        mais_popular = musics_album["Música"].head(n=3)
        quantidade_exibicoes_max = musics_album["Popularidade"].head(n=3)
        for musica, quantidade in zip(mais_popular,quantidade_exibicoes_max):
            lista_albuns.append(album)
            musicas.append(musica)
            valores.append(quantidade)
            popularidade.append("Mais Popular")

        menos_popular = musics_album["Música"].tail(n=3)
        quantidade_exibicoes_min = musics_album["Popularidade"].tail(n=3)
        for musica,quantidade in zip(menos_popular, quantidade_exibicoes_min):
            lista_albuns.append(album)
            musicas.append(musica)
            valores.append(quantidade)
            popularidade.append("Menos Popular")
    popularidade = {"Álbum":lista_albuns ,"Música":musicas, "Popularidade": valores, "Tipo Popularidade": popularidade}
    return popularidade

teste = popularidade_album(df_musicas)

def graficos(dicionario):
    df_albuns = pd.DataFrame(dicionario)
    albuns = df_albuns["Álbum"].unique()
    graficos = list()
    
    for album in albuns:
        musics_album = df_albuns.loc[df_albuns["Álbum"] == album]
        
        #criando uma figure, axes, alterando tamanho
        fig, graf = plt.subplots(figsize=(9,6))
        #criando o gráfico de barras
        sns.barplot(data=musics_album, y="Música", x="Popularidade", ax=graf, hue = "Tipo Popularidade" )
        #adicionando título
        graf.set_title(f"Popularidade das Músicas do Álbum {album}", fontdict={'fontsize':15})
        #mudando nome e tamanho do label x
        graf.set_xlabel('Popularidade', fontdict={'fontsize':13})
        graf.set_ylabel("")
        graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        graficos.append(graf.get_figure())
        plt.close()
    
    return graficos

graf = graficos(teste)
graf[0].savefig("gr",  bbox_inches='tight')