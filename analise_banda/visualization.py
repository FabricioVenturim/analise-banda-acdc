import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import exploratory_analysis

#Gráficos da questão 1
def grafico_popularidade_album(df_albuns):
    #Transforma o dicionario em dataframe
    albuns = df_albuns["Álbum"].unique()
    
    index = 0
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

        graf.get_figure().savefig(f"img/questao_1.1/1atividade-{index}.png",bbox_inches="tight")
        index += 1
        plt.close()

#Gráficos da questão 2
def grafico_duracao_album(df_albuns):
    albuns = df_albuns["Álbum"].unique()
    
    index = 0
    for album in albuns:
        musics_album = df_albuns.loc[df_albuns["Álbum"] == album]
        
        #criando uma figure, axes, alterando tamanho
        fig, graf = plt.subplots(figsize=(9,6))
        #criando o gráfico de barras
        sns.barplot(data=musics_album, y="Música", x="Duração", ax=graf, hue = "Tipo Duração" )
        #adicionando título
        graf.set_title(f"Duração das Músicas do Álbum {album}", fontdict={'fontsize':15})
        #mudando nome e tamanho do label x e y
        graf.set_xlabel('Duração (milissegundos)', fontdict={'fontsize':13})
        graf.set_ylabel("")
        #formatando legenda 
        graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

        graf.get_figure().savefig(f"img/questao_1.2/2atividade-{index}.png",bbox_inches='tight')
        index += 1
        plt.close()

#Gráficos da questão 3
def grafico_popularidade_geral(df_albuns):
    
    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_albuns, y="Música", x="Popularidade", ax=graf, hue = "Tipo Popularidade" )
    #adicionando título
    graf.set_title("Popularidade das Músicas da banda AC/DC", fontdict={'fontsize':15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel('Popularidade', fontdict={'fontsize':13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    graf.get_figure().savefig(f"img/questao_1.3/3atividade.png",bbox_inches='tight')
    plt.close()

#Gráficos da questão 4
def grafico_tamanho_musica_geral(df_musicas):
    #Transforma o dicionario em dataframe
    df_musicas["Música"].mask((df_musicas["Música"]=="Let There Be Rock") & (df_musicas["Duração"]==736133), other = "Let There Be Rock (LIVE)" , inplace=True)    

    #criando uma figure, axes, alterando tamanho
    fig, graf = plt.subplots(figsize=(9,6))
    #criando o gráfico de barras
    sns.barplot(data=df_musicas, y="Música", x="Duração", ax=graf, hue = "Tipo Duração" )
    #adicionando título
    graf.set_title("Duração das Músicas da banda AC/DC", fontdict={'fontsize':15})
    #mudando nome e tamanho do label x e y
    graf.set_xlabel("Popularidade", fontdict={'fontsize':13})
    graf.set_ylabel("")
    #formatando legenda 
    graf.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    graf.get_figure().savefig(f"img/questao_1.4/4atividade.png",bbox_inches='tight')
    plt.close()

#Gráficos da questão 6
def grafico_corresp(corr_df):
    fig, graf = plt.subplots(figsize=(9,6))
    sns.heatmap(corr_df, annot=True, ax=graf)
    #adicionando título
    graf.set_title("Correlação entre Popularidade das músicas e sua Duração", fontdict={'fontsize':15})
    #salvar
    graf.get_figure().savefig(f"img/questao_1.6/corresp.png",bbox_inches='tight')

def grafico_plot(df):
    fig, graf = plt.subplots(figsize=(9,6))
    sns.scatterplot(df, x=df["Popularidade"], y=df["Duração"], ax=graf)
    plt.ticklabel_format(style='plain', axis='y')
    #adicionando título
    graf.set_title("Duração das músicas por Popularidade", fontdict={'fontsize':15})
    #eixos
    graf.set_xlabel("Popularidade", fontdict={'fontsize':13})
    graf.set_ylabel("Duração em milissegundos", fontdict={'fontsize':13})
    #salvar gráfico
    graf.get_figure().savefig(f"img/questao_1.6/plot.png",bbox_inches='tight')