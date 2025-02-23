# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuperbLogin(object):
    def setupUi(self, SuperbLogin):
        SuperbLogin.setObjectName("SuperbLogin")
        SuperbLogin.resize(870, 571)
        SuperbLogin.setMinimumSize(QtCore.QSize(870, 571))
        SuperbLogin.setMaximumSize(QtCore.QSize(870, 571))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone Site/images/icone site.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SuperbLogin.setWindowIcon(icon)
        SuperbLogin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SuperbLogin)
        self.centralwidget.setMinimumSize(QtCore.QSize(870, 545))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cabecalho = QtWidgets.QFrame(self.centralwidget)
        self.cabecalho.setMaximumSize(QtCore.QSize(16777215, 55))
        self.cabecalho.setStyleSheet("background-color: rgb(13, 15, 31);")
        self.cabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cabecalho.setObjectName("cabecalho")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cabecalho)
        self.horizontalLayout_2.setContentsMargins(11, 9, 11, 9)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_error = QtWidgets.QFrame(self.cabecalho)
        self.login_error.setMaximumSize(QtCore.QSize(515, 16777215))
        self.login_error.setStyleSheet("background-color: rgb(24, 22, 35);\n"
"color: rgb(219, 149, 121);")
        self.login_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_error.setObjectName("login_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.login_error)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.texto_erro_login = QtWidgets.QLabel(self.login_error)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.texto_erro_login.setFont(font)
        self.texto_erro_login.setAlignment(QtCore.Qt.AlignCenter)
        self.texto_erro_login.setObjectName("texto_erro_login")
        self.horizontalLayout_3.addWidget(self.texto_erro_login)
        self.fechar_cabecalho = QtWidgets.QPushButton(self.login_error)
        self.fechar_cabecalho.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fechar_cabecalho.setFont(font)
        self.fechar_cabecalho.setStyleSheet("QPushButton {\n"
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
        self.fechar_cabecalho.setObjectName("fechar_cabecalho")
        self.horizontalLayout_3.addWidget(self.fechar_cabecalho)
        self.horizontalLayout_2.addWidget(self.login_error)
        self.verticalLayout.addWidget(self.cabecalho)
        self.central = QtWidgets.QFrame(self.centralwidget)
        self.central.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.central.setFont(font)
        self.central.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(14, 33, 64, 255), stop:0.208955 rgba(39, 35, 57, 255), stop:0.830846 rgba(141, 44, 31, 255), stop:1 rgba(199, 49, 15, 255));")
        self.central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central.setObjectName("central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.conteudo = QtWidgets.QFrame(self.central)
        self.conteudo.setMaximumSize(QtCore.QSize(550, 16777215))
        self.conteudo.setStyleSheet("background-color: rgb(12, 14, 28);")
        self.conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.user = QtWidgets.QLineEdit(self.conteudo)
        self.user.setGeometry(QtCore.QRect(110, 250, 361, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.user.setFont(font)
        self.user.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(25, 28, 41);\n"
"    border-radius: 3px;\n"
"    padding: 10px;\n"
"    background-color: rgb(41, 43, 56);\n"
"    color: rgb(228, 230, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(12, 14, 28);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(199, 49, 15);\n"
"}")
        self.user.setMaxLength(12)
        self.user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.user.setClearButtonEnabled(False)
        self.user.setObjectName("user")
        self.conectar_login = QtWidgets.QPushButton(self.conteudo)
        self.conectar_login.setGeometry(QtCore.QRect(300, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.conectar_login.setFont(font)
        self.conectar_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conectar_login.setStyleSheet("QPushButton {\n"
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
        self.conectar_login.setObjectName("conectar_login")
        self.icon_user = QtWidgets.QLabel(self.conteudo)
        self.icon_user.setGeometry(QtCore.QRect(75, 250, 31, 41))
        self.icon_user.setStyleSheet("image: url(:/User/images/user.png);")
        self.icon_user.setText("")
        self.icon_user.setObjectName("icon_user")
        self.icon_senha = QtWidgets.QLabel(self.conteudo)
        self.icon_senha.setGeometry(QtCore.QRect(75, 300, 31, 41))
        self.icon_senha.setStyleSheet("image: url(:/Senha/images/senha.png);")
        self.icon_senha.setText("")
        self.icon_senha.setObjectName("icon_senha")
        self.fechar_login = QtWidgets.QPushButton(self.conteudo)
        self.fechar_login.setGeometry(QtCore.QRect(110, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.fechar_login.setFont(font)
        self.fechar_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fechar_login.setStyleSheet("QPushButton {\n"
"    background-color: rgb(24, 22, 35);\n"
"    border: 2px solid rgb(219, 149, 121);\n"
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
        self.fechar_login.setObjectName("fechar_login")
        self.logo_superb = QtWidgets.QFrame(self.conteudo)
        self.logo_superb.setGeometry(QtCore.QRect(75, 19, 400, 231))
        self.logo_superb.setStyleSheet("background-position: center;\n"
"image: url(:/Logo/images/logo.png);\n"
"background-repeat: no-repeat;")
        self.logo_superb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_superb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_superb.setObjectName("logo_superb")
        self.user_2 = QtWidgets.QLineEdit(self.conteudo)
        self.user_2.setGeometry(QtCore.QRect(110, 300, 361, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.user_2.setFont(font)
        self.user_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(25, 28, 41);\n"
"    border-radius: 3px;\n"
"    padding: 10px;\n"
"    background-color: rgb(41, 43, 56);\n"
"    color: rgb(228, 230, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(12, 14, 28);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(199, 49, 15);\n"
"}")
        self.user_2.setMaxLength(16)
        self.user_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_2.setClearButtonEnabled(False)
        self.user_2.setObjectName("user_2")
        self.horizontalLayout.addWidget(self.conteudo)
        self.verticalLayout.addWidget(self.central)
        SuperbLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuperbLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 26))
        self.menubar.setObjectName("menubar")
        SuperbLogin.setMenuBar(self.menubar)

        self.fechar_cabecalho.clicked.connect(lambda: self.cabecalho.hide())
        self.cabecalho.hide()

        self.retranslateUi(SuperbLogin)
        self.fechar_login.pressed.connect(SuperbLogin.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SuperbLogin)

    def retranslateUi(self, SuperbLogin):
        _translate = QtCore.QCoreApplication.translate
        SuperbLogin.setWindowTitle(_translate("SuperbLogin", "Superb"))
        self.texto_erro_login.setText(_translate("SuperbLogin", "Usuário/Senha não podem estar vazios."))
        self.fechar_cabecalho.setText(_translate("SuperbLogin", "X"))
        self.user.setPlaceholderText(_translate("SuperbLogin", "usuario"))
        self.conectar_login.setText(_translate("SuperbLogin", "CONECTAR À SUPERB"))
        self.fechar_login.setText(_translate("SuperbLogin", "FECHAR"))
        self.user_2.setPlaceholderText(_translate("SuperbLogin", "senha"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuperbLogin = QtWidgets.QMainWindow()
    ui = Ui_SuperbLogin()
    ui.setupUi(SuperbLogin)
    SuperbLogin.show()
    sys.exit(app.exec_())
