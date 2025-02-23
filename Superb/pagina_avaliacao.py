# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDoubleSpinBox


class Ui_SuperbAvaliar(object):
    def setupUi(self, SuperbAvaliar):
        SuperbAvaliar.setObjectName("SuperbAvaliar")
        SuperbAvaliar.resize(870, 571)
        SuperbAvaliar.setMinimumSize(QtCore.QSize(870, 571))
        SuperbAvaliar.setMaximumSize(QtCore.QSize(870, 571))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone Site/images/icone site.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SuperbAvaliar.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SuperbAvaliar)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 33, 64, 255), stop:0.208955 rgba(39, 35, 57, 255), stop:0.830846 rgba(141, 44, 31, 255), stop:1 rgba(199, 49, 15, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(13, 13, 13, 13)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_1 = QtWidgets.QFrame(self.frame)
        self.frame_1.setStyleSheet("background-color: rgb(12, 14, 28);\n"
"border-radius: 10px;")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_1)
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(27, 19, 47, 255), stop:0.368159 rgba(12, 14, 28, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(27, 19, 47, 255), stop:0.368159 rgba(22, 17, 40, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(27, 19, 47);\n"
"border-radius: 30px\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.labelFotoJogo_pag3 = QtWidgets.QLabel(self.frame_3)
        self.labelFotoJogo_pag3.setGeometry(QtCore.QRect(49, 50, 251, 351))
        self.labelFotoJogo_pag3.setStyleSheet("background-color: rgb(39, 35, 57);\n"
"border-radius: 5px;")
        self.labelFotoJogo_pag3.setText("")
        self.labelFotoJogo_pag3.setObjectName("labelFotoJogo_pag3")
        self.labelNomeJogo_pag3 = QtWidgets.QLabel(self.frame_3)
        self.labelNomeJogo_pag3.setGeometry(QtCore.QRect(30, 420, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelNomeJogo_pag3.setFont(font)
        self.labelNomeJogo_pag3.setStyleSheet("color: rgb(255, 230, 219);")
        self.labelNomeJogo_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNomeJogo_pag3.setObjectName("labelNomeJogo_pag3")
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("background-color: rgb(22, 17, 40);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.botaoGostei_pag3 = QtWidgets.QRadioButton(self.frame_4)
        self.botaoGostei_pag3.setGeometry(QtCore.QRect(320, 60, 61, 61))
        self.botaoGostei_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoGostei_pag3.setStyleSheet("QRadioButton::indicator {\n"
"    background: transparent;\n"
"    image: url(:/Av Gostei/images/RBotaoGostei_pag3.png);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    image: url(:/Av Gostei/images/RBotaoGostei_hover_pag3.png);\n"
"}\n"
"QRadioButton::indicator:pressed {\n"
"    image: url(:/Av Gostei/images/RBotaoGostei_pressed_pag3.png);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Av Gostei/images/RBotaoGostei_checked_pag3.png);\n"
"}\n"
"")
        self.botaoGostei_pag3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.botaoGostei_pag3.setText("")
        self.botaoGostei_pag3.setObjectName("botaoGostei_pag3")
        self.botaoNGostei_pag3 = QtWidgets.QRadioButton(self.frame_4)
        self.botaoNGostei_pag3.setGeometry(QtCore.QRect(390, 60, 61, 61))
        self.botaoNGostei_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoNGostei_pag3.setStyleSheet("QRadioButton::indicator {\n"
"    background: transparent;\n"
"    image: url(:/Av NGostei/images/RBotaoNGostei_pag3.png);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    image: url(:/Av NGostei/images/RBotaoNGostei_hover_pag3.png);\n"
"}\n"
"QRadioButton::indicator:pressed {\n"
"    image: url(:/Av NGostei/images/RBotaoNGostei_pressed_pag3.png);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Av NGostei/images/RBotaoNGostei_checked_pag3.png);\n"
"}\n"
"")
        self.botaoNGostei_pag3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.botaoNGostei_pag3.setText("")
        self.botaoNGostei_pag3.setObjectName("botaoNGostei_pag3")
        self.labelAvaliar_pag3 = QtWidgets.QLabel(self.frame_4)
        self.labelAvaliar_pag3.setGeometry(QtCore.QRect(40, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelAvaliar_pag3.setFont(font)
        self.labelAvaliar_pag3.setStyleSheet("color: rgb(255, 230, 219);")
        self.labelAvaliar_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvaliar_pag3.setObjectName("labelAvaliar_pag3")
        self.textAvaliar_pag3 = QtWidgets.QTextEdit(self.frame_4)
        self.textAvaliar_pag3.setGeometry(QtCore.QRect(40, 140, 411, 241))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.textAvaliar_pag3.setFont(font)
        self.textAvaliar_pag3.setStyleSheet("QTextEdit {\n"
"    border: 2px solid rgb(175, 54, 38);\n"
"    border-radius: 9px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 230, 219);\n"
"}")
        self.textAvaliar_pag3.setObjectName("textAvaliar_pag3")
        self.botaoFechar_pag3 = QtWidgets.QPushButton(self.frame_4)
        self.botaoFechar_pag3.setGeometry(QtCore.QRect(40, 465, 91, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.botaoFechar_pag3.setFont(font)
        self.botaoFechar_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoFechar_pag3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(12, 14, 28);\n"
"    border: 2px solid rgb(12, 14, 28);\n"
"    border-radius: 5px;\n"
"    color: rgb(219, 149, 121);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(23, 19, 48);\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rbg(250, 270, 200);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.botaoFechar_pag3.setObjectName("botaoFechar_pag3")
        self.botaoSubmeter_pag3 = QtWidgets.QPushButton(self.frame_4)
        self.botaoSubmeter_pag3.setGeometry(QtCore.QRect(280, 465, 171, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.botaoSubmeter_pag3.setFont(font)
        self.botaoSubmeter_pag3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoSubmeter_pag3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(105, 31, 21);\n"
"    border: 2px solid rgb(77, 21, 13);\n"
"    border-radius: 5px;\n"
"    color: rgb(219, 149, 121);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(141, 44, 31);\n"
"    border: 2px solid rgb(105, 32, 22);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(24, 22, 35);\n"
"    border: 2px solid rgb(219, 149, 121);\n"
"}")
        self.botaoSubmeter_pag3.setObjectName("botaoSubmeter_pag3")
        self.labelTempoJogo_pag3 = QtWidgets.QLabel(self.frame_4)
        self.labelTempoJogo_pag3.setGeometry(QtCore.QRect(130, 400, 151, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelTempoJogo_pag3.setFont(font)
        self.labelTempoJogo_pag3.setStyleSheet("color: rgb(255, 230, 219);")
        self.labelTempoJogo_pag3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTempoJogo_pag3.setObjectName("labelTempoJogo_pag3")
        self.DSPContador_pag3 = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.DSPContador_pag3.setGeometry(QtCore.QRect(290, 400, 161, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(9)
        self.DSPContador_pag3.setFont(font)
        self.DSPContador_pag3.setStyleSheet("QDoubleSpinBox {\n"
"    border: 2px solid rgb(175, 54, 38); \n"
"    border-radius: 5px;\n"
"    color: rgb(255, 230, 219);\n"
"    padding: 5px;\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"    background-color: transparent;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"    image: url(:/Setas/images/UpArrow-TextEdit_pag3.png);\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"    background-color: transparent;\n"
"}\n"
"QDoubleSpinBox::down-arrow {\n"
"    image: url(:/Setas/images/DownArrow-TextEdit_pag3.png);\n"
"}\n"
"\n"
"")
        self.DSPContador_pag3.setObjectName("DSPContador_pag3")
        self.DSPContador_pag3.setMaximum(10000.00)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame_1)
        self.horizontalLayout.addWidget(self.frame)
        SuperbAvaliar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuperbAvaliar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 26))
        self.menubar.setObjectName("menubar")
        SuperbAvaliar.setMenuBar(self.menubar)

        self.retranslateUi(SuperbAvaliar)
        QtCore.QMetaObject.connectSlotsByName(SuperbAvaliar)

    def retranslateUi(self, SuperbAvaliar):
        _translate = QtCore.QCoreApplication.translate
        SuperbAvaliar.setWindowTitle(_translate("SuperbAvaliar", "Superb"))
        self.labelNomeJogo_pag3.setText(_translate("SuperbAvaliar", "*"))
        self.labelAvaliar_pag3.setText(_translate("SuperbAvaliar", "Avaliação:"))
        self.botaoFechar_pag3.setText(_translate("SuperbAvaliar", "VOLTAR"))
        self.botaoSubmeter_pag3.setText(_translate("SuperbAvaliar", "SUBMETER"))
        self.labelTempoJogo_pag3.setText(_translate("SuperbAvaliar", "Tempo de jogo (h)"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuperbAvaliar = QtWidgets.QMainWindow()
    ui = Ui_SuperbAvaliar()
    ui.setupUi(SuperbAvaliar)
    SuperbAvaliar.show()
    sys.exit(app.exec_())

