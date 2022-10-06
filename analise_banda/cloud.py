import random
from tracemalloc import stop
import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
import exploratory_analysis as ea
from os import path
from PIL import Image




def cloud_acdc(palavras: dict[str, int], mask: np.ndarray,background: str ='black',
               contour_width: int = 3, contour: str = 'gold',
               hue_letras: int = 215 ,saturacao_letras: int = 80, 
               clareza_min_letras: int =30,
               clareza_max_letras: int = 50)-> WordCloud:
    """ Cria um word cloud com a logo do ACDC

    :param palavras: dicionario com a frequencia de cada palavra
    :type palavras: dict[str, int]
    :param mask: mascara para criação do wordcloud
    :type mask: ndarray
    :param background: cor do plano de fundo do wordcloud, defaults to 'black'
    :type background: str, optional
    :param contour: cor da borda da logo, defaults to 'gold'
    :type contour: str, optional
    :param hue_letras: tonalidade das letras, defaults to 213
    :type hue_letras: int, optional 
    :param saturacao_letras: saturacao das letras, defaults to 0
    :type saturacao_letras: int, optional
    :param clareza_min_letras: clareza mínima das letras, defaults to 60
    :type clareza_min_letras: int, optional 
    :param clareza_max_letras: clareza maxima das letras, defaults to 100
    :param contour_width: grossura da borda da logo, defaults to 3
    :type contour_widdth: int, optional
    :type clareza_max_letras: int, optional
    :return: retorna a imagem do wordcloud
    :rtype: WordCloud
    """
    def letras_coloridas(word, font_size, position, orientation, random_state=None,
                    **kwargs):
        """
        função copiada de um exemplo do word cloud, não entedo direito mas funciona.
        A intenção principal da função é criar um range de cores aletórias que cada
        palavra do wordcloud pode assumir.
        """
        return f"hsl({hue_letras}, {saturacao_letras}%%, %d%%)" % random_state.randint(
            clareza_min_letras, clareza_max_letras)
    cloud = WordCloud(
                    background_color=background,
                    contour_color=contour,
                    contour_width=contour_width,
                    mask=mask,max_words=1000)
    cloud = cloud.generate_from_frequencies(palavras)
    cloud = cloud.recolor(color_func=letras_coloridas, random_state=3)
    return cloud


if __name__ == '__main__':
    musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')
    musicas = musicas[['Álbum','Música','Letra']]
    nome_musicas = np.unique(musicas['Música'])
    cloud = cloud_acdc(ea.contar_palavras(nome_musicas), np.array(Image.open("acdc_logo2.png")),
                    'black', 5,'white',5, 80,
                    clareza_min_letras=40, clareza_max_letras= 50)
    plt.figure()
    plt.imshow(cloud)
    plt.axis("off")

    plt.savefig(f"img/questao_2.4/tagcloud_letras.png",bbox_inches="tight")
    letras = np.unique(musicas['Letra'])
    cloud = cloud_acdc(ea.frequencia_titulo(' '.join(nome_musicas),' '.join(letras)),
                    np.array(Image.open("logo_ACDC.png")))
    plt.figure()
    plt.imshow(cloud)
    plt.axis("off")

    plt.savefig(f"img/questao_2.6/tagcloud_musicas_letras.png",bbox_inches="tight")
    cloud = cloud_acdc(ea.contar_palavras(nome_musicas),
                    np.array(Image.open("acdc_logo2.png")),'white', 5,'gold',
                    5, 80,clareza_min_letras=40, clareza_max_letras= 50)
    plt.figure()
    plt.imshow(cloud)
    plt.axis("off")
    plt.savefig(f"img/questao_2.2/tagcloud_musicas.png",bbox_inches="tight")