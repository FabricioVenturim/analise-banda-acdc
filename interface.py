from analise_banda import *
import pandas as pd
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

#variáveis globais:
margem = 50
linha = 750

def fontes():
    """Função que registrará as fontes que serão utilizadas na criação do pdf
    """    
    # Registra font family
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    # Registra fontfamily
    registerFontFamily('Vera',normal='Vera',bold='VeraBd')
    

def printar_msg(pdf: canvas.Canvas, msg: str):
    """Função para escrever frases simples no pdf, atualizando o valor das linhas.

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param msg: mensagem que se deseja escrever no pdf
    :type msg: str
    """    
    global margem
    global linha
    pdf.drawString(margem,linha,msg)
    linha-=15


def printar_primeira_questao_grupo_1(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf as músicas mais famosas e menos famosas de cada álbum, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as músicas mais populares e menos populares de cada álbum
    :type df_musica: pd.DataFrame
    """   

    global margem
    global linha
    popularidade = exploratory_analysis.popularidade_album(df_musica) #Pega o df da popularidade
    visualization.grafico_popularidade_album(popularidade) #Vai salvar os gráficos na pasta img
    
    #pegar cada álbum
    albuns = popularidade["Álbum"].unique()
    
    index_img = 0
    for album in albuns:
        musics_album = popularidade.loc[popularidade["Álbum"] == album]
        
        #Músicas mais famosas:
        printar_msg(pdf, f"As músicas mais famosas do Álbum {album} são:")
        for index in range(0, 3):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Popularidade']})")
            linha -= 15

        #Músicas menos famosas:
        printar_msg(pdf, f'As músicas menos famosas do Álbum "{album}" são:')
        for index in range(3, 6):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Popularidade']})")
            linha -= 15

        #plotar as imagens (como quero duas imagens por página, caso o index seja impar, ele quebra a página)
        if index_img%2 == 0:
            pdf.drawImage(f"img/questao_1.1/1atividade-{index_img}.png", margem+50, 220, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"img/questao_1.1/1atividade-{index_img}.png", margem+50, -140, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            pdf.showPage()
            linha = 720
            #Título de toda página nova
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_segunda_questao_grupo_1(pdf: canvas.Canvas, df_musica:pd.DataFrame):
    """Função que escreve no pdf as músicas mais famosas e menos famosas de cada álbum, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as músicas mais longas e mais curtas de cada álbum
    :type df_musica: pd.DataFrame
    """     

    global margem
    global linha
    duracao = exploratory_analysis.tamanho_musica_album(df_musica) #Pega o df da duração
    visualization.grafico_duracao_album(duracao) #Vai salvar os gráficos na pasta
    #pegar cada álbum
    albuns = duracao["Álbum"].unique()
    
    index_img = 0
    for album in albuns:
        musics_album = duracao.loc[duracao["Álbum"] == album]
        
        #Músicas mais longas:
        printar_msg(pdf, f'As músicas mais longas do Álbum "{album}" são:')
        for index in range(0, 3):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Duração']})")
            linha -= 15
        
        #Músicas mais curtas:
        printar_msg(pdf, f'As músicas mais curtas do Álbum "{album}" são:')
        for index in range(3, 6):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Duração']})")
            linha -= 15

        #plotar as imagens (como quero duas imagens por página, caso o index seja impar, ele quebra a página)
        if index_img%2 == 0:
            pdf.drawImage(f"img/questao_1.2/2atividade-{index_img}.png", margem+50, 225, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"img/questao_1.2/2atividade-{index_img}.png", margem+50, -135, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            pdf.showPage()
            linha = 725
            #Título de toda página nova
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_terceira_questao_grupo_1(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf as músicas mais famosas e menos famosas de toda banda, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as músicas mais famosas e menos famosas de toda banda
    :type df_musica: pd.DataFrame
    """     
    
    global margem
    global linha
    popularidade = exploratory_analysis.popularidade_geral(df_musica) #Pega o df da popularidade
    visualization.grafico_popularidade_geral(popularidade) #Vai salvar os gráficos na pasta
    
    #Músicas mais populares
    printar_msg(pdf, f"As músicas mais populares da banda AC/DC são:")
    for index in range(0, 3):
        pdf.drawString(margem+15,linha,f"-{popularidade.iloc[index]['Música']}({popularidade.iloc[index]['Popularidade']})")
        linha -= 15
    
    #Músicas menos populares
    printar_msg(pdf, f'As músicas menos famosas da banda AC/DC são:')
    for index in range(3, 6):
        pdf.drawString(margem+15,linha,f"-{popularidade.iloc[index]['Música']}({popularidade.iloc[index]['Popularidade']})")
        linha -= 15

    #plotar a imagem  
    pdf.drawImage(f"img/questao_1.3/3atividade.png", margem+50, 200, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 


def printar_quarta_questao_grupo_1(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf as músicas mais longas e mais curtas de toda banda, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as músicas mais longas e mais curtas de toda banda
    :type df_musica: pd.DataFrame
    """     

    global margem
    global linha
    duracoes_gerais = exploratory_analysis.tamanho_musica_geral(df_musica) #Pega o df da duração
    visualization.grafico_tamanho_musica_geral(duracoes_gerais) #Vai salvar os gráficos na pasta
    
    #Música mais longas
    printar_msg(pdf, f"As músicas mais longas da banda AC/DC são:")
    for index in range(0, 3):
        pdf.drawString(margem+15,linha,f"-{duracoes_gerais.iloc[index]['Música']}({duracoes_gerais.iloc[index]['Duração']})")
        linha -= 15
    
    #Música mais curtas
    printar_msg(pdf, f'As músicas mais curtas da banda AC/DC são:')
    for index in range(3, 6):
        pdf.drawString(margem+15,linha,f"-{duracoes_gerais.iloc[index]['Música']}({duracoes_gerais.iloc[index]['Duração']})")
        linha -= 15
    
    #plotar a imagem 
    pdf.drawImage(f"img/questao_1.4/4atividade.png", margem+50, 200, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 


def printar_quinta_questao_grupo_1(pdf: canvas.Canvas, df_musica_premiacao: pd.DataFrame):
    """Função que escreve no pdf os álbuns mais premiados da banda, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com os álbuns mais premiados da banda
    :type df_musica: pd.DataFrame
    """     

    global margem
    global linha
    premiacoes_gerais = exploratory_analysis.premiacoes_album(df_musica_premiacao) #Pega o df das premiações
    visualization.grafico_premiacoes_album(premiacoes_gerais) #Vai salvar os gráficos na pasta
    
    #As 3 músicas mais premiadas e seus prêmios
    printar_msg(pdf, f"As músicas mais longas da banda AC/DC são:")
    for index in range(0, 3):
        pdf.drawString(margem+15,linha,f"-{premiacoes_gerais.iloc[index]['Álbum']}: ")
        linha -= 15
        pdf.drawString(margem+30,linha,f"- Disco de Prata: {premiacoes_gerais.iloc[index]['Quantidade']}.")
        linha -= 15
        pdf.drawString(margem+30,linha,f"- Disco de Ouro: {premiacoes_gerais.iloc[index+3]['Quantidade']}.")
        linha -= 15
        pdf.drawString(margem+30,linha,f"- Disco de Platina: {premiacoes_gerais.iloc[index+6]['Quantidade']}.")
        linha -= 15
        pdf.drawString(margem+30,linha,f"- Disco de Diamante: {premiacoes_gerais.iloc[index+9]['Quantidade']}.")
        linha -= 15
    
    #plotar a imagem 
    pdf.drawImage(f"img/questao_1.5/graf_premiacoes.png", margem+50, 75, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 

def printar_sexta_questao_grupo_1(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a correlação entre as variáveis popularidade e duração das músicas da banda, bem como seus gráficos
    
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as colunas de poplaridade e duração das músicas da banda
    :type df_musica: pd.DataFrame
    """     
    
    global margem
    global linha
    correlacao = exploratory_analysis.relacao_duracao_popularidade(df_musica) #Pega o df da correlação
    visualization.grafico_corresp(correlacao) #Vai salvar os gráficos na pasta
    visualization.grafico_plot(df_musica) #Vai salvar os gráficos na pasta

    #Printar a correlação
    printar_msg(pdf, f"A correlação entre a duração das músicas e a popularidade é de {correlacao['Popularidade'].iloc[1]}")
    printar_msg(pdf, f"Logo, apesar de ter uma leve correlação inversa, podemos dizer que não há correlação.")

    #plotar as imagens 
    pdf.drawImage(f"img/questao_1.6/corresp.png", margem+50, 270, width=400, preserveAspectRatio=True, mask='auto')
    pdf.drawImage(f"img/questao_1.6/plot.png", margem+50, -25, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)

def printar_primeira_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """    
    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_1(df_musica)
    #pega cada paravra e sua quantidade
    for palavra, quant in palavras_mais_comuns.items():
        pdf.drawString(margem,linha, f"{palavra}: {quant}.")
        linha -= 15
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

def printar_segunda_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 2 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_2(df_musica)
    #pega cada paravra e sua quantidade
    for key, value in palavras_mais_comuns.items():
        pdf.drawString(margem,linha, f"{key}: {value}.")
        linha -= 15
        if linha < 80: #Estamos mostrando apenas as palavras mais comuns
            break
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
    pdf.showPage()
    
    #Colocar o world cloud no pdf
    cloud.cloud_1(df_musica)
    pdf.drawImage(f"img/questao_2.2/tagcloud_musicas.png", margem, 500, width=500, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

def printar_terceira_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   

    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_3(df_musica)
    quant_album_pag = 5 #Quantidade máxima de álbuns que cabe por página
    #pega cada album e sua lista de palavras
    for album, palavras in palavras_mais_comuns.items():
        pdf.drawString(margem,linha,f"Palavras mais comuns no álbum {album}:")
        linha -= 15
        quant = 5
        #pega cada paravra e sua quantidade
        for palavra, quantidade in palavras.items():
            if quant < 0:
                break
            pdf.drawString(margem,linha,f"{palavra}: {quantidade}")
            linha -= 15
            quant -= 1
        linha -= 15
        quant_album_pag -= 1
        #Se a quantidade ficar abaixo de 0, ele quebra a página e vai repetindo 
        if quant_album_pag < 0:
            quant_album_pag = 5
            pdf.showPage()
            linha = 720
            #Título de toda página nova
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_quarta_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    
    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_4(df_musica)
    #pega cada paravra e sua quantidade
    for palavra, quant in palavras_mais_comuns.items():
        pdf.drawString(margem,linha, f"{palavra}: {quant}.")
        linha -= 15
        if linha < 80: #Estamos mostrando apenas as palavras mais comuns
            break
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
    pdf.showPage()
    
    #Coloca o world cloud na página
    cloud.cloud_2(df_musica)
    pdf.drawImage(f"img/questao_2.4/tagcloud_letras.png", margem, 500, width=500, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

def printar_quinta_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    
    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_5(df_musica)
    #pega cada paravra e sua quantidade
    for palavra, quant in palavras_mais_comuns.items():
        pdf.drawString(margem,linha, f"{palavra}: {quant}.")
        linha -= 15 #Só queremos as mais comuns
    linha -= 15 
    printar_msg(pdf, "O tema dos títulos aparecem muito nas letras dos álbuns,")
    printar_msg(pdf, "como as palavras got, rock, back, let e want.")

    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

def printar_sexta_questao_grupo_2(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    
    global margem
    global linha

    palavras_mais_comuns = exploratory_analysis.pergunta2_6(df_musica)
    pdf.drawString(margem, linha,"As palavras do título aparecem nas letras: ")
    linha -= 15
    #pega cada paravra e sua quantidade
    for palavra, quant in palavras_mais_comuns.items():
        pdf.drawString(margem, linha,f"{palavra}: {quant}")
        linha -= 15
        if linha < 40:
            pdf.showPage()
            linha = 720
            #Título de toda página nova
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

    linha -= 15 
    printar_msg(pdf, "O tema dos títulos das músicas aparecem muito nas letras dos álbuns.")

    #Coloca o would cloud na página
    cloud.cloud_3(df_musica)
    pdf.drawImage(f"img/questao_2.6/tagcloud_musicas_letras.png", margem, 325, width=500, preserveAspectRatio=True, mask='auto')

    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
   
#Grupo 3 de questões

def printar_primeira_questao_grupo_3(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   

    global margem
    global linha

    visualization.pergunta_1(df_musica)
    printar_msg(pdf, "Como a correlação é de -0,14, temos que não há correlação.")
    pdf.drawImage(f"img/questoes_3/energia.png", margem+50, 250, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")


def printar_segunda_questao_grupo_3(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    
    global margem
    global linha

    visualization.pergunta_2(df_musica)
    printar_msg(pdf, "Como a correlação é de 0,11, temos que não há correlação.")
    pdf.drawImage(f"img/questoes_3/Tempo.png", margem+50, 250, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

def printar_terceira_questao_grupo_3(pdf: canvas.Canvas, df_musica: pd.DataFrame):
    """Função que escreve no pdf a pergunta 1 do grupo de perguntas 2

    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """   
    
    global margem
    global linha

    visualization.pergunta_3(df_musica)
    printar_msg(pdf, "Como a correlação é de 0,25, temos que não há correlação.")
    pdf.drawImage(f"img/questoes_3/dancabilidade.png", margem+50, 250, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")

    
def printar_modelo_questão(pdf: canvas.Canvas, enunciado: str, funcao, database: pd.DataFrame):
    """Função responsável por gerar um modelo para escrever as questões no pdf
    :param pdf: pdf a ser editado
    :type pdf: canvas.Canvas
    :param enunciado: questão a ser imprimida no pdf
    :type enunciado: str
    :param funcao: função responsável por imprimir determinada questão
    :type funcao: function
    :param df_musica: DataFrame com as informações da banda AC/DC gerados no create_dataset
    :type df_musica: pd.DataFrame
    """    
    
    global coluna
    global linha
    
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, enunciado)
    pdf.setFont('Vera', 12)
    linha-=15
    funcao(pdf, database)
    pdf.showPage()


def gera_pdf(df_musica: pd.DataFrame, df_musica_premiacao: pd.DataFrame):
    """Função responsável por gerar o pdf com as perguntas respondidas

    :param df_musica: DataFrame com as informações da discografia da banda AC/DC
    :type df_musica: pd.DataFrame
    :param csv_premiacoes: DataFrame com as premiações dos álbuns da banda AC/DC
    :type df_musica_premiacao: pd.DataFrame
    """    

    # margem e linha da localização da plotagem de texto
    global margem
    global linha

    #Configurando a página
    pdf = canvas.Canvas("Analise_acdc.pdf", pagesize=A4)
    fontes() #chama a função com as fontes que serão utilizadas

    #Titulo
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
    
    #Grupo 1 de perguntas
    pdf.setFont('VeraBd', 12)
    pdf.drawString(250,780,"Grupo 1 de Perguntas")
    
    #Pergunta 1
    printar_modelo_questão(pdf, "Pergunta 1) Músicas mais ouvidas e músicas menos ouvidas por Álbum: ", printar_primeira_questao_grupo_1, df_musica)

    #Pergunta 2
    printar_modelo_questão(pdf, "Pergunta 2) Músicas mais longas e músicas mais curtas por Álbum:", printar_segunda_questao_grupo_1, df_musica)

    #Pergunta 3
    printar_modelo_questão(pdf, "Pergunta 3) Músicas mais ouvidas e músicas menos ouvidas da banda", printar_terceira_questao_grupo_1, df_musica)

    #Pergunta 4
    printar_modelo_questão(pdf, "Pergunta 4) Músicas mais longas e músicas mais curtas da banda", printar_quarta_questao_grupo_1, df_musica)

    #Pergunta 5
    printar_modelo_questão(pdf, "Pergunta 5) Álbuns mais premiados:", printar_quinta_questao_grupo_1, df_musica_premiacao)

    #Pergunta 6
    printar_modelo_questão(pdf, "Pergunta 6) Álbuns mais premiados:", printar_sexta_questao_grupo_1, df_musica)

    #Grupo 2 de perguntas
    pdf.setFont('VeraBd', 12)
    pdf.drawString(250,780,"Grupo 2 de Perguntas")
    
    #Pergunta 1
    printar_modelo_questão(pdf, "Pergunta 1) Quais são as palavras mais comuns nos títulos dos Álbuns?", printar_primeira_questao_grupo_2, df_musica)
    
    #Pergunta 2
    printar_modelo_questão(pdf, "Pergunta 2) Quais são as palavras mais comuns nos títulos das músicas?", printar_segunda_questao_grupo_2, df_musica)

    #Pergunta 3
    printar_modelo_questão(pdf, "Pergunta 3) Quais são as palavras mais comuns, por Álbum?", printar_terceira_questao_grupo_2, df_musica)

    #Pergunta 4
    printar_modelo_questão(pdf, "Pergunta 4) Quais são as palavras mais comuns, em toda a discografia?", printar_quarta_questao_grupo_2, df_musica )

    #Pergunta 5
    printar_modelo_questão(pdf, "Pergunta 5) O título de um álbum é tema recorrente nas letras?", printar_quinta_questao_grupo_2, df_musica)

    #Pergunta 6
    printar_modelo_questão(pdf, "Pergunta 6) O título de uma música é tema recorrente nas letras?", printar_sexta_questao_grupo_2, df_musica)

    #Grupo 3 de perguntas
    pdf.setFont('VeraBd', 12)
    pdf.drawString(250,780,"Grupo 3 de Perguntas")
    
    #Pergunta 1
    printar_modelo_questão(pdf, "Pergunta 1) Há correlação entre Popularidade e a Energia das músicas?", printar_primeira_questao_grupo_3, df_musica)


    #Pergunta 2
    printar_modelo_questão(pdf, "Pergunta 2) Há correlação entre Popularidade e a Tempo  das músicas?", printar_segunda_questao_grupo_3, df_musica)
   

    #Pergunta 3
    printar_modelo_questão(pdf, "Pergunta 3) Há correlação entre Popularidade e a Dançabilidade das músicas?", printar_terceira_questao_grupo_3, df_musica)

    pdf.save()

def interface(csv_musica: str, csv_premiacoes: str):
    """Função que receberá dois csv e irá convertê-los em dois DataFrames para as demais funções

    :param csv_musica: Caminho do csv com as músicas da banda
    :type csv_musica: str
    :param csv_premiacoes: Caminho do csv com as premiações de cada álbum da banda
    :type csv_premiacoes: str
    """    
    try: 
        df_musica = pd.read_csv(csv_musica)
        df_musica_premiacao = pd.read_csv(csv_premiacoes)
    except FileNotFoundError:
        print("Desculpe, o arquivo que você passou não foi encontrado")
    else:
        gera_pdf(df_musica, df_musica_premiacao)

