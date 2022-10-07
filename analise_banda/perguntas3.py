from numpy import size
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')
    """O spotify disponibilza vários dados sobre as músicas, 
    como a popularidade, energia da música, tempo, instrumentalidade, entre outros.
    Portanto achamos interessante analisar esses dados e ver se conseguimos encontrar
    Alguma relação entre eles e a popularidade da música."""
    
    fig, graf = plt.subplots(figsize=(9,6))
    # Gráfico de dispersão entre a popularidade e a energia da música
    sns.scatterplot(data=musicas, x=musicas['Popularidade'],
                    y=musicas['Energia'], ax=graf)
    plt.ticklabel_format(style="plain", axis="y")
    # calculo do coeficiente de correlação entre popularidade e energia
    correlacao = musicas['Popularidade'].corr(musicas['Energia'])
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
    
    fig, graf = plt.subplots(figsize=(9,6))
    # Gráfico de dispersão entre a popularidade e o tempo da música
    sns.scatterplot(data=musicas, x=musicas['Popularidade'],
                    y=musicas['Tempo'], ax=graf)
    # calculo do coeficiente de correlação entre popularidade e tempo
    correlacao = musicas['Popularidade'].corr(musicas['Tempo'])
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
    
    fig, graf = plt.subplots(figsize=(9,6))
    #gráfico de dispersão entre a popularidade e a dançabilidade da música
    sns.scatterplot(data=musicas, x=musicas['Popularidade'],
                    y=musicas['Dançabilidade'], ax=graf)
    #calcula o coeficiente de correlação entre popularidade e dançabilidade
    correlacao = musicas['Popularidade'].corr(musicas['Dançabilidade'])
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