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
rgb_max = 255.
def blue_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    """
    função copiada de um exemplo do word cloud, não entedo direito mas funciona
    """
    return "hsl(215, 80%%, %d%%)" % random_state.randint(20, 30)
musicas = pd.read_csv("dataset_acdc1.csv", encoding= 'UTF-8')
musicas = musicas[['Álbum','Música','Letra']]
# musicas = musicas.set_index(['Álbum','Música'])
# back = musicas.loc['Back In Black','Back In Black']
# print(back['Letra'])
# print(ea.frequencia_titulo('Back In Black',back['Letra']))
def cloud_musicas():
    global musicas
    letras = np.unique(musicas['Letra'])
    mask = np.array(Image.open("forThoseAboutToRockMask.png"))
    mask_color = np.array(Image.open("forThoseAboutToRock.png"))
    cloud = WordCloud(width=600,height=600,max_words=1000,background_color='black',mask=mask)
    cloud.generate_from_frequencies(ea.contar_palavras(letras))
    image_colors = ImageColorGenerator(mask_color)
    # show
    fig, axes = plt.subplots(1, 3)
    axes[0].imshow(cloud, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(cloud.recolor(color_func=image_colors), interpolation="bilinear")
    axes[2].imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()
    
def cloud_titulo_musicas():
    global musicas
    letras = np.unique(musicas['Letra'])
    letras = ' '.join(letras)
    titulos = np.unique(musicas['Álbum'])
    titulos = ' '.join(titulos)
    mask = np.array(Image.open("logo_ACDC.png"))
    cloud = WordCloud(width=1920,height=1080,
                    background_color="black",
                    contour_width=3,max_words=1000)
    cloud.generate_from_frequencies(ea.frequencia_titulo(titulos, letras))
    plt.figure()
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def cloud_letras():
    global musicas
    musicas = np.unique(musicas['Letra'])
    mask = np.array(Image.open("logo_ACDC.png"))
    cloud = WordCloud(width=1920,height=1080,
                    background_color="black",
                    contour_color='gold',
                    contour_width=3,
                    mask=mask,max_words=1000)
    cloud.generate_from_frequencies(ea.contar_palavras(musicas))
    plt.figure()
    plt.imshow(cloud.recolor(color_func=blue_color_func, random_state=3), interpolation="bilinear")
    plt.axis("off")
print(cloud_letras())
plt.show()