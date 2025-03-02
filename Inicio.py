

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1260, 820)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1010, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton#pushButton_3 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(60, 60, 60, 255));\n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"border-image: url(:/images/invisible.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(80, 80, 80, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 272, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,0)")
        self.label_4.setObjectName("label_4")
        self.lineEditContrasenia = QtWidgets.QLineEdit(Form)
        self.lineEditContrasenia.setGeometry(QtCore.QRect(550, 370, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditContrasenia.setFont(font)
        self.lineEditContrasenia.setStyleSheet("background-color: rgba(80, 80, 80, 255);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEditContrasenia.setText("")
        self.lineEditContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditContrasenia.setObjectName("lineEditContrasenia")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 461, 141))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,0)")
        self.label_3.setObjectName("label_3")
        self.lineEditUsuario = QtWidgets.QLineEdit(Form)
        self.lineEditUsuario.setGeometry(QtCore.QRect(550, 280, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditUsuario.setFont(font)
        self.lineEditUsuario.setStyleSheet("background-color: rgba(80, 80, 80, 255);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEditUsuario.setText("")
        self.lineEditUsuario.setMaxLength(32788)
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.forgotPasswordButton = QtWidgets.QPushButton(Form)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(180, 660, 372, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.forgotPasswordButton.setFont(font)
        self.forgotPasswordButton.setStyleSheet("QPushButton#forgotPasswordButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(60, 60, 60, 255));\n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#forgotPasswordButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(80, 80, 80, 255));\n"
"}\n"
"\n"
"QPushButton#forgotPasswordButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120, 255);\n"
"}\n"
"")
        self.forgotPasswordButton.setObjectName("forgotPasswordButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 360, 271, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0,0,0,0)")
        self.label_5.setObjectName("label_5")
        self.pushButtonIngresar = QtWidgets.QPushButton(Form)
        self.pushButtonIngresar.setGeometry(QtCore.QRect(700, 460, 260, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonIngresar.setFont(font)
        self.pushButtonIngresar.setStyleSheet("QPushButton#pushButtonIngresar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(60, 60, 60, 255));\n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonIngresar:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(80, 80, 80, 255));\n"
"}\n"
"\n"
"QPushButton#pushButtonIngresar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120, 255);\n"
"}\n"
"")
        self.pushButtonIngresar.setObjectName("pushButtonIngresar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1261, 821))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/images/images/fondo2.png);\n"
"border-top-left-radius: 7px;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButtonVer = QtWidgets.QPushButton(Form)
        self.pushButtonVer.setGeometry(QtCore.QRect(1010, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonVer.setFont(font)
        self.pushButtonVer.setStyleSheet("\n"
"QPushButton#pushButtonVer {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(60, 60, 60, 255));\n"
"    color: rgba(255, 255, 255, 255);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"border-image: url(:/images/images/ojo.png);\n"
"}\n"
"\n"
"QPushButton#pushButtonVer:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(80, 80, 80, 255));\n"
"}\n"
"\n"
"QPushButton#pushButtonVer:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"")
        self.pushButtonVer.setText("")
        self.pushButtonVer.setObjectName("pushButtonVer")
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.label_4.raise_()
        self.lineEditContrasenia.raise_()
        self.label_3.raise_()
        self.lineEditUsuario.raise_()
        self.forgotPasswordButton.raise_()
        self.label_5.raise_()
        self.pushButtonIngresar.raise_()
        self.pushButtonVer.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inicio"))
        self.label_4.setText(_translate("Form", "Usuario:"))
        self.lineEditContrasenia.setPlaceholderText(_translate("Form", "Ingrese Contraseña"))
        self.label_3.setText(_translate("Form", "VETERINARIA"))
        self.lineEditUsuario.setPlaceholderText(_translate("Form", "Ingrese Usuario"))
        self.forgotPasswordButton.setText(_translate("Form", "¿Olvidaste Tu Contraseña?"))
        self.label_5.setText(_translate("Form", "Contraseña: "))
        self.pushButtonIngresar.setText(_translate("Form", "Ingresar"))
import data_rc



