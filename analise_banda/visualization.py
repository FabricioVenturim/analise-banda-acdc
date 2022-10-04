import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#############################
### Gráficos da questão 1 ###
#############################

def grafico_popularidade_album(df_albuns: pd.DataFrame):
    """Função para criar e salvar os gráficos das músicas mais populares e menos populares de cada álbum da banda

    :param df_albuns: DataFrame com as 3 músicas mais famosas e as 3 músicas menos famosas de cada álbum
    :type df_albuns: pd.DataFrame
    """   

    albuns = df_albuns["Álbum"].unique() #Pega os albuns
    index = 0 #index para salvar as imagens com número de identificação
    for album in albuns:
        musicas_album = df_albuns.loc[df_albuns["Álbum"] == album]
        #criando uma figure, axes, alterando tamanho
        fig, graf = plt.subplots(figsize=(9,6))
        #criando o gráfico de barras
        sns.barplot(data=musicas_album, y="Música", x="Popularidade", ax=graf, hue = "Tipo Popularidade" )
        #adicionando título
        graf.set_title(f"Popularidade das Músicas do Álbum {album}", fontdict={"fontsize":15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

        graf.get_figure().savefig(f"../img/questao_1.1/1atividade-{index}.png",bbox_inches="tight")
        index += 1
        plt.close()

#############################
### Gráficos da questão 2 ###
#############################

def grafico_duracao_album(df_albuns: pd.DataFrame):
    """Função para criar e salvar os gráficos das músicas mais longas e mais curtas de cada álbum da banda

    :param df_albuns: DataFrame com as 3 músicas mais longas e as 3 músicas mais curtas de cada álbum
    :type df_albuns: pd.DataFrame
    """    

    albuns = df_albuns["Álbum"].unique()#Pega os albuns
    index = 0 #index para salvar as imagens com número de identificação
    for album in albuns:
        musicas_album = df_albuns.loc[df_albuns["Álbum"] == album]
        
        #criando uma figure, axes, alterando tamanho
        fig, graf = plt.subplots(figsize=(9,6))
        #criando o gráfico de barras
        sns.barplot(data=musicas_album, y="Música", x="Duração", ax=graf, hue = "Tipo Duração" )
        #adicionando título
        graf.set_title(f"Duração das Músicas do Álbum {album}", fontdict={"fontsize":15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel("Duração (milissegundos)", fontdict={"fontsize":13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

        graf.get_figure().savefig(f"../img/questao_1.2/2atividade-{index}.png",bbox_inches="tight")
        index += 1
        plt.close()

#############################
### Gráficos da questão 3 ###
#############################

def grafico_popularidade_geral(df_musicas: pd.DataFrame):
    """Função para criar e salvar o gráfico das músicas mais populares e menos populares de toda história da banda

    :param df_albuns: DataFrame com as 3 músicas mais famosas e as 3 músicas menos famosas de toda história da banda
    :type df_albuns: pd.DataFrame
    """    

    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_musicas, y="Música", x="Popularidade", ax=graf, hue = "Tipo Popularidade" )
    #adicionando título
    graf.set_title("Popularidade das Músicas da banda AC/DC", fontdict={"fontsize":15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

    graf.get_figure().savefig(f"../img/questao_1.3/3atividade.png",bbox_inches="tight")
    plt.close()

#############################
### Gráficos da questão 4 ###
#############################

def grafico_tamanho_musica_geral(df_musicas: pd.DataFrame):
    """Função para criar e salvar o gráfico das músicas mais longas e mais curtas de toda história da banda

    :param df_albuns: DataFrame com as 3 músicas mais longas e as 3 músicas mais curtas de de toda história da banda
    :type df_albuns: pd.DataFrame
    """   

    #Transforma o dicionario em dataframe
    df_musicas["Música"].mask((df_musicas["Música"]=="Let There Be Rock") & (df_musicas["Duração"]==736133), other = "Let There Be Rock (LIVE)" , inplace=True)    
    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_musicas, y="Música", x="Duração", ax=graf, hue = "Tipo Duração" )
    #adicionando título
    graf.set_title("Duração das Músicas da banda AC/DC", fontdict={"fontsize":15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Duração", fontdict={"fontsize":13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

    graf.get_figure().savefig(f"../img/questao_1.4/4atividade.png",bbox_inches="tight")
    plt.close()

#############################
### Gráficos da questão 5 ###
#############################

def grafico_premiacoes_album(df_premiacoes: pd.DataFrame):
    """Função para criar e salvar o gráfico dos álbuns mais premiados da banda

    :param df_albuns: DataFrame com os 3 álbuns mais premiados e suas premiações
    :type df_albuns: pd.DataFrame
    """    

    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_premiacoes, y="Álbum", x="Quantidade", hue="Tipo", ax=graf)
    #adicionando título
    graf.set_title("Premiações dos 3 álbuns mais premiados da banda AC/DC", fontdict={"fontsize":15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Premiações", fontdict={"fontsize":13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

    graf.get_figure().savefig(f"../img/questao_1.4/graf_premiacoes.png",bbox_inches="tight")
    plt.close()

#############################
### Gráficos da questão 6 ###
#############################

def grafico_corresp(corr_df: pd.DataFrame):
    """Função para criar e salvar o gráfico de correlação das variáveis popularidade e duração das músicas

    :param df_albuns: DataFrame com as correlações entre as duas variáveis
    :type df_albuns: pd.DataFrame
    """ 

    fig, graf = plt.subplots(figsize=(9,6))
    sns.heatmap(corr_df, annot=True, ax=graf)
    #adicionando título
    graf.set_title("Correlação entre Popularidade das músicas e sua Duração", fontdict={"fontsize":15})
    #salvar
    graf.get_figure().savefig(f"../img/questao_1.6/corresp.png",bbox_inches="tight")

def grafico_plot(df: pd.DataFrame):
    """Função para criar e salvar o gráfico de dispersão das variáveis popularidade e duração das músicas

    :param df_albuns: DataFrame com todas as músicas e as variáveis popularidade e duração das músicas
    :type df_albuns: pd.DataFrame
    """ 

    fig, graf = plt.subplots(figsize=(9,6))
    sns.scatterplot(df, x=df["Popularidade"], y=df["Duração"], ax=graf)
    plt.ticklabel_format(style="plain", axis="y")
    #adicionando título
    graf.set_title("Gráfico de dispersão", fontdict={"fontsize":15})
    #eixos
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("Duração em milissegundos", fontdict={"fontsize":13})
    #salvar gráfico
    graf.get_figure().savefig(f"../img/questao_1.6/plot.png",bbox_inches="tight")