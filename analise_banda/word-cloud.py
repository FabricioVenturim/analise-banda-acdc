import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import exploratory_analysis as ea
from os import path
from PIL import Image

musicas = pd.read_csv("dataset_acdc.csv", encoding= 'UTF-8')

musicas = musicas[['Álbum','Música','Letra']]
letras = np.unique(musicas['Letra'])
print(ea.contar_palavras(letras))
mask = np.array(Image.open("logo_ACDC.png"))
cloud = WordCloud(width=1920,height=1080,
                  background_color="black",
                  contour_width=3,
                  mask=mask,max_words=1000)
cloud.generate_from_frequencies(ea.contar_palavras(letras))
plt.figure()
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()
