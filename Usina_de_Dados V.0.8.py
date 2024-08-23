#IMPORTACAO
from googleapiclient.discovery import build
from datetime import datetime
import pandas as pd
import time
import sys
#from tkinter import *
#from tkinter import ttk
import glob

import os


##############################################################
#CONFIGURAÇÕES
api_key = 'SUA_CHAVE_API'


entrada_arquivos = rf"PASTA_DE_ENTRADA"
saida_arquivos = rf"PASTA_DE_SAIDA"




#AI
class AI:
    def __init__(self, nome,sobrenome, maquina):
        self.nome = nome
        self.sobrenome = sobrenome
        self.maquina = maquina

    def boas_vindas(self):
        print(ss)
        print(self.nome,self.sobrenome,':',"Bem vindo a",self.maquina,"eu sou", self.nome,",como posso ajudar você hoje?")
        print(ss)
        print("Digite o número do serviço que deseja acessar:")
        print("1.",M_EX_VU)
        print("2.",M_EX_CA)
        print("3.",M_EX_PL)
        print("5.",M_IM_Ex)
        print("6.",M_FOR_DF)
        print("7.",M_EXP_Ex)
        print("8.",M_ARM_CHE)
        print("9.Teste de Logística de Dados - [EM BREVE]" )
        print("0.[SAIR]")
        print(ss)

    def comm(self, MQN):
    # Pergunta ao usuário se deseja continuar
        print(ss)
        print(self.nome,self.sobrenome,':',"Ferramenta selecionada:",MQN,'\n', )
        resposta = input("Pressione 1 para continuar ou digite '0' para voltar ao menu inicial: ")
        print(ss)
        if resposta == '1':
            print("Continuando com a próxima etapa...")
            print(ss)       

        elif resposta == '0':
            print("Voltando ao menu")
            print(ss)
            menu_teste()

    def abortar_programa(self):
        print(ss)
        print(self.nome,self.sobrenome,":Encerrando o programa. Obrigado")
        print(ss)
        sys.exit()


M_HUB = '[USINA TERRA DADOS V.0.8.0]'
M_EX_VU = '[EXTRATORA DE VIDEO UNICO]'
M_EX_CA = '[EXTRATORA DE CANAL]'
M_EX_PL = '[EXTRATORA DE PLAYLISTS]'
M_IM_Ex = '[IMPORTADOR DE EXCEL]'
M_FOR_DF = '[FORMATADOR DE DATAFRAME]'
M_ARM_CHE = '[CONFERIDOR DE ARMAZENAGEM]'
M_EXP_Ex = '[EXPORTADOR PARA EXCEL]'

AI_OP = AI(nome="AURELIA",sobrenome="AGRIPPINA",maquina=M_HUB)



##############################################################



##############################################################

#DEFINICOES

ss = "===================================================================================================================="
videoId = []
video_data = []
timestamp = datetime.now()
youtube = build('youtube', 'v3', developerKey=api_key)


##############################################################
#FUNCOES

##############################################################



##############################################################
#SUPORTE



def funcao3():
    print("Você escolheu a Função 3!")

def teste_logistica_01():
    A_I()




##############################################################
#MENU








def menu_teste():
    while True:
        AI_OP.boas_vindas()
        escolha = input("Escolha uma opção: ")

        #EXTRATOR UNICO
        if escolha == "1":
            AI_OP.comm(M_EX_VU)
            Extrator_Unico()
            Dataframer()
        #EXTRATOR CANAL
        elif escolha == "2":
            AI_OP.comm(M_EX_CA)
            Extrator_Canal()
            Dataframer()
        #EXTRATOR PLAYLISTS
        elif escolha == "3":
            AI_OP.comm(M_EX_PL)
            Extrator_playlists2()
        #LEITOR EXCEL
        elif escolha == "5":
            AI_OP.comm(M_IM_Ex)
            Leitor_excel()
        #FORMATADOR
        elif escolha == "6":
            AI_OP.comm(M_FOR_DF)
            Dataframer()
            Conferidor_dataframe()
            AI_OP.comm(M_HUB)
        #EXPORTADOR
        elif escolha == "7":
            AI_OP.comm(M_EXP_Ex)
            Conferidor_dataframe()
            Exportador_Excel()
            AI_OP.comm(M_HUB)
        #ARMAZENAMENTO
        elif escolha == "8":
            AI_OP.comm(M_ARM_CHE)
            armazenamento()
            AI_OP.comm(M_HUB)
        #TESTE
        elif escolha == "9":
            AI_OP.comm(M_HUB)
            
        elif escolha == "0":
            AI_OP.abortar_programa()
        else:
            print("Opção inválida. Tente novamente.")



################################################################

