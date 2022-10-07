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
        sns.barplot(data=musicas_album, y="Música", x="Popularidade", ax=graf, hue = "Tipo")
        #adicionando título
        graf.set_title(f"Popularidade das Músicas do Álbum {album}", fontdict={"fontsize":15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

        graf.get_figure().savefig(f"img/questao_1.1/1atividade-{index}.png",bbox_inches="tight")
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
        sns.barplot(data=musicas_album, y="Música", x="Duração", ax=graf, hue = "Tipo")
        #adicionando título
        graf.set_title(f"Duração das Músicas do Álbum {album}", fontdict={"fontsize":15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel("Duração (milissegundos)", fontdict={"fontsize":13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

        graf.get_figure().savefig(f"img/questao_1.2/2atividade-{index}.png",bbox_inches="tight")
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
    sns.barplot(data=df_musicas, y="Música", x="Popularidade", ax=graf, hue = "Tipo")
    #adicionando título
    graf.set_title("Popularidade das Músicas da banda AC/DC", fontdict={"fontsize":15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

    graf.get_figure().savefig(f"img/questao_1.3/3atividade.png",bbox_inches="tight")
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
    sns.barplot(data=df_musicas, y="Música", x="Duração", ax=graf, hue = "Tipo")
    #adicionando título
    graf.set_title("Duração das Músicas da banda AC/DC", fontdict={"fontsize":15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Duração", fontdict={"fontsize":13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

    graf.get_figure().savefig(f"img/questao_1.4/4atividade.png",bbox_inches="tight")
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

    graf.get_figure().savefig(f"img/questao_1.4/graf_premiacoes.png",bbox_inches="tight")
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
    graf.get_figure().savefig(f"img/questao_1.6/corresp.png",bbox_inches="tight")

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
    graf.get_figure().savefig(f"img/questao_1.6/plot.png",bbox_inches="tight")

#gráficos das questão do grupo 3:

"""O spotify disponibilza vários dados sobre as músicas, 
    como a popularidade, energia da música, tempo, instrumentalidade, entre outros.
    Portanto achamos interessante analisar esses dados e ver se conseguimos encontrar
    Alguma relação entre eles e a popularidade da música."""

def pergunta_1(df_musica: pd.DataFrame):
    """Gera um gráfico de dispersão entre a popularidade e a energia da música

    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """    
    fig, graf = plt.subplots(figsize=(9,6))
    # Gráfico de dispersão entre a popularidade e a energia da música
    sns.scatterplot(data=df_musica, x=df_musica['Popularidade'], y=df_musica['Energia'], ax=graf)
    plt.ticklabel_format(style="plain", axis="y")
    # calculo do coeficiente de correlação entre popularidade e energia
    correlacao = df_musica['Popularidade'].corr(df_musica['Energia'])
    # anota o valor do coeficiente de correlação no gráfico
    plt.text(60, 0.5,s=correlacao, horizontalalignment='left', size='medium', color='black', weight='semibold')
    #adicionando título
    graf.set_title("Popularidade x Energia", fontdict={"fontsize":15})
    #eixos
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("Energia", fontdict={"fontsize":13})
    #salvar gráfico
    graf.get_figure().savefig(f"img/questoes_3/energia.png",bbox_inches="tight")
    plt.close(fig)

def pergunta_2(df_musica: pd.DataFrame): 
    """Gera um gráfico de dispersão entre a popularidade e o tempo da música

    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """     
    fig, graf = plt.subplots(figsize=(9,6))
    # Gráfico de dispersão entre a popularidade e o tempo da música
    sns.scatterplot(data=df_musica, x=df_musica['Popularidade'], y=df_musica['Tempo'], ax=graf)
    # calculo do coeficiente de correlação entre popularidade e tempo
    correlacao = df_musica['Popularidade'].corr(df_musica['Tempo'])
    #anota o valor do coeficiente de correlação no gráfico
    plt.text(60, 200,s=correlacao, horizontalalignment='left', 
             size='medium', color='black', weight='semibold')
    #eixos
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("Tempo", fontdict={"fontsize":13})
    #título
    graf.set_title("Popularidade x Tempo", fontdict={"fontsize":15})
    #salvar gráfico
    graf.get_figure().savefig(f"img/questoes_3/tempo.png",bbox_inches="tight")
    plt.close(fig)

def pergunta_3(df_musica: pd.DataFrame):
    """Gera um gráfico de dispersão entre a popularidade e a dançabilidade da música

    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    fig, graf = plt.subplots(figsize=(9,6))
    #gráfico de dispersão entre a popularidade e a dançabilidade da música
    sns.scatterplot(data=df_musica, x=df_musica['Popularidade'], y=df_musica['Dançabilidade'], ax=graf)
    #calcula o coeficiente de correlação entre popularidade e dançabilidade
    correlacao = df_musica['Popularidade'].corr(df_musica['Dançabilidade'])
    #anota o valor do coeficiente de correlação no gráfico
    plt.text(60, 0.7,s=correlacao, horizontalalignment='left',
             size='medium', color='black', weight='semibold')
    #eixos
    graf.set_xlabel("Popularidade", fontdict={"fontsize":13})
    graf.set_ylabel("Dancabilidade", fontdict={"fontsize":13})
    #título
    graf.set_title("Popularidade x Dancabilidade", fontdict={"fontsize":15})
    #salvar gráfico
    graf.get_figure().savefig(f"img/questoes_3/dancabilidade.png",bbox_inches="tight")