import exploratory_analysis
import visualization
import pandas as pd
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont


df_musica = pd.read_csv("dataset_acdc.csv")
df_musica_premiacao = pd.read_csv("premiacoes.csv")
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
            pdf.drawImage(f"../img/questao_1.1/1atividade-{index_img}.png", margem+50, 220, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"../img/questao_1.1/1atividade-{index_img}.png", margem+50, -140, width=400, preserveAspectRatio=True, mask='auto')
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
            pdf.drawImage(f"../img/questao_1.2/2atividade-{index_img}.png", margem+50, 225, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            linha -= 230
        else:
            pdf.drawImage(f"../img/questao_1.2/2atividade-{index_img}.png", margem+50, -135, width=400, preserveAspectRatio=True, mask='auto')
            index_img += 1
            pdf.showPage()
            linha = 725
            pdf.setFont('VeraBd', 15)
            pdf.drawString(150,800,"Análise da Discografia da banda AC/DC")
            pdf.setFont("Vera", 12)

def printar_terceira_questão(pdf):
    global margem
    global linha
    popularidade = exploratory_analysis.popularidade_geral(df_musica)
    visualization.grafico_popularidade_geral(popularidade) #Vai salvar os gráficos na pasta
    printar_msg(pdf, f"As músicas mais populares da banda AC/DC são:")
    for index in range(0, 3):
        pdf.drawString(margem+15,linha,f"-{popularidade.iloc[index]['Música']}({popularidade.iloc[index]['Popularidade']})")
        linha -= 15
        
    printar_msg(pdf, f'As músicas menos famosas da banda AC/DC são:')
    for index in range(3, 6):
        pdf.drawString(margem+15,linha,f"-{popularidade.iloc[index]['Música']}({popularidade.iloc[index]['Popularidade']})")
        linha -= 15
    pdf.drawImage(f"../img/questao_1.3/3atividade.png", margem+50, 200, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 

def printar_quarta_questão(pdf):
    global margem
    global linha
    duracoes_gerais = exploratory_analysis.tamanho_musica_geral(df_musica)
    visualization.grafico_tamanho_musica_geral(duracoes_gerais) #Vai salvar os gráficos na pasta
    printar_msg(pdf, f"As músicas mais longas da banda AC/DC são:")
    for index in range(0, 3):
        pdf.drawString(margem+15,linha,f"-{duracoes_gerais.iloc[index]['Música']}({duracoes_gerais.iloc[index]['Duração']})")
        linha -= 15
        
    printar_msg(pdf, f'As músicas mais curtas da banda AC/DC são:')
    for index in range(3, 6):
        pdf.drawString(margem+15,linha,f"-{duracoes_gerais.iloc[index]['Música']}({duracoes_gerais.iloc[index]['Duração']})")
        linha -= 15
    pdf.drawImage(f"../img/questao_1.4/4atividade.png", margem+50, 200, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 

def printar_quinta_questão(pdf):
    global margem
    global linha
    premiacoes_gerais = exploratory_analysis.premiacoes_album(df_musica_premiacao)
    visualization.grafico_premiacoes_album(premiacoes_gerais) #Vai salvar os gráficos na pasta
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
    pdf.drawImage(f"../img/questao_1.5/graf_premiacoes.png", margem+50, 75, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)
    pdf.drawString(150,800,"Análise da Discografia da banda AC/DC") 

def printar_sexta_questão(pdf):
    global margem
    global linha
    correlacao = exploratory_analysis.relacao_duracao_popularidade(df_musica)
    visualization.grafico_corresp(correlacao) #Vai salvar os gráficos na pasta
    visualization.grafico_plot(df_musica) #Vai salvar os gráficos na pasta
    printar_msg(pdf, f"A correlação entre a duração das músicas e a popularidade é de: {correlacao['Popularidade'].iloc[1]}")
    printar_msg(pdf, f"Logo, não tem correlação.")

    pdf.drawImage(f"../img/questao_1.6/corresp.png", margem+50, 270, width=400, preserveAspectRatio=True, mask='auto')
    pdf.drawImage(f"../img/questao_1.6/plot.png", margem+50, -25, width=400, preserveAspectRatio=True, mask='auto')
    pdf.setFont('VeraBd', 15)


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
    pdf.showPage()

    #Pergunta 3
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 3) Músicas mais ouvidas e músicas menos ouvidas")
    printar_msg(pdf, "[em toda a história da banda ou artista]:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_terceira_questão(pdf)
    pdf.showPage()

    #Pergunta 4
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 4) Músicas mais longas e músicas mais curtas")
    printar_msg(pdf, "[em toda a história da banda ou artista]:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_quarta_questão(pdf)
    pdf.showPage()

    #Pergunta 5
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 5) Álbuns mais premiados:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_quinta_questão(pdf)
    pdf.showPage()

    #Pergunta 6
    linha = 750
    pdf.setFont('VeraBd', 12)
    printar_msg(pdf, "Pergunta 6) Álbuns mais premiados:")
    pdf.setFont('Vera', 12)
    linha-=15
    printar_sexta_questão(pdf)
    pdf.showPage()

    pdf.save()

interface()