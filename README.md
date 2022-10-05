<h1 align="center">Analise Banda AC/DC - A1 LP</h1>

## Repositório de criação do banco de dados da discografia da banda AC/DC e análise exploratória e visualização dos dados.

### Como rodar?

Passo 1: utilize o comando a seguir para instalar as bibliotecas necessárias para o funcionamento do programa: 

```
pip install -r requirements.txt
```

Passo 2: Para executar o programa, é necessário rodar o arquivo main.py da pasta. Nele há apenas um código que chamará a função interface do módulo.

## Projeto:

### interface:

Responsável por gerar o pdf com as respostas das perguntas e a estrutura do programa utilizando a biblioteca ```reportlab```. Para isso, são necessários dois csv:

* Csv com as informações de cada música dos álbuns da banda.
* Csv com as premiações dos álbuns da banda. 

Ao rodar a interface, ela chamará os módulos do pacote ```analise_banda``` e produzirá o pdf no mesmo diretório.

### create_dataset:

Módulo responsável por criar o csv com as informações de cada música dos álbuns da banda. Para isso, ela utiliza a biblioteca ```spotipy``` e a biblioteca ```beautifulsoup``` para fazer o scraping do site letras.com.br.

### exploratory_analysis:

Módulo responsável por responder o grupo 1 de perguntas:

* Músicas mais ouvidas e músicas menos ouvidas por Álbum

* Músicas mais longas e músicas mais curtas por Álbum

* Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]

* Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]

* Álbuns mais premiados [https://twiftnews.com/lifestyle/top-6-most-prestigious-music-awards/]

* Existe alguma relação entre a duração da música e sua popularidade?

### visualization:

Módulo responsável por criar as visualizações do grupo de perguntas 1. Para isso, foram utilizadas as bibliotecas ```seaborn``` e ```matplotlib```.
