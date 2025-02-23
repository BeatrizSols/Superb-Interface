    # BIBLIOTECAS
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys, webbrowser

    # Interfaces geradas pelo QtDesigner
from pagina_avaliacao import Ui_SuperbAvaliar
from pagina_biblioteca import Ui_SuperbBiblioteca
from pagina_inicio import Ui_SuperbInicio
from pagina_login import Ui_SuperbLogin

    # Controlador user
class Usuario:
    def __init__(self):
        # User compartilhado entre todas as páginas
        self.usuario = ''

    # Controlador lista de avaliações
class Avaliacao:
    def __init__(self):
        # Lista compartilhada entre todas as páginas
        self.historico_avaliacoes = []

    # Avaliação
class Avaliar(QMainWindow):
    def __init__(self, estado, jogo_selecionado, historico_avaliacoes, *args, **argvs):
        super(Avaliar, self).__init__(*args, **argvs)
        self.ui = Ui_SuperbAvaliar()
        self.ui.setupUi(self)
        self.historico_avaliacoes = historico_avaliacoes # Salvando histórico de avaliações
        self.estado = estado # Salvando user
        self.jogo_selecionado = jogo_selecionado # Jogo selecionado
        self.nome_jogo = None  # Armazenar nome do jogo atual

        # Conectar botões à lógica
        self.ui.textAvaliar_pag3.textChanged.connect(self.limitar_caracteres)
        self.ui.botaoFechar_pag3.clicked.connect(self.voltar_inicio) # Voltando ao início
        self.ui.botaoSubmeter_pag3.clicked.connect(self.submeter_dados)  # Conectando o botão ao metodo de salvar dados

        self.exibir_imagem_jogo(jogo_selecionado) # Selecionar imagem do jogo
        self.exibir_nome_jogo(jogo_selecionado) # Selecionar nome do jogo

        # Limitando caracteres no texto de avaliação
    def limitar_caracteres(self):
        limite = 150  # Definir o limite de caracteres
        texto = self.ui.textAvaliar_pag3.toPlainText()
        if len(texto) > limite:
            # Truncar o texto caso ultrapasse o limite
            self.ui.textAvaliar_pag3.setPlainText(texto[:limite])

            # Reposicionar o cursor no final após truncar
            cursor = self.ui.textAvaliar_pag3.textCursor()
            cursor.setPosition(limite)
            self.ui.textAvaliar_pag3.setTextCursor(cursor)


    # Selecionar nome do jogo
    def exibir_nome_jogo(self, jogo):
        nomes = {
            "celeste": "Celeste",
            "bomb_rush": "BombRush Cyberfunk",
            "nine_sols": "Nine Sols",
            "hades_2": "Hades 2",
            "murky_divers": "Murky Divers",
            "mullet_madjack": "Mullet Madjack",
            "scratchin_melodii": "Scratchin Melodii"
        }
        self.nome_jogo = nomes.get(jogo) # Usando .get no dicionário
        self.ui.labelNomeJogo_pag3.setText(self.nome_jogo) # Nome do jogo na labelNome

    # Selecionar imagem do jogo
    def exibir_imagem_jogo(self, jogo):
        imagens = {
            "celeste": "images/labelAvCeleste_pag3.png",
            "bomb_rush": "images/labelAvBombRush_pag3.png",
            "nine_sols": "images/labelAvNineSols_pag3.png",
            "hades_2": "images/labelAvHades2_pag3.png",
            "murky_divers": "images/labelAvMurkyDivers_pag3.png",
            "mullet_madjack": "images/labelAvMulletMadjack_pag3.png",
            "scratchin_melodii": "images/labelAvScratchinMelodii_pag3.png"
        }
        caminho_imagem = imagens.get(jogo) # Usando .get no dicionário
        pixmap = QPixmap(caminho_imagem) # Pixmap otimiza, renderiza e redimensiona a imagem caso precise
        self.ui.labelFotoJogo_pag3.setPixmap(pixmap) # Foto da imagem na labelFoto

    # Salvando dados do formulario
    def salvar_dados(self):
        # Recuperar o texto de avaliação e o tempo de jogo
        avaliacao_texto = self.ui.textAvaliar_pag3.toPlainText()  # Avaliação por texto
        avaliacao_tempo_jogo = str(self.ui.DSPContador_pag3.value()) # Tempo do jogo transformado em uma string

        # Verificar qual botão foi clicado
        if self.ui.botaoGostei_pag3.isChecked():
            avaliacao_por_botao = "Gostei"
        elif self.ui.botaoNGostei_pag3.isChecked():
            avaliacao_por_botao = "Não gostei"
        else:
            avaliacao_por_botao = None  # Nenhum botão foi selecionado

        # Salvando a avaliação em um dicionário
        avaliacao = {
            "nome_jogo": self.nome_jogo,
            "avaliacao_texto": avaliacao_texto,
            "avaliacao_tempo_jogo": avaliacao_tempo_jogo,
            "avaliacao_por_botao": avaliacao_por_botao
        }

        # Armazenar avaliação na lista de avaliados
        self.historico_avaliacoes.historico_avaliacoes.append(avaliacao)

        # Submetendo dados
    def submeter_dados(self):
        self.salvar_dados()  # Ativar função salvar_dados
        self.window = Biblioteca(self.estado, self.historico_avaliacoes)# Mudar a página e transportar as variáveis entre elas
        self.window.show() # Mostrar a página atual
        self.close() # Fechar a antiga página
        print(self.historico_avaliacoes.historico_avaliacoes) # Print no terminal

        # Voltar ao início
    def voltar_inicio(self):
        self.window = Inicio(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show() # Mostrar a página atual
        self.close() # Fechar a antiga página

    # Biblioteca
class Biblioteca(QMainWindow):
    def __init__(self, estado, historico_avaliacoes, *args, **argvs):
        super(Biblioteca, self).__init__(*args, **argvs)
        self.ui = Ui_SuperbBiblioteca()
        self.ui.setupUi(self)

        # Inicializando variáveis
        self.historico_avaliacoes = historico_avaliacoes # Salvando histórico de avaliações
        self.estado = estado  # Salvando usuário
        self.pagina_atual = 0  # Sempre começamos na página 0

        # Conectar botões à lógica
        self.ui.botaoVoltarLog_pag3.clicked.connect(self.voltar_login)  # Ativar função voltar_login
        self.ui.botaoInicio_pag3.clicked.connect(self.voltar_inicio)  # Ativar função voltar_inicio
        self.ui.labelNome_pag3.setText(self.estado.usuario)  # Nome do user na label Bib
        self.ui.botaoDescer_pag3.clicked.connect(self.mudar_pagina) # Ativar função mudar_pagina

        # Exibir somente as avaliações correspondentes à página atual
        self.exibir_informacoes_biblioteca()

    # Mudar a página
    def mudar_pagina(self):
        # Verifica se ainda há páginas disponíveis
        total_itens = len(self.historico_avaliacoes.historico_avaliacoes)
        total_paginas = (total_itens + 3) // 4  # Calcula o número total de páginas

        if self.pagina_atual + 1 < total_paginas:  # Se a próxima página existir
            self.pagina_atual += 1  # Avança para a próxima página
            self.exibir_informacoes_biblioteca()  # Recarrega a função de exibir_informações_biblioteca
        else:
            print("Não há mais páginas disponíveis.")  # Print no terminal

    # Exibir as imagens com base na página atual
    def exibir_informacoes_biblioteca(self):

        # Dicionário que mapeia o nome do jogo às imagens
        imagens = {
            "Celeste": "images/BibCeleste.png",
            "BombRush Cyberfunk": "images/BibBombRush.png",
            "Nine Sols": "images/BibNineSols.png",
            "Hades 2": "images/BibHades2.png",
            "Murky Divers": "images/BibMurkyDivers.png",
            "Mullet Madjack": "images/BibMulletMadjack.png",
            "Scratchin Melodii": "images/BibScratchinMelodii.png"
        }

        # QLabels para exibir as fotos dos jogos
        labels = [
            self.ui.labelIMG1,
            self.ui.labelIMG2,
            self.ui.labelIMG3,
            self.ui.labelIMG4
        ]

        # QLabels para exibir os nomes dos jogos
        labels_nome_jogo = [
            self.ui.labelnome1,
            self.ui.labelnome2,
            self.ui.labelnome3,
            self.ui.labelnome4
        ]

        # QLabels para exibir os textos das avaliações
        labels_avaliacoes = [
            self.ui.labeltextavaliar1,
            self.ui.labeltextavaliar2,
            self.ui.labeltextavaliar3,
            self.ui.labeltextavaliar4
        ]

        # QLabels para exibir os tempos
        labels_tempo = [
            self.ui.labelhorasjogadas1,
            self.ui.labelhorasjogadas2,
            self.ui.labelhorasjogadas3,
            self.ui.labelhorasjogadas4
        ]

        # QLabels para exibir as imagens de Gostei/NGostei
        labels_joinha = [
            self.ui.labelIMGjoinha1,
            self.ui.labelIMGjoinha2,
            self.ui.labelIMGjoinha3,
            self.ui.labelIMGjoinha4
        ]

        # Verificar se há avaliações antes de processar
        if not self.historico_avaliacoes.historico_avaliacoes:
            print("Nenhuma avaliação disponível.") # Print no terminal
            return

        # Calcula o índice inicial e final das avaliações com base na página
        inicio = self.pagina_atual * 4
        fim = inicio + 4

        # Garantir que está dentro do limite da lista
        avaliacoes = self.historico_avaliacoes.historico_avaliacoes[inicio:fim]


        # Limpar QLabels (esvaziar antes de popular novamente)
        for label in labels + labels_nome_jogo + labels_tempo + labels_avaliacoes + labels_joinha:
            label.clear()

        # Preencher as labels com base nas avaliações da página
        for i, avaliacao in enumerate(avaliacoes):  # Usa enumerate para evitar problemas de índice
            nome_jogo = avaliacao.get("nome_jogo")  # Nome do jogo avaliado
            texto_avaliacao = avaliacao.get("avaliacao_texto", "Sem texto")  # Texto de avaliação
            botao_joinha = avaliacao.get("avaliacao_por_botao", "Sem click")  # Gostei/Não gostei
            tempo_avaliacao = avaliacao.get("avaliacao_tempo_jogo", "Sem tempo")  # Tempo de jogo

            # Atualiza as labels de nome de jogo
            labels_nome_jogo[i].setText(nome_jogo)

            # Atualiza as labels de texto de avaliação
            labels_avaliacoes[i].setText(texto_avaliacao)

            # Atualiza as labels de horas jogadas
            labels_tempo[i].setText(tempo_avaliacao + " hrs")

            # Atualiza as imagem das labels de joinha puxando o valor guardado pelas chaves
            if botao_joinha == "Gostei":
                pixmap = QPixmap("images/BibGostei.png")  # Caminho da imagem "Gostei"
            elif botao_joinha == "Não gostei":
                pixmap = QPixmap("images/BibNGostei.png")  # Caminho da imagem "Não Gostei"
            else:
                pixmap = QPixmap()  # Deixar vazio caso não haja avaliação

            labels_joinha[i].setPixmap(pixmap)  # Define a imagem na label correspondente
            labels_joinha[i].setScaledContents(True)  # Ajusta a imagem ao tamanho da label

            # Atualiza a imagem das labels de imagem do jogo
            if nome_jogo in imagens:
                pixmap = QPixmap(imagens[nome_jogo])  # Carregar a imagem
                labels[i].setPixmap(pixmap)  # Definir a imagem na label correspondente
                labels[i].setScaledContents(True)  # Ajustar ao tamanho da label

    # Indo ao login
    def voltar_login(self):
        self.window = Login(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show()  # Mostrar a página atual
        self.close()  # Fechar a antiga página

    # Indo ao início
    def voltar_inicio(self):
        self.window = Inicio(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show()  # Mostrar a página atual
        self.close()  # Fechar a antiga página

    # Início
class Inicio(QMainWindow):
    def __init__(self, estado, historico_avaliacoes, *args, **argvs):
        super(Inicio, self).__init__(*args, **argvs)
        self.ui = Ui_SuperbInicio()
        self.ui.setupUi(self)
        self.historico_avaliacoes = historico_avaliacoes # Salvando histórico de avaliações
        self.estado = estado # Salvando user
        self.ui.labelNomeUser_pag2.setText(f"Olá, {self.estado.usuario}!") # Nome do user na label do Início

        # Conectar botões à lógica
        self.ui.botaoVoltarLog_pag2.clicked.connect(self.voltar_login) # Ativar função voltar_login
        self.ui.botaoListaJogo_pag2.clicked.connect(self.ir_biblioteca) # Ativar função ir_biblioteca
        self.ui.botaoListaJogo_pag2_2.clicked.connect(self.ir_SteamApp) # Ativar função ir_SteamApp

        # Selecionando jogo - cada jogo recebe uma chave para os dicionários
        self.ui.botaoCeleste_pag2.clicked.connect(lambda: self.ir_avaliacao("celeste"))
        self.ui.botaoBombRush_pag2.clicked.connect(lambda: self.ir_avaliacao("bomb_rush"))
        self.ui.botaoNineSols_pag2.clicked.connect(lambda: self.ir_avaliacao("nine_sols"))
        self.ui.botaoHades2_pag2.clicked.connect(lambda: self.ir_avaliacao("hades_2"))
        self.ui.botaoMurkyDivers_pag2.clicked.connect(lambda: self.ir_avaliacao("murky_divers"))
        self.ui.botaoMulletMadjack_pag2.clicked.connect(lambda: self.ir_avaliacao("mullet_madjack"))
        self.ui.botaoScratchinMelodii_pag2.clicked.connect(lambda: self.ir_avaliacao("scratchin_melodii"))

    # Indo à Avaliação
    def ir_avaliacao(self, jogo_selecionado):
        self.window = Avaliar(self.estado, jogo_selecionado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show() # Mostrar a página atual
        self.close() # Fechar a antiga página

    # Indo à Steam
    def ir_SteamApp(self):
        webbrowser.open('https://store.steampowered.com/') # Abrir browser (no IF o site é bloqueado)

    # Indo ao login
    def voltar_login(self):
        self.window = Login(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show() # Mostrar a página atual
        self.close() # Fechar a antiga página

    # Indo à Biblioteca
    def ir_biblioteca(self):
        self.window = Biblioteca(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
        self.window.show() # Mostrar a página atual
        self.close() # Fechar a antiga página

    # Login
class Login(QMainWindow):
    def __init__(self, estado, historico_avaliacoes, *args, **argvs):
        super(Login, self).__init__(*args, **argvs)
        self.ui = Ui_SuperbLogin()
        self.ui.setupUi(self)
        self.historico_avaliacoes = historico_avaliacoes # Salvando histórico de avaliações
        self.estado = estado # Salvando user

        # Conectar botões à lógica
        self.ui.conectar_login.clicked.connect(self.login) # Ativar função login

    # Indo ao Início e inserindo login
    def login(self):
        user = self.ui.user.text()
        passwrd = self.ui.user_2.text()
        if user and passwrd: # Conferir se estão preenchidos
            self.estado.usuario = user # Salvando user
            self.window = Inicio(self.estado, self.historico_avaliacoes) # Mudar a página e transportar as variáveis entre elas
            self.window.show() # Mostrar a página atual
            self.close() # Fechar a antiga página

        else:
            self.ui.cabecalho.show() # Mostrar cabeçalho de erro



app = QApplication(sys.argv) # Abrindo execução
estado = Usuario() # Chamando a classe de Usuario
historico_avaliacoes = Avaliacao() # Chamando a classe de Avaliação
window = Login(estado, historico_avaliacoes) # Chamando a classe de Login (primeira pág mostrada), transportando as variáveis
window.show() # Mostrar a página
sys.exit(app.exec_()) # Fechando execução