#IMPORTADORES
def Escritor_Banco_de_Dados():
    print('Escrevendo nos Bancos de Dados Integrados...')
    with open(entrada_arquivos, 'w') as f:
        for item in videoId:
            f.write(item + '\n')

def Leitor_Banco_de_Dados():
    print('Lendo Bancos de Dados Integrados...')
    with open(entrada_arquivos, 'r') as f:
        videoId = {line.strip() for line in f}
        print("Leitor de Banco de Dados diz: videoId:", videoId)  
        return videoId
    
def Leitor_excel():
    caminho_pasta = entrada_arquivos
    arquivos_excel = glob.glob(f'{caminho_pasta}/*.xlsx')

    df_final = pd.DataFrame()
    for arquivo in arquivos_excel:
        df_temporario = pd.read_excel(arquivo)
        df_final = pd.concat([df_final, df_temporario], ignore_index=True)
        video_data.append(df_final)
    print(df_final)
    print(video_data)
##############################################################

#CHAVES E SELETORES
def chave_api():
    print("Autenticando chave API...")
    youtube = build('youtube', 'v3', developerKey=api_key)

def Seletor_BD():
    resposta = input("")

def Seletor_Extrator():
    resposta = input("Selecione o Extrator:     1:Unico   2:Canal   3:Playlists")
    if resposta() == '1':
        print("Iniciando Extrator Unico...")
        #Extrator_Unico()
    elif resposta() == '2':
        print("Iniciando Extrator Canal...")

    elif resposta() == '3':
        print("Iniciando Extrator Playlists...")




##############################################################


