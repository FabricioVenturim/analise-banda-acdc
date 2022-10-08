Projeto
=======

interface
---------
Responsável por gerar o pdf com as respostas das perguntas e a estrutura do 
programa utilizando a biblioteca ``reportlab``. Para isso, são necessários dois csv:

* Csv com as informações de cada música dos álbuns da banda.
* Csv com as premiações dos álbuns da banda.

Ao rodar a interface, ela chamará os módulos do pacote ``analise_banda`` e produzirá o pdf no mesmo diretório.

create_dataset
--------------
Módulo responsável por criar o csv com as informações de cada música dos álbuns 
da banda. Para isso, ela utiliza a biblioteca ``spotipy`` e a biblioteca ``beautifulsoup``
para fazer o scraping do site `letras.com.br`.

exploratory_analysis
--------------------

Módulo responsável por responder as perguntas da etapa 2 do trabalho.
Mais informações sobre as perguntas: `https://github.com/barrafas/Monitoria_LP/blob/main/Aulas%20.py/Trabalho%20A1.md`

**Grupo 3 de perguntas:**
O spotify disponibilza vários dados sobre as músicas, como a popularidade,
energia da música, tempo, instrumentalidade, entre outros. Portanto achamos
interessante analisar esses dados e ver se conseguimos encontrar alguma relação
entre eles e a popularidade da música.

visualization
-------------
Módulo responsável por criar as visualizações.
Para isso, foram utilizadas as bibliotecas ``seaborn`` e ``matplotlib``.

cloud
-----
Módulo responsável por criar os World Cloud. Para isso,
foram utilizadas as bibliotecas ``matplotlib``, ``tracemalloc`` e ``wordcloud``.
