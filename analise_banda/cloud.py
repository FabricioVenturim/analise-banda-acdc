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

def letras_azul(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    """
    função copiada de um exemplo do word cloud, não entedo direito mas funciona
    """
    return "hsl(215, 80%%, %d%%)" % random_state.randint(20, 30)
musicas = pd.read_csv("dataset_acdc1.csv", encoding= 'UTF-8')
musicas = musicas[['Álbum','Música','Letra']]

def cloud_acdc(palavras: list[str], background: str ='black', contour: str = 'gold') -> None:
    mask = np.array(Image.open("logo_ACDC.png"))
    cloud = WordCloud(
                    background_color=background,
                    contour_color=contour,
                    contour_width=3,
                    mask=mask,max_words=1000)
    return cloud.generate_from_frequencies(ea.contar_palavras(palavras))

musicas = np.unique(musicas['Letra'])

cloud = cloud_acdc(musicas)
print(type(cloud))
plt.figure()
plt.imshow(cloud.recolor(color_func=letras_azul, random_state=3), interpolation="bilinear")
plt.axis("off")

plt.show()