from analise_banda import *
import pandas as pd
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont


df_musica = pd.read_csv("dataset_acdc.csv")
margem = 50
linha = 750

def printar_msg(pdf, msg):
    global margem
    global linha
    pdf.drawString(margem,linha,msg)
    linha-=15

def fontes():
    global margem
    global linha
    # Registered font family
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    # Registered fontfamily
    registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',boldItalic='VeraBI')
    

def printar_primeira_questão(pdf):
    global margem
    global linha
    popularidade = exploratory_analysis.popularidade_album(df_musica)
    visualization.grafico_popularidade_album(popularidade) #Vai salvar os gráficos na pasta
    
    #pegar cada álbum
    albuns = popularidade["Álbum"].unique()
    
    index_img = 0
    for album in albuns:
        musics_album = popularidade.loc[popularidade["Álbum"] == album]
        printar_msg(pdf, f"As músicas mais famosas do Álbum {album} são:")
        for index in range(0, 3):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Popularidade']})")
            linha -= 15
        
        printar_msg(pdf, f'As músicas menos famosas do Álbum "{album}" são:')
        for index in range(3, 6):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Popularidade']})")
            linha -= 15

        if index_img%2 == 0:
            pdf.drawImage(f"img/questao_1.1/1atividade-{index_img}.png", margem+50, 220, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"img/questao_1.1/1atividade-{index_img}.png", margem+50, -140, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            pdf.showPage()
            linha = 720
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_segunda_questão(pdf):
    global margem
    global linha
    duracao = exploratory_analysis.tamanho_musica_album(df_musica)
    visualization.grafico_duracao_album(duracao) #Vai salvar os gráficos na pasta
    #pegar cada álbum
    albuns = duracao["Álbum"].unique()
    
    index_img = 0
    for album in albuns:
        musics_album = duracao.loc[duracao["Álbum"] == album]
        printar_msg(pdf, f'As músicas mais longas do Álbum "{album}" são:')
        for index in range(0, 3):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Duração']})")
            linha -= 15
        
        printar_msg(pdf, f'As músicas mais curtas do Álbum "{album}" são:')
        for index in range(3, 6):
            pdf.drawString(margem+15,linha,f"-{musics_album.iloc[index]['Música']}({musics_album.iloc[index]['Duração']})")
            linha -= 15

        if index_img%2 == 0:
            pdf.drawImage(f"img/questao_1.2/2atividade-{index_img}.png", margem+50, 225, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"img/questao_1.2/2atividade-{index_img}.png", margem+50, -135, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            pdf.showPage()
            linha = 725
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_terceira_questão(pdf):
    pass

def interface():
    global margem
    global linha
    #Configurando a página
    pdf = canvas.Canvas("Analise_acdc.pdf", pagesize=A4)
    fontes()

    #Titulo
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
    
    #Pergunta 1
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 1) Músicas mais ouvidas e músicas menos ouvidas por Álbum: ")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_primeira_questão(pdf)
    pdf.showPage()

    #Pergunta 2
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 2) Músicas mais longas e músicas mais curtas por Álbum:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_segunda_questão(pdf)

    #Pergunta 2
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 3) Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_terceira_questão(pdf)


    pdf.save()

interface()