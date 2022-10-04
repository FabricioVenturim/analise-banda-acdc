import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def grafico_popularidade_album(dicionario):
    #Transforma o dicionario em dataframe
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
        #mudando nome e tamanho do label x e y
        graf.set_xlabel('Popularidade', fontdict={'fontsize':13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        graficos.append(graf.get_figure())
        plt.close()
    
    return graficos

def grafico_duracao_album(dicionario):
    #Transforma o dicionario em dataframe
    df_albuns = pd.DataFrame(dicionario)
    albuns = df_albuns["Álbum"].unique()
    graficos = list()
    
    for album in albuns:
        musics_album = df_albuns.loc[df_albuns["Álbum"] == album]
        
        #criando uma figure, axes, alterando tamanho
        fig, graf = plt.subplots(figsize=(9,6))
        #criando o gráfico de barras
        sns.barplot(data=musics_album, y="Música", x="Duraçao", ax=graf, hue = "Tipo Duração" )
        #adicionando título
        graf.set_title(f"Duração das Músicas do Álbum {album}", fontdict={'fontsize':15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel('Duração (milissegundos)', fontdict={'fontsize':13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        graficos.append(graf.get_figure())
        plt.close()
    
    return graficos

def grafico_popularidade_geral(dicionario):
    #Transforma o dicionario em dataframe
    df_musicas = pd.DataFrame(dicionario)
    graficos = list()

    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_musicas, y="Música", x="Popularidade", ax=graf, hue = "Tipo Popularidade" )
    #adicionando título
    graf.set_title("Popularidade das Músicas da banda AC/DC", fontdict={'fontsize':15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel('Popularidade', fontdict={'fontsize':13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    graficos.append(graf.get_figure())
    plt.close()

    return graficos

def grafico_tamanho_musica_geral(dicionario):
    #Transforma o dicionario em dataframe
    df_musicas = pd.DataFrame(dicionario) 
    df_musicas["Música"].mask((df_musicas["Música"]=="Let There Be Rock") & (df_musicas["Duraçao"]==736133), other = "Let There Be Rock (LIVE)" , inplace=True)    
    graficos = list()

    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_musicas, y="Música", x="Duraçao", ax=graf, hue = "Tipo Duração" )
    #adicionando título
    graf.set_title("Duração das Músicas da banda AC/DC", fontdict={'fontsize':15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel('Popularidade', fontdict={'fontsize':13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    graficos.append(graf.get_figure())
    plt.close()

    return graficos