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




def cloud_acdc(palavras: list[str], background: str ='black', contour: str = 'gold', hue_letras: int = 215, saturacao_letras: int = 80) -> WordCloud:
    """ Cria um word cloud com a logo do ACDC

    :param palavras: lista com os textos utilizados para gerar o wordcloud
    :type palavras: list[str]
    :param background: cor do plano de fundo do wordcloud, defaults to 'black'
    :type background: str, optional
    :param contour: cor da borda da logo, defaults to 'gold'
    :type contour: str, optional
    :param hue_letras: tonalidade das letras
    :type hue_letras: int, optional 
    :param saturacao_letras: saturacao das letras
    type saturacao_letras: int, optional
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
        return f"hsl({hue_letras}, {saturacao_letras}%%, %d%%)" % random_state.randint(30, 50)
    mask = np.array(Image.open("logo_ACDC.png"))
    cloud = WordCloud(
                    background_color=background,
                    contour_color=contour,
                    contour_width=3,
                    mask=mask,max_words=1000)
    cloud = cloud.generate_from_frequencies(ea.contar_palavras(palavras))
    cloud = cloud.recolor(color_func=letras_coloridas, random_state=3)
    return cloud



musicas = pd.read_csv("dataset_acdc1.csv", encoding= 'UTF-8')
musicas = musicas[['Álbum','Música','Letra']]
musicas = np.unique(musicas['Letra'])
cloud = cloud_acdc(musicas)

plt.figure()
plt.imshow(cloud)
plt.axis("off")

plt.show()