#EXTRATORES
def Extrator_Unico():
    print("Autenticando chave API...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_id = input("Digite o ID do video:")

    request = youtube.videos().list(
        part="snippet,contentDetails,topicDetails, statistics",
        id=video_id
    )

    # Execute a solicitação e obtenha a resposta
    response = request.execute()
    print('Pegando dados do Vídeo:', video_id)
    print(response)
    for item in response['items']:
        #SNIPPETS
        title = item.get("snippet", {}).get("title", 0)
        channelId = item.get("snippet", {}).get("channelId", 0)
        channelTitle = item.get("snippet", {}).get("channelTitle", 0)
        publishedAt = item.get("snippet", {}).get("publishedAt", 0)
        categoryId = item.get("snippet", {}).get("categoryId", 0)
        viewCount = item.get("statistics", {}).get("viewCount", 0)
        description = item.get("snippet", {}).get("description", 0)
        #ESTATISTICAS
        commentCount = item.get("statistics", {}).get("commentCount", 0)
        likeCount = item.get("statistics", {}).get("likeCount", 0)
        #DETALHES CONTEUDO
        duration = item.get("contentDetails", {}).get("duration", 0)
        topicCategories = item.get("topicDetails", {}).get("topicCategories", 0)


    
    # Create a dictionary with video data and append it to the list
    video_dict = {
        "Título": title,
        "ID Video": video_id,
        "Canal": channelTitle,
        "ID Canal": channelId,
        "Visualizações": viewCount,
        "Publicado": publishedAt,
        "Comentários": commentCount,
        "Duração": duration,
        "Curtidas" : likeCount,   
        "ID de categoria" : categoryId,
        "Topico Wikipedia" : topicCategories,
        "Descrição" : description,
    }
    video_data.append(video_dict)
    return video_data


def Extrator_Canal():
    print("Autenticando chave API...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = input("Digite o ID do canal:")
    page_token = ""
    while page_token is not None: 
        # Make a request to the YouTube API to get the latest 50 videos of the channel
        request = youtube.search().list(
            part = "snippet",
            type = "video",
            order = "date",
            channelId = channel_id,
            maxResults = 50,
            pageToken = page_token
        )
        response = request.execute()
        # Iterate over the items in the response
        for item in response["items"]:
            # Get video ID
            video_id = item["id"]["videoId"]
            print('Conferindo Ids:', video_id)
            # Make another request to the YouTube API to get more details about the video
            request = youtube.videos().list(
                part = "snippet,contentDetails,statistics,topicDetails",
                id = video_id
        )
        
        response = request.execute()
        # Recupera informações adicionais do vídeo
        for item in response['items']:
            #SNIPPETS
            title = item.get("snippet", {}).get("title", 0)
            channelId = item.get("snippet", {}).get("channelId", 0)
            channelTitle = item.get("snippet", {}).get("channelTitle", 0)
            publishedAt = item.get("snippet", {}).get("publishedAt", 0)
            categoryId = item.get("snippet", {}).get("categoryId", 0)
            viewCount = item.get("statistics", {}).get("viewCount", 0)
            description = item.get("snippet", {}).get("description", 0)
            #ESTATISTICAS
            commentCount = item.get("statistics", {}).get("commentCount", 0)
            likeCount = item.get("statistics", {}).get("likeCount", 0)
            #DETALHES CONTEUDO
            duration = item.get("contentDetails", {}).get("duration", 0)
            topicCategories = item.get("topicDetails", {}).get("topicCategories", 0)


            # Create a dictionary with video data and append it to the list
            video_dict = {
                "Título": title,
                "ID Video": video_id,
                "Canal": channelTitle,
                "ID Canal": channelId,
                "Visualizações": viewCount,
                "Publicado": publishedAt,
                "Comentários": commentCount,
                "Duração": duration,
                "Curtidas" : likeCount,   
                "ID de categoria" : categoryId,
                "Topico Wikipedia" : topicCategories,
                "Descrição" : description,
            }
            video_data.append(video_dict)

        # Get the next page token
        page_token = response.get('nextPageToken')
        # If there is no next page token, we have reached the end of the results
        if not page_token:
            break
        # Add a delay before the next request
        time.sleep(2)
    return video_data


def Extrator_playlists2():
    print("Autenticando chave API...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    playlist_id = input("insira o código da playlist:")

    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
)
    playlist_response = request.execute()

    # Itera sobre os itens e recupera as informações necessárias
    for item in playlist_response['items']:
        video_id = item['snippet']['resourceId']['videoId']  # Recupera o ID do vídeo
        title = item['snippet']['title']
        
        
        # Faz uma nova requisição para obter detalhes do vídeo específico
        video_request = youtube.videos().list(
            part='snippet,contentDetails,statistics,status, topicDetails',
            id=video_id
        )
        response = video_request.execute()
        # Recupera informações adicionais do vídeo
        for item in response['items']:
            #SNIPPETS
            title = item.get("snippet", {}).get("title", 0)
            channelId = item.get("snippet", {}).get("channelId", 0)
            channelTitle = item.get("snippet", {}).get("channelTitle", 0)
            publishedAt = item.get("snippet", {}).get("publishedAt", 0)
            categoryId = item.get("snippet", {}).get("categoryId", 0)
            viewCount = item.get("statistics", {}).get("viewCount", 0)
            description = item.get("snippet", {}).get("description", 0)
            #ESTATISTICAS
            commentCount = item.get("statistics", {}).get("commentCount", 0)
            likeCount = item.get("statistics", {}).get("likeCount", 0)
            #DETALHES CONTEUDO
            duration = item.get("contentDetails", {}).get("duration", 0)
            topicCategories = item.get("topicDetails", {}).get("topicCategories", 0)


            # Create a dictionary with video data and append it to the list
            video_dict = {
                "Título": title,
                "ID Video": video_id,
                "Canal": channelTitle,
                "ID Canal": channelId,
                "Visualizações": viewCount,
                "Publicado": publishedAt,
                "Comentários": commentCount,
                "Duração": duration,
                "Curtidas" : likeCount,   
                "ID de categoria" : categoryId,
                "Topico Wikipedia" : topicCategories,
                "Descrição" : description,
            }
            video_data.append(video_dict)
    return video_data





##############################################################
#FORMATADORES
def Dataframer():
    # Cria um DataFrame com os dados
    videos_df = pd.DataFrame(video_data, columns=['Título','ID Video', 'Canal','ID Canal',  'Visualizações', 'Publicado','Comentários','Duração', 'Curtidas', 'ID de categoria', "Descrição"])
    videos_df['Visualizações'] = pd.to_numeric(videos_df['Visualizações'], errors='coerce')
    videos_df["Comentários"] = pd.to_numeric(videos_df['Comentários'], errors='coerce')
    videos_df['Curtidas'] = pd.to_numeric(videos_df['Curtidas'], errors='coerce')
    videos_df['Dia'] = timestamp.date()  # Obtém a data
    videos_df['Hora Local'] = timestamp.time()  # Obtém a hora
    
    return videos_df

def Conferidor_dataframe():
    print("==========================Conferencia de dados dataframe:========================================")
    videos_df = Dataframer()
    print(videos_df)
    maquinas_de_dados = videos_df.dtypes
    print(maquinas_de_dados)

def armazenamento():
    print(video_data)


##############################################################

#EXPORTACAO
def Exportador_Excel():
    # Pergunta ao usuário se deseja continuar
    confirmacao = input('Deseja exportar os dados para Excel? (s/n): ')

    # Verifica a resposta do usuário
    if confirmacao.lower() == 's':
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        # Define o caminho e o nome do arquivo com a data e hora
        file_name = f'USINA TERRA DADOS V.0.8_{timestamp}.xlsx'
        file_path = os.path.join(saida_arquivos,file_name)    
        # Exporta para um arquivo Excel com o nome contendo a data e horas
        videos_df = Dataframer()
        videos_df.to_excel(file_path, index=False)
        print('Dados exportados com sucesso!')
    else:
        print('Exportação cancelada.')


##############################################################




#ATIVACAO




menu_teste()










