# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuperbInicio(object):
    def setupUi(self, SuperbInicio):
        SuperbInicio.setObjectName("SuperbInicio")
        SuperbInicio.resize(870, 571)
        SuperbInicio.setMinimumSize(QtCore.QSize(870, 571))
        SuperbInicio.setMaximumSize(QtCore.QSize(870, 571))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone Site/images/icone site.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SuperbInicio.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SuperbInicio)
        self.centralwidget.setMinimumSize(QtCore.QSize(870, 545))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0597015, y1:0.08, x2:0.93, y2:0.886, stop:0 rgba(21, 24, 48, 255), stop:1 rgba(199, 19, 15, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 468))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.585227, x2:1, y2:0.574136, stop:0.223881 rgba(25, 28, 41, 255), stop:0.293532 rgba(27, 29, 53, 227), stop:0.58209 rgba(27, 29, 53, 227), stop:0.651741 rgba(97, 30, 21, 255));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame2_pag2 = QtWidgets.QFrame(self.frame_3)
        self.frame2_pag2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame2_pag2.setStyleSheet("background-color: rgb(35, 30, 52);\n"
"border-radius: 30px;")
        self.frame2_pag2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2_pag2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2_pag2.setObjectName("frame2_pag2")
        self.frame1_pag2 = QtWidgets.QFrame(self.frame2_pag2)
        self.frame1_pag2.setGeometry(QtCore.QRect(0, 0, 230, 561))
        self.frame1_pag2.setAutoFillBackground(False)
        self.frame1_pag2.setStyleSheet("background-color: rgb(25, 28, 41);\n"
"border-radius: 30px;")
        self.frame1_pag2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_pag2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_pag2.setObjectName("frame1_pag2")
        self.botaoListaJogo_pag2 = QtWidgets.QPushButton(self.frame1_pag2)
        self.botaoListaJogo_pag2.setGeometry(QtCore.QRect(40, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.botaoListaJogo_pag2.setFont(font)
        self.botaoListaJogo_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoListaJogo_pag2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(25, 28, 41);\n"
"    border: 2px solid rgb(35, 30, 52);\n"
"    border-radius: 5px;\n"
"    color: rgb(108, 83, 171);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 30, 52);\n"
"    border: 2px solid rgb(175, 54, 38);\n"
"    color: rgb(175, 54, 38);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rbg(250, 270, 200);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(219, 149, 121);\n"
"}")
        self.botaoListaJogo_pag2.setObjectName("botaoListaJogo_pag2")
        self.iconPerfil_pag2 = QtWidgets.QLabel(self.frame1_pag2)
        self.iconPerfil_pag2.setGeometry(QtCore.QRect(70, 40, 81, 81))
        self.iconPerfil_pag2.setStyleSheet("border-radius: 40px;\n"
"background-image: url(:/iconPerfil_pag2/iconPerfil_pag2.png);")
        self.iconPerfil_pag2.setText("")
        self.iconPerfil_pag2.setObjectName("iconPerfil_pag2")
        self.labelIconPerfil_pag2 = QtWidgets.QLabel(self.frame1_pag2)
        self.labelIconPerfil_pag2.setGeometry(QtCore.QRect(69, 40, 81, 81))
        self.labelIconPerfil_pag2.setStyleSheet("border-radius: 40px;\n"
"background-image: url(:/Perfil/images/iconPerfil_pag2.png);")
        self.labelIconPerfil_pag2.setText("")
        self.labelIconPerfil_pag2.setObjectName("labelIconPerfil_pag2")
        self.labelNomeUser_pag2 = QtWidgets.QLabel(self.frame1_pag2)
        self.labelNomeUser_pag2.setGeometry(QtCore.QRect(20, 145, 181, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelNomeUser_pag2.setFont(font)
        self.labelNomeUser_pag2.setStyleSheet("color: rgb(175, 54, 38);")
        self.labelNomeUser_pag2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNomeUser_pag2.setObjectName("labelNomeUser_pag2")
        self.labelVerificar_pag2 = QtWidgets.QLabel(self.frame1_pag2)
        self.labelVerificar_pag2.setGeometry(QtCore.QRect(40, 280, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelVerificar_pag2.setFont(font)
        self.labelVerificar_pag2.setStyleSheet("color: rgb(255, 230, 219);\n"
"")
        self.labelVerificar_pag2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelVerificar_pag2.setObjectName("labelVerificar_pag2")
        self.botaoListaJogo_pag2_2 = QtWidgets.QPushButton(self.frame1_pag2)
        self.botaoListaJogo_pag2_2.setGeometry(QtCore.QRect(40, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.botaoListaJogo_pag2_2.setFont(font)
        self.botaoListaJogo_pag2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoListaJogo_pag2_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(25, 28, 41);\n"
"    border: 2px solid rgb(35, 30, 52);\n"
"    border-radius: 5px;\n"
"    color: rgb(108, 83, 171);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 30, 52);\n"
"    border: 2px solid rgb(175, 54, 38);\n"
"    color: rgb(175, 54, 38);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rbg(250, 270, 200);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(219, 149, 121);\n"
"}")
        self.botaoListaJogo_pag2_2.setObjectName("botaoListaJogo_pag2_2")
        self.iconPerfil_pag2.raise_()
        self.labelIconPerfil_pag2.raise_()
        self.labelNomeUser_pag2.raise_()
        self.labelVerificar_pag2.raise_()
        self.botaoListaJogo_pag2.raise_()
        self.botaoListaJogo_pag2_2.raise_()
        self.botaoHades2_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoHades2_pag2.setGeometry(QtCore.QRect(280, 40, 451, 211))
        self.botaoHades2_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoHades2_pag2.setMouseTracking(False)
        self.botaoHades2_pag2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botaoHades2_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Hades 2/images/header_hades_pag2.jpg);\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Hades 2/images/header_hades_hover_pag2.png);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoHades2_pag2.setText("")
        self.botaoHades2_pag2.setAutoDefault(False)
        self.botaoHades2_pag2.setFlat(False)
        self.botaoHades2_pag2.setObjectName("botaoHades2_pag2")
        self.botaoScratchinMelodii_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoScratchinMelodii_pag2.setGeometry(QtCore.QRect(250, 300, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botaoScratchinMelodii_pag2.setFont(font)
        self.botaoScratchinMelodii_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoScratchinMelodii_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Scratchin Melodii/images/scratchinmelodii_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Scratchin Melodii/images/scratchinmelodii_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoScratchinMelodii_pag2.setObjectName("botaoScratchinMelodii_pag2")
        self.botaoCeleste_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoCeleste_pag2.setGeometry(QtCore.QRect(605, 300, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botaoCeleste_pag2.setFont(font)
        self.botaoCeleste_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoCeleste_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Celeste/images/celeste_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Celeste/images/celeste_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoCeleste_pag2.setObjectName("botaoCeleste_pag2")
        self.botaoNineSols_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoNineSols_pag2.setGeometry(QtCore.QRect(428, 300, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botaoNineSols_pag2.setFont(font)
        self.botaoNineSols_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoNineSols_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Nine Sols/images/ninesols_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Nine Sols/images/ninesols_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoNineSols_pag2.setObjectName("botaoNineSols_pag2")
        self.botaoMulletMadjack_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoMulletMadjack_pag2.setGeometry(QtCore.QRect(250, 420, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botaoMulletMadjack_pag2.setFont(font)
        self.botaoMulletMadjack_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoMulletMadjack_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Mullet Madjack/images/mulletmadjack_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Mullet Madjack/images/mulletmadjack_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoMulletMadjack_pag2.setObjectName("botaoMulletMadjack_pag2")
        self.botaoMurkyDivers_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoMurkyDivers_pag2.setGeometry(QtCore.QRect(428, 420, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.botaoMurkyDivers_pag2.setFont(font)
        self.botaoMurkyDivers_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoMurkyDivers_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo Murky Divers/images/murkydivers_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo Murky Divers/images/murkydivers_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoMurkyDivers_pag2.setObjectName("botaoMurkyDivers_pag2")
        self.botaoBombRush_pag2 = QtWidgets.QPushButton(self.frame2_pag2)
        self.botaoBombRush_pag2.setGeometry(QtCore.QRect(605, 420, 157, 90))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.botaoBombRush_pag2.setFont(font)
        self.botaoBombRush_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoBombRush_pag2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/Jogo BombRush/images/bombrush_pag2.png);\n"
"    border-radius: 12px;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.532338 rgba(27, 29, 53, 0));\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Jogo BombRush/images/bombrush_hover_pag2.png);\n"
"    color: rgb(234, 217, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"")
        self.botaoBombRush_pag2.setObjectName("botaoBombRush_pag2")
        self.horizontalLayout.addWidget(self.frame2_pag2)
        self.frame3_pag2 = QtWidgets.QFrame(self.frame_3)
        self.frame3_pag2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame3_pag2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame3_pag2.setStyleSheet("background-color: rgb(97, 30, 21);")
        self.frame3_pag2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3_pag2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3_pag2.setObjectName("frame3_pag2")
        self.botaoVoltarLog_pag2 = QtWidgets.QPushButton(self.frame3_pag2)
        self.botaoVoltarLog_pag2.setGeometry(QtCore.QRect(4, 402, 61, 61))
        self.botaoVoltarLog_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoVoltarLog_pag2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(97,30, 21);\n"
"    background-image: url(:/Login/images/casa_login_pag2.png);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Login/images/casa_login_hover_pag2.png);\n"
"    background-color: rgb(84, 26, 18);\n"
"    border: 2px solid rgb(84, 26, 18);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(141, 44, 31);\n"
"    border: 2px solid rgb(141, 44, 31);\n"
"}")
        self.botaoVoltarLog_pag2.setText("")
        self.botaoVoltarLog_pag2.setObjectName("botaoVoltarLog_pag2")
        self.botaoSair_pag2 = QtWidgets.QPushButton(self.frame3_pag2)
        self.botaoSair_pag2.setGeometry(QtCore.QRect(4, 470, 61, 61))
        self.botaoSair_pag2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoSair_pag2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(97,30, 21);\n"
"    background-image: url(:/Sair/images/sair_pag2.png);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-image: url(:/Sair/images/sair_hover_pag2.png);\n"
"    background-color: rgb(84, 26, 18);\n"
"    border: 2px solid rgb(84, 26, 18);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(141, 44, 31);\n"
"    border: 2px solid rgb(141, 44, 31);\n"
"}")
        self.botaoSair_pag2.setText("")
        self.botaoSair_pag2.setObjectName("botaoSair_pag2")
        self.iconSuperb_pag2 = QtWidgets.QLabel(self.frame3_pag2)
        self.iconSuperb_pag2.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.iconSuperb_pag2.setStyleSheet("image: url(:/Icone Site/images/icone site.png);")
        self.iconSuperb_pag2.setText("")
        self.iconSuperb_pag2.setObjectName("iconSuperb_pag2")
        self.horizontalLayout.addWidget(self.frame3_pag2)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.frame)
        SuperbInicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuperbInicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 26))
        self.menubar.setObjectName("menubar")
        SuperbInicio.setMenuBar(self.menubar)

        self.retranslateUi(SuperbInicio)
        self.botaoSair_pag2.clicked.connect(SuperbInicio.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SuperbInicio)

    def retranslateUi(self, SuperbInicio):
        _translate = QtCore.QCoreApplication.translate
        SuperbInicio.setWindowTitle(_translate("SuperbInicio", "Superb"))
        self.botaoListaJogo_pag2.setText(_translate("SuperbInicio", "Suas Avaliações"))
        self.labelNomeUser_pag2.setText(_translate("SuperbInicio", "Olá, xxxx!"))
        self.labelVerificar_pag2.setText(_translate("SuperbInicio", "Verificar:"))
        self.botaoListaJogo_pag2_2.setText(_translate("SuperbInicio", "SteamApp"))
        self.botaoScratchinMelodii_pag2.setText(_translate("SuperbInicio", "SCRATCHIN\n"
"MELODII"))
        self.botaoCeleste_pag2.setText(_translate("SuperbInicio", "CELESTE"))
        self.botaoNineSols_pag2.setText(_translate("SuperbInicio", "NINE SOLS"))
        self.botaoMulletMadjack_pag2.setText(_translate("SuperbInicio", " MULLET\n"
"MADJACK"))
        self.botaoMurkyDivers_pag2.setText(_translate("SuperbInicio", "MURKY DIVERS"))
        self.botaoBombRush_pag2.setText(_translate("SuperbInicio", "BOMB RUSH\n"
"CYBERFUNK"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuperbInicio = QtWidgets.QMainWindow()
    ui = Ui_SuperbInicio()
    ui.setupUi(SuperbInicio)
    SuperbInicio.show()
    sys.exit(app.exec_())
