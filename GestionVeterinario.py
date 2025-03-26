from PyQt5 import QtCore, QtGui, QtWidgets
import data_rc
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import bcrypt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt  # Para centrar texto
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os, shutil
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5.QtWidgets import (
    QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox,QAbstractSpinBox
)


def connect_to_database():
    return mysql.connector.connect(
        host="34.70.72.185",
        port=3306,
        user="root",
        password="Jhonr2005",
        database="veterinaria"
    )


class Ui_Form(object):
    def __init__(self):
        self.client_id = None 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1258, 822)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: white;")
        self.widgetTitulo = QtWidgets.QWidget(Form)
        self.widgetTitulo.setGeometry(QtCore.QRect(0, 0, 1261, 101))
        self.widgetTitulo.setMaximumSize(QtCore.QSize(1271, 16777215))
        self.widgetTitulo.setStyleSheet("background-color: #4aa6ff; /* Azul claro */\n"
"\n"
"")
        self.widgetTitulo.setObjectName("widgetTitulo")
        self.label = QtWidgets.QLabel(self.widgetTitulo)
        self.label.setGeometry(QtCore.QRect(0, 10, 171, 81))
        self.label.setStyleSheet("image: url(:/icons/Iconos/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widgetTitulo)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widgetBarraVertical = QtWidgets.QWidget(Form)
        self.widgetBarraVertical.setGeometry(QtCore.QRect(-10, 100, 131, 751))
        self.widgetBarraVertical.setStyleSheet("background-color: #e8e9e8; /* Azul claro */")
        self.widgetBarraVertical.setObjectName("widgetBarraVertical")
        self.pushButtonGeneral = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonGeneral.setGeometry(QtCore.QRect(20, 10, 101, 81))
        self.pushButtonGeneral.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/casa-icono-silueta.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"\n"
"}\n"
"")
        self.pushButtonGeneral.setText("")
        self.pushButtonGeneral.setObjectName("pushButtonGeneral")
        self.label_5 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 111, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButtonMiPerfil = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonMiPerfil.setGeometry(QtCore.QRect(20, 130, 101, 81))
        self.pushButtonMiPerfil.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/usuario-de-perfil.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonMiPerfil.setText("")
        self.pushButtonMiPerfil.setObjectName("pushButtonMiPerfil")
        self.label_7 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 81, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButtonMascotas = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonMascotas.setGeometry(QtCore.QRect(20, 250, 101, 81))
        self.pushButtonMascotas.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/pata.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonMascotas.setText("")
        self.pushButtonMascotas.setObjectName("pushButtonMascotas")
        self.label_8 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_8.setGeometry(QtCore.QRect(30, 450, 81, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_9.setGeometry(QtCore.QRect(30, 570, 81, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButtonHistoria = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonHistoria.setGeometry(QtCore.QRect(20, 490, 101, 81))
        self.pushButtonHistoria.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"     /* Imagen en el botón */\n"
"    \n"
"    image: url(:/images/images/diagnostico.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonHistoria.setText("")
        self.pushButtonHistoria.setObjectName("pushButtonHistoria")
        self.label_10 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_10.setGeometry(QtCore.QRect(20, 690, 101, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButtonCitas_2 = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonCitas_2.setGeometry(QtCore.QRect(20, 370, 101, 81))
        self.pushButtonCitas_2.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    \n"
"    image: url(:/images/images/cita-medica.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonCitas_2.setText("")
        self.pushButtonCitas_2.setObjectName("pushButtonCitas_2")
        self.pushButtonPagos = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonPagos.setGeometry(QtCore.QRect(20, 600, 101, 81))
        self.pushButtonPagos.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    \n"
"    image: url(:/images/images/poder.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonPagos.setText("")
        self.pushButtonPagos.setObjectName("pushButtonPagos")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 100, 1171, 741))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageGeneral = QtWidgets.QWidget()
        self.pageGeneral.setObjectName("pageGeneral")
        self.widgetDinero = QtWidgets.QWidget(self.pageGeneral)
        self.widgetDinero.setGeometry(QtCore.QRect(90, 110, 641, 131))
        self.widgetDinero.setStyleSheet("QWidget#widgetDinero {\n"
"background-color: #a8daff; /* Azul claro */\n"
"border-radius: 15px; /* Borde redondeado */\n"
"border: 2px solid #808080; /* Borde gris */\n"
"background-position: right center; /* Coloca la imagen en el lado derecho */\n"
"background-repeat: no-repeat; /* No repite la imagen */\n"
"padding-right: 40px; /* Espacio adicional para evitar que el contenido se superponga con la imagen */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.widgetDinero.setObjectName("widgetDinero")
        self.lineEditDineroCaja = QtWidgets.QLineEdit(self.widgetDinero)
        self.lineEditDineroCaja.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.lineEditDineroCaja.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"border: 2px solid #a8daff; /* Borde gris */")
        self.lineEditDineroCaja.setObjectName("lineEditDineroCaja")
        self.label_3 = QtWidgets.QLabel(self.widgetDinero)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_3.setObjectName("label_3")
        self.lineEditMesDineroEnCaja = QtWidgets.QLineEdit(self.widgetDinero)
        self.lineEditMesDineroEnCaja.setGeometry(QtCore.QRect(180, 10, 121, 31))
        self.lineEditMesDineroEnCaja.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"border: 2px solid #a8daff; /* Borde gris */")
        self.lineEditMesDineroEnCaja.setObjectName("lineEditMesDineroEnCaja")
        self.DatoCurioso = QtWidgets.QLabel(self.widgetDinero)
        self.DatoCurioso.setGeometry(QtCore.QRect(20, 40, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DatoCurioso.setFont(font)
        self.DatoCurioso.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DatoCurioso.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.DatoCurioso.setText("")
        self.DatoCurioso.setObjectName("DatoCurioso")
        self.widgetCitasCompletadas = QtWidgets.QWidget(self.pageGeneral)
        self.widgetCitasCompletadas.setGeometry(QtCore.QRect(100, 310, 281, 191))
        self.widgetCitasCompletadas.setStyleSheet("QWidget#widgetCitasCompletadas {\n"
"background-color: #e7e4e4; /* Azul claro */\n"
"border-radius: 15px; /* Borde redondeado */\n"
"border: 2px solid #808080; /* Borde gris */\n"
"background-position: right center; /* Coloca la imagen en el lado derecho */\n"
"background-repeat: no-repeat; /* No repite la imagen */\n"
"padding-right: 40px; /* Espacio adicional para evitar que el contenido se superponga con la imagen */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.widgetCitasCompletadas.setObjectName("widgetCitasCompletadas")
        self.label_13 = QtWidgets.QLabel(self.widgetCitasCompletadas)
        self.label_13.setGeometry(QtCore.QRect(70, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("background-color: #e7e4e4; /* Azul claro */")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widgetCitasCompletadas)
        self.label_14.setGeometry(QtCore.QRect(60, 50, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("background-color: #e7e4e4; /* Azul claro */\n"
"image: url(:/images/images/completada.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.lcdNumberCitasCompletadas = QtWidgets.QLCDNumber(self.widgetCitasCompletadas)
        self.lcdNumberCitasCompletadas.setGeometry(QtCore.QRect(100, 150, 64, 23))
        self.lcdNumberCitasCompletadas.setObjectName("lcdNumberCitasCompletadas")
        self.widgetCitasAgendadas = QtWidgets.QWidget(self.pageGeneral)
        self.widgetCitasAgendadas.setGeometry(QtCore.QRect(450, 310, 281, 191))
        self.widgetCitasAgendadas.setStyleSheet("QWidget#widgetCitasAgendadas {\n"
"background-color: #e7e4e4; /* Azul claro */\n"
"border-radius: 15px; /* Borde redondeado */\n"
"border: 2px solid #808080; /* Borde gris */\n"
"background-position: right center; /* Coloca la imagen en el lado derecho */\n"
"background-repeat: no-repeat; /* No repite la imagen */\n"
"padding-right: 40px; /* Espacio adicional para evitar que el contenido se superponga con la imagen */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.widgetCitasAgendadas.setObjectName("widgetCitasAgendadas")
        self.label_15 = QtWidgets.QLabel(self.widgetCitasAgendadas)
        self.label_15.setGeometry(QtCore.QRect(80, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet("background-color: #e7e4e4; /* Azul claro */")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widgetCitasAgendadas)
        self.label_16.setGeometry(QtCore.QRect(60, 50, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet("background-color: #e7e4e4; /* Azul claro */\n"
"image: url(:/images/images/reloj.png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.lcdNumberCitasAgendadas = QtWidgets.QLCDNumber(self.widgetCitasAgendadas)
        self.lcdNumberCitasAgendadas.setGeometry(QtCore.QRect(110, 150, 64, 23))
        self.lcdNumberCitasAgendadas.setObjectName("lcdNumberCitasAgendadas")
        self.widgetAnimales = QtWidgets.QWidget(self.pageGeneral)
        self.widgetAnimales.setGeometry(QtCore.QRect(780, 110, 281, 451))
        self.widgetAnimales.setStyleSheet("QWidget#widgetAnimales {\n"
"background-color: #a8daff; /* Azul claro */\n"
"border-radius: 15px; /* Borde redondeado */\n"
"border: 2px solid #808080; /* Borde gris */\n"
"background-position: right center; /* Coloca la imagen en el lado derecho */\n"
"background-repeat: no-repeat; /* No repite la imagen */\n"
"padding-right: 40px; /* Espacio adicional para evitar que el contenido se superponga con la imagen */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.widgetAnimales.setObjectName("widgetAnimales")
        self.label_17 = QtWidgets.QLabel(self.widgetAnimales)
        self.label_17.setGeometry(QtCore.QRect(70, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widgetAnimales)
        self.label_18.setGeometry(QtCore.QRect(60, 70, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:/images/images/perro.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.lcdNumberPerros = QtWidgets.QLCDNumber(self.widgetAnimales)
        self.lcdNumberPerros.setGeometry(QtCore.QRect(110, 180, 64, 23))
        self.lcdNumberPerros.setObjectName("lcdNumberPerros")
        self.lcdNumberGatos = QtWidgets.QLCDNumber(self.widgetAnimales)
        self.lcdNumberGatos.setGeometry(QtCore.QRect(110, 390, 64, 23))
        self.lcdNumberGatos.setObjectName("lcdNumberGatos")
        self.label_19 = QtWidgets.QLabel(self.widgetAnimales)
        self.label_19.setGeometry(QtCore.QRect(60, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:/images/images/gato.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.widgetAnimales)
        self.label_22.setGeometry(QtCore.QRect(120, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widgetAnimales)
        self.label_23.setGeometry(QtCore.QRect(120, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_23.setObjectName("label_23")
        self.labelFecha = QtWidgets.QLabel(self.pageGeneral)
        self.labelFecha.setGeometry(QtCore.QRect(260, 250, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFecha.setFont(font)
        self.labelFecha.setObjectName("labelFecha")
        self.stackedWidget.addWidget(self.pageGeneral)
        self.pageAgregarUsuarios = QtWidgets.QWidget()
        self.pageAgregarUsuarios.setObjectName("pageAgregarUsuarios")
        self.label_11 = QtWidgets.QLabel(self.pageAgregarUsuarios)
        self.label_11.setGeometry(QtCore.QRect(450, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayoutWidget = QtWidgets.QWidget(self.pageAgregarUsuarios)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 130, 811, 378))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(1, 0, 0, 0)
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEditUsuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditUsuario.setFont(font)
        self.lineEditUsuario.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsuario)
        self.label_93 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_93)
        self.lineEditContrasenia = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditContrasenia.setFont(font)
        self.lineEditContrasenia.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditContrasenia.setObjectName("lineEditContrasenia")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditContrasenia)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEditNombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombre.setFont(font)
        self.lineEditNombre.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditNombre)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEditCedula = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedula.setFont(font)
        self.lineEditCedula.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedula.setObjectName("lineEditCedula")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditCedula)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEditCorreo = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCorreo.setFont(font)
        self.lineEditCorreo.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCorreo.setObjectName("lineEditCorreo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditCorreo)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEditTelefono_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTelefono_2.setFont(font)
        self.lineEditTelefono_2.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTelefono_2.setObjectName("lineEditTelefono_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditTelefono_2)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEditDireccion = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDireccion.setFont(font)
        self.lineEditDireccion.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditDireccion.setObjectName("lineEditDireccion")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditDireccion)
        self.pushButtonRegresarRegistrar = QtWidgets.QPushButton(self.pageAgregarUsuarios)
        self.pushButtonRegresarRegistrar.setGeometry(QtCore.QRect(300, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarRegistrar.setFont(font)
        self.pushButtonRegresarRegistrar.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarRegistrar.setObjectName("pushButtonRegresarRegistrar")
        self.pushButtonModificar = QtWidgets.QPushButton(self.pageAgregarUsuarios)
        self.pushButtonModificar.setGeometry(QtCore.QRect(530, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonModificar.setFont(font)
        self.pushButtonModificar.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonModificar.setObjectName("pushButtonModificar")
        self.stackedWidget.addWidget(self.pageAgregarUsuarios)
        self.pageListaUsuariosMascotas = QtWidgets.QWidget()
        self.pageListaUsuariosMascotas.setObjectName("pageListaUsuariosMascotas")
        self.label_36 = QtWidgets.QLabel(self.pageListaUsuariosMascotas)
        self.label_36.setGeometry(QtCore.QRect(440, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.pageListaUsuariosMascotas)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(190, 60, 731, 182))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setHorizontalSpacing(7)
        self.formLayout_4.setVerticalSpacing(16)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_45 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.lineEditNombreMascota = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreMascota.setFont(font)
        self.lineEditNombreMascota.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreMascota.setObjectName("lineEditNombreMascota")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreMascota)
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.comboBoxTipoEspecieLista = QtWidgets.QComboBox(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxTipoEspecieLista.setFont(font)
        self.comboBoxTipoEspecieLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxTipoEspecieLista.setObjectName("comboBoxTipoEspecieLista")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxTipoEspecieLista)
        self.label_44 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.lineEditRazaLista = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaLista.setFont(font)
        self.lineEditRazaLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaLista.setObjectName("lineEditRazaLista")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaLista)
        self.tableWidgetListaMascotas = QtWidgets.QTableWidget(self.pageListaUsuariosMascotas)
        self.tableWidgetListaMascotas.setGeometry(QtCore.QRect(145, 260, 861, 331))
        self.tableWidgetListaMascotas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetListaMascotas.setObjectName("tableWidgetListaMascotas")
        self.tableWidgetListaMascotas.setColumnCount(0)
        self.tableWidgetListaMascotas.setRowCount(0)
        self.pushButtonRegresarLista = QtWidgets.QPushButton(self.pageListaUsuariosMascotas)
        self.pushButtonRegresarLista.setGeometry(QtCore.QRect(320, 620, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresarLista.setFont(font)
        self.pushButtonRegresarLista.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarLista.setObjectName("pushButtonRegresarLista")
        self.pushButtonAbrirLista = QtWidgets.QPushButton(self.pageListaUsuariosMascotas)
        self.pushButtonAbrirLista.setGeometry(QtCore.QRect(580, 620, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonAbrirLista.setFont(font)
        self.pushButtonAbrirLista.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonAbrirLista.setObjectName("pushButtonAbrirLista")
        self.stackedWidget.addWidget(self.pageListaUsuariosMascotas)
        self.pageDetallesPropietario = QtWidgets.QWidget()
        self.pageDetallesPropietario.setObjectName("pageDetallesPropietario")
        self.label_37 = QtWidgets.QLabel(self.pageDetallesPropietario)
        self.label_37.setGeometry(QtCore.QRect(370, -10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.pageDetallesPropietario)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(110, 310, 431, 250))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEditNombreMascotaDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreMascotaDetalles.setFont(font)
        self.lineEditNombreMascotaDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreMascotaDetalles.setObjectName("lineEditNombreMascotaDetalles")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreMascotaDetalles)
        self.lineEditEspeciesDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditEspeciesDetalles.setFont(font)
        self.lineEditEspeciesDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditEspeciesDetalles.setObjectName("lineEditEspeciesDetalles")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditEspeciesDetalles)
        self.lineEditRazaDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaDetalles.setFont(font)
        self.lineEditRazaDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaDetalles.setObjectName("lineEditRazaDetalles")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaDetalles)
        self.lineEditColorDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditColorDetalles.setFont(font)
        self.lineEditColorDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditColorDetalles.setObjectName("lineEditColorDetalles")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditColorDetalles)
        self.label_101 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_101)
        self.label_107 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_107.setFont(font)
        self.label_107.setObjectName("label_107")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_107)
        self.label_106 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_106.setFont(font)
        self.label_106.setObjectName("label_106")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_106)
        self.label_108 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_108.setFont(font)
        self.label_108.setObjectName("label_108")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_108)
        self.label_105 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_105.setFont(font)
        self.label_105.setObjectName("label_105")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_105)
        self.label_104 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_104.setFont(font)
        self.label_104.setObjectName("label_104")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_104)
        self.lineEditTamanioDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTamanioDetalles.setFont(font)
        self.lineEditTamanioDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTamanioDetalles.setObjectName("lineEditTamanioDetalles")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditTamanioDetalles)
        self.lineEditfechaNacimientoDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditfechaNacimientoDetalles.setFont(font)
        self.lineEditfechaNacimientoDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditfechaNacimientoDetalles.setObjectName("lineEditfechaNacimientoDetalles")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditfechaNacimientoDetalles)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.pageDetallesPropietario)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(110, 40, 811, 211))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_46 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.lineEditNombreDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreDetalles.setFont(font)
        self.lineEditNombreDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreDetalles.setObjectName("lineEditNombreDetalles")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreDetalles)
        self.label_47 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.lineEditCedulaDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaDetalles.setFont(font)
        self.lineEditCedulaDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaDetalles.setObjectName("lineEditCedulaDetalles")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaDetalles)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.lineEditCorreoDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCorreoDetalles.setFont(font)
        self.lineEditCorreoDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCorreoDetalles.setObjectName("lineEditCorreoDetalles")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditCorreoDetalles)
        self.label_50 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.lineEditTelefonoDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTelefonoDetalles.setFont(font)
        self.lineEditTelefonoDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTelefonoDetalles.setObjectName("lineEditTelefonoDetalles")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditTelefonoDetalles)
        self.label_32 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.lineEditDireccion_2 = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDireccion_2.setFont(font)
        self.lineEditDireccion_2.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditDireccion_2.setObjectName("lineEditDireccion_2")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditDireccion_2)
        self.label_52 = QtWidgets.QLabel(self.pageDetallesPropietario)
        self.label_52.setGeometry(QtCore.QRect(410, 270, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.labelFotoMascota = QtWidgets.QLabel(self.pageDetallesPropietario)
        self.labelFotoMascota.setGeometry(QtCore.QRect(580, 310, 351, 251))
        self.labelFotoMascota.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.labelFotoMascota.setFrameShape(QtWidgets.QFrame.Box)
        self.labelFotoMascota.setText("")
        self.labelFotoMascota.setObjectName("labelFotoMascota")
        self.pushButtonRegresarDetalles = QtWidgets.QPushButton(self.pageDetallesPropietario)
        self.pushButtonRegresarDetalles.setGeometry(QtCore.QRect(420, 600, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresarDetalles.setFont(font)
        self.pushButtonRegresarDetalles.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarDetalles.setObjectName("pushButtonRegresarDetalles")
        self.stackedWidget.addWidget(self.pageDetallesPropietario)
        self.pageTarifas = QtWidgets.QWidget()
        self.pageTarifas.setObjectName("pageTarifas")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.pageTarifas)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(180, 60, 731, 151))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setHorizontalSpacing(7)
        self.formLayout_6.setVerticalSpacing(16)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_53 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.lineEditCedulaCitas = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaCitas.setFont(font)
        self.lineEditCedulaCitas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaCitas.setObjectName("lineEditCedulaCitas")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaCitas)
        self.label_54 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.lineEditNombreCitas = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreCitas.setFont(font)
        self.lineEditNombreCitas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreCitas.setObjectName("lineEditNombreCitas")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreCitas)
        self.label_57 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.lineEditRazaCitas = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaCitas.setFont(font)
        self.lineEditRazaCitas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaCitas.setObjectName("lineEditRazaCitas")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaCitas)
        self.pushButtonRegresarCitas = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonRegresarCitas.setGeometry(QtCore.QRect(240, 630, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresarCitas.setFont(font)
        self.pushButtonRegresarCitas.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarCitas.setObjectName("pushButtonRegresarCitas")
        self.tableWidgetListaCitas = QtWidgets.QTableWidget(self.pageTarifas)
        self.tableWidgetListaCitas.setGeometry(QtCore.QRect(140, 220, 861, 331))
        self.tableWidgetListaCitas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetListaCitas.setObjectName("tableWidgetListaCitas")
        self.tableWidgetListaCitas.setColumnCount(0)
        self.tableWidgetListaCitas.setRowCount(0)
        self.pushButtonDetallesCita = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonDetallesCita.setGeometry(QtCore.QRect(480, 630, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonDetallesCita.setFont(font)
        self.pushButtonDetallesCita.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonDetallesCita.setObjectName("pushButtonDetallesCita")
        self.label_38 = QtWidgets.QLabel(self.pageTarifas)
        self.label_38.setGeometry(QtCore.QRect(470, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.pushButtonAtender = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonAtender.setGeometry(QtCore.QRect(720, 630, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonAtender.setFont(font)
        self.pushButtonAtender.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonAtender.setObjectName("pushButtonAtender")
        self.pushButtonMisCitas = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonMisCitas.setGeometry(QtCore.QRect(480, 560, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonMisCitas.setFont(font)
        self.pushButtonMisCitas.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonMisCitas.setObjectName("pushButtonMisCitas")
        self.stackedWidget.addWidget(self.pageTarifas)
        self.pageDetallesContaduria = QtWidgets.QWidget()
        self.pageDetallesContaduria.setObjectName("pageDetallesContaduria")
        self.label_75 = QtWidgets.QLabel(self.pageDetallesContaduria)
        self.label_75.setGeometry(QtCore.QRect(430, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.pageDetallesContaduria)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(130, 70, 841, 501))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_10 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setVerticalSpacing(11)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_80 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_80)
        self.lineEditNombreDetallesCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreDetallesCita.setFont(font)
        self.lineEditNombreDetallesCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreDetallesCita.setObjectName("lineEditNombreDetallesCita")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreDetallesCita)
        self.label_81 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_81)
        self.lineEditCedulaDetallesCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaDetallesCita.setFont(font)
        self.lineEditCedulaDetallesCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaDetallesCita.setObjectName("lineEditCedulaDetallesCita")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaDetallesCita)
        self.label_82 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_82)
        self.lineEditTelefonoDetallesCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTelefonoDetallesCita.setFont(font)
        self.lineEditTelefonoDetallesCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTelefonoDetallesCita.setObjectName("lineEditTelefonoDetallesCita")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditTelefonoDetallesCita)
        self.label_83 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_83)
        self.lineEditDireccionDetallesCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDireccionDetallesCita.setFont(font)
        self.lineEditDireccionDetallesCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditDireccionDetallesCita.setObjectName("lineEditDireccionDetallesCita")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditDireccionDetallesCita)
        self.label_85 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.lineEditNombreMascotaCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreMascotaCita.setFont(font)
        self.lineEditNombreMascotaCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreMascotaCita.setObjectName("lineEditNombreMascotaCita")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreMascotaCita)
        self.label_76 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_76)
        self.lineEditRazaCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaCita.setFont(font)
        self.lineEditRazaCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaCita.setObjectName("lineEditRazaCita")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaCita)
        self.label_77 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_77)
        self.lineEditServicioDetallesCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServicioDetallesCita.setFont(font)
        self.lineEditServicioDetallesCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditServicioDetallesCita.setObjectName("lineEditServicioDetallesCita")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditServicioDetallesCita)
        self.label_79 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_79)
        self.lineEditEstadoCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditEstadoCita.setFont(font)
        self.lineEditEstadoCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditEstadoCita.setObjectName("lineEditEstadoCita")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditEstadoCita)
        self.label_84 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_84)
        self.lineEditFechaCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditFechaCita.setFont(font)
        self.lineEditFechaCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditFechaCita.setObjectName("lineEditFechaCita")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEditFechaCita)
        self.label_86 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_86)
        self.lineEditHoraCita = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditHoraCita.setFont(font)
        self.lineEditHoraCita.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditHoraCita.setObjectName("lineEditHoraCita")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEditHoraCita)
        self.pushButtonAsignarCita = QtWidgets.QPushButton(self.pageDetallesContaduria)
        self.pushButtonAsignarCita.setGeometry(QtCore.QRect(580, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonAsignarCita.setFont(font)
        self.pushButtonAsignarCita.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonAsignarCita.setObjectName("pushButtonAsignarCita")
        self.pushButtonRegresarDetallesCita = QtWidgets.QPushButton(self.pageDetallesContaduria)
        self.pushButtonRegresarDetallesCita.setGeometry(QtCore.QRect(350, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarDetallesCita.setFont(font)
        self.pushButtonRegresarDetallesCita.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarDetallesCita.setObjectName("pushButtonRegresarDetallesCita")
        self.stackedWidget.addWidget(self.pageDetallesContaduria)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButtonGuardar = QtWidgets.QPushButton(self.page)
        self.pushButtonGuardar.setGeometry(QtCore.QRect(570, 630, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonGuardar.setFont(font)
        self.pushButtonGuardar.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonGuardar.setObjectName("pushButtonGuardar")
        self.label_59 = QtWidgets.QLabel(self.page)
        self.label_59.setGeometry(QtCore.QRect(440, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.formLayoutWidget_12 = QtWidgets.QWidget(self.page)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(130, 60, 821, 166))
        self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
        self.formLayout_12 = QtWidgets.QFormLayout(self.formLayoutWidget_12)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.formLayout_12.setVerticalSpacing(8)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_65 = QtWidgets.QLabel(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_65)
        self.lineEditUsuarioProductos = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditUsuarioProductos.setFont(font)
        self.lineEditUsuarioProductos.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditUsuarioProductos.setObjectName("lineEditUsuarioProductos")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsuarioProductos)
        self.label_87 = QtWidgets.QLabel(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_87)
        self.lineEditNombreMascotaCita_2 = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreMascotaCita_2.setFont(font)
        self.lineEditNombreMascotaCita_2.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreMascotaCita_2.setObjectName("lineEditNombreMascotaCita_2")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreMascotaCita_2)
        self.label_78 = QtWidgets.QLabel(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_78)
        self.label_90 = QtWidgets.QLabel(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_90)
        self.lineEditEspecie = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditEspecie.setFont(font)
        self.lineEditEspecie.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditEspecie.setObjectName("lineEditEspecie")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditEspecie)
        self.lineEditServicio = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServicio.setFont(font)
        self.lineEditServicio.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditServicio.setObjectName("lineEditServicio")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditServicio)
        self.pushButtonRegresarVentas = QtWidgets.QPushButton(self.page)
        self.pushButtonRegresarVentas.setGeometry(QtCore.QRect(330, 630, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresarVentas.setFont(font)
        self.pushButtonRegresarVentas.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b0b5b0; /* Color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8f938f; /* Color al hacer clic */\n"
"}\n"
"")
        self.pushButtonRegresarVentas.setObjectName("pushButtonRegresarVentas")
        self.textEditAnotaciones = QtWidgets.QTextEdit(self.page)
        self.textEditAnotaciones.setGeometry(QtCore.QRect(110, 280, 941, 281))
        self.textEditAnotaciones.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.textEditAnotaciones.setObjectName("textEditAnotaciones")
        self.label_91 = QtWidgets.QLabel(self.page)
        self.label_91.setGeometry(QtCore.QRect(460, 240, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.stackedWidget.addWidget(self.page)
        self.widgetBarraVertical.raise_()
        self.widgetTitulo.raise_()
        self.stackedWidget.raise_()
        self.configurar_botones()
        self.cargar_datos_usuario()
        self.pushButtonModificar.clicked.connect(self.modificar_usuario)
        self.cargar_lista_mascotas()
        self.llenar_combo_especies()
        self.conectar_filtros_lista()       
        self.conectar_boton_abrir()     
        self.configurar_label_foto()
        self.cargar_foto_mascota_desde_bd()
        self.cargar_citas()
        self.conectar_boton_abrir_cita()
        self.pushButtonAsignarCita.clicked.connect(self.asignar_cita_a_mi)
        self.pushButtonMisCitas.clicked.connect(self.cargar_citas_veterinario)
        self.conectar_boton_abrir_cita_asignada()
        self.conectar_boton_guardar()
        self.pushButtonPagos.clicked.connect(self.cerrar_ventana)
        
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Veterinaria"))
        self.label_2.setText(_translate("Form", "Veterinaria "))
        self.label_5.setText(_translate("Form", "General"))
        self.label_6.setText(_translate("Form", "Mi perfil"))
        self.label_7.setText(_translate("Form", "Mascotas"))
        self.label_8.setText(_translate("Form", "Citas"))
        self.label_9.setText(_translate("Form", "Historiales"))
        self.label_10.setText(_translate("Form", "Cerrar Sesión"))
        self.label_3.setText(_translate("Form", "Dato Curioso:"))
        self.label_13.setText(_translate("Form", "Citas Completadas"))
        self.label_15.setText(_translate("Form", "Citas Agendadas"))
        self.label_17.setText(_translate("Form", "Animales Atendidos"))
        self.label_22.setText(_translate("Form", "Perros"))
        self.label_23.setText(_translate("Form", "Gatos"))
        self.labelFecha.setText(_translate("Form", "Miercoles 19 de febrero 2025"))
        self.label_11.setText(_translate("Form", "Mis Datos:"))
        self.label_24.setText(_translate("Form", "Usuario:"))
        self.label_93.setText(_translate("Form", "Contraseña:"))
        self.label_12.setText(_translate("Form", "Nombre: "))
        self.label_25.setText(_translate("Form", "Cedula: "))
        self.label_26.setText(_translate("Form", "Correo:"))
        self.label_27.setText(_translate("Form", "Telefono:"))
        self.label_28.setText(_translate("Form", "Direccion:"))
        self.pushButtonRegresarRegistrar.setText(_translate("Form", "Regresar"))
        self.pushButtonModificar.setText(_translate("Form", "Modificar"))
        self.label_36.setText(_translate("Form", "Mascotas:"))
        self.label_45.setText(_translate("Form", "Nombre:"))
        self.lineEditNombreMascota.setPlaceholderText(_translate("Form", "Buscar por Nombre..."))
        self.label_43.setText(_translate("Form", "Tipo Especie:"))
        self.label_44.setText(_translate("Form", "Raza:"))
        self.lineEditRazaLista.setPlaceholderText(_translate("Form", "Buscar por raza..."))
        self.pushButtonRegresarLista.setText(_translate("Form", "Regresar"))
        self.pushButtonAbrirLista.setText(_translate("Form", "Abrir"))
        self.label_37.setText(_translate("Form", "Detalles del Propietario:"))
        self.label_101.setText(_translate("Form", "Nombre"))
        self.label_107.setText(_translate("Form", "Especie:"))
        self.label_106.setText(_translate("Form", "Raza:"))
        self.label_108.setText(_translate("Form", "Color:"))
        self.label_105.setText(_translate("Form", "Tamaño:"))
        self.label_104.setText(_translate("Form", "Fecha de Nacimiento:"))
        self.label_46.setText(_translate("Form", "Nombre: "))
        self.label_47.setText(_translate("Form", "Cedula: "))
        self.label_35.setText(_translate("Form", "Correo:"))
        self.label_50.setText(_translate("Form", "Telefono:"))
        self.label_32.setText(_translate("Form", "Direccion:"))
        self.label_52.setText(_translate("Form", "Datos Mascota:"))
        self.pushButtonRegresarDetalles.setText(_translate("Form", "Regresar"))
        self.label_53.setText(_translate("Form", "Cedula: "))
        self.lineEditCedulaCitas.setPlaceholderText(_translate("Form", "Buscar por cedula..."))
        self.label_54.setText(_translate("Form", "Nombre Cliente:"))
        self.lineEditNombreCitas.setPlaceholderText(_translate("Form", "Buscar por Nombre..."))
        self.label_57.setText(_translate("Form", "Raza:"))
        self.lineEditRazaCitas.setPlaceholderText(_translate("Form", "Buscar por raza..."))
        self.pushButtonRegresarCitas.setText(_translate("Form", "Regresar"))
        self.pushButtonDetallesCita.setText(_translate("Form", "Detalles"))
        self.label_38.setText(_translate("Form", "Citas:"))
        self.pushButtonAtender.setText(_translate("Form", "Atender"))
        self.pushButtonMisCitas.setText(_translate("Form", "Mis Citas"))
        self.label_75.setText(_translate("Form", "Detalles Cita:"))
        self.label_80.setText(_translate("Form", "Nombre: "))
        self.label_81.setText(_translate("Form", "Cedula: "))
        self.label_82.setText(_translate("Form", "Telefono:"))
        self.label_83.setText(_translate("Form", "Direccion:"))
        self.label_85.setText(_translate("Form", "Nombre Mascota:"))
        self.label_76.setText(_translate("Form", "Raza:"))
        self.label_77.setText(_translate("Form", "Servicio:"))
        self.label_79.setText(_translate("Form", "Estado:"))
        self.label_84.setText(_translate("Form", "Fecha: "))
        self.label_86.setText(_translate("Form", "Hora:"))
        self.pushButtonAsignarCita.setText(_translate("Form", "Asignarme Cita"))
        self.pushButtonRegresarDetallesCita.setText(_translate("Form", "Regresar"))
        self.pushButtonGuardar.setText(_translate("Form", "Guardar"))
        self.label_59.setText(_translate("Form", "Cita Medica:"))
        self.label_65.setText(_translate("Form", "Cliente:"))
        self.label_87.setText(_translate("Form", "Nombre Mascota:"))
        self.label_78.setText(_translate("Form", "Especie:"))
        self.label_90.setText(_translate("Form", "Servicio:"))
        self.pushButtonRegresarVentas.setText(_translate("Form", "Regresar"))
        self.label_91.setText(_translate("Form", "Anotaciones:"))

    def configurar_botones(self):
        
        """Asigna cada botón a la página correspondiente en el QStackedWidget."""
        self.pushButtonGeneral.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonMiPerfil.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButtonMascotas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButtonCitas_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButtonHistoria.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButtonPagos.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        
    def cargar_datos_usuario(self):
        """Carga los datos del cliente actualmente ingresado en la interfaz."""
        try:
            # 1️⃣ Conectar a la base de datos
            conexion = connect_to_database()
            cursor   = conexion.cursor()

            print(f"ID del cliente logueado: {self.client_id}")  # 🛠 Verificar ID antes de la consulta

            # 2️⃣ Obtener datos del usuario logueado
            query = """
                SELECT u.NombreUsuario, d.Nombre, d.Cedula, d.CorreoElectronico, d.Telefono, d.Direccion
                FROM Usuarios u
                JOIN DatosUsuarios d ON u.ID = d.UsuarioID
                WHERE u.ID = %s
            """
            print(f"Ejecutando consulta: {query} con ID {self.client_id}")  # 🛠 Verificar consulta SQL

            cursor.execute(query, (self.client_id,))
            datos = cursor.fetchone()

            if datos:
                usuario, nombre, cedula, correo, telefono, direccion = datos

                # 3️⃣ Cargar los datos en los campos de texto
                self.lineEditUsuario.setText(usuario)  # Usuario no modificable
                self.lineEditUsuario.setEnabled(False)
                self.lineEditNombre.setText(nombre)
                self.lineEditCedula.setText(cedula)
                self.lineEditCorreo.setText(correo)
                self.lineEditTelefono_2.setText(telefono)
                self.lineEditDireccion.setText(direccion)

            else:
                QMessageBox.warning(None, "Error", "No se encontraron datos para este usuario.")

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"Error al cargar datos: {err}")

        finally:
            cursor.close()
            conexion.close()


    def modificar_usuario(self):
        """Modifica los datos del cliente actualmente ingresado (incluyendo la contraseña si se ingresa)."""
        try:
            # 1️⃣ Obtener datos de la interfaz
            nombre       = self.lineEditNombre.text().strip()
            cedula       = self.lineEditCedula.text().strip()
            correo       = self.lineEditCorreo.text().strip()
            telefono     = self.lineEditTelefono_2.text().strip()
            direccion    = self.lineEditDireccion.text().strip()
            nueva_contra = self.lineEditContrasenia.text().strip()  # Nueva contraseña ingresada

            # 2️⃣ Validaciones
            if not all([nombre, cedula, correo, telefono, direccion]):
                QMessageBox.warning(None, "Error", "Por favor, llena todos los campos obligatorios.")
                return

            # 3️⃣ Conectar a la base de datos
            conexion = connect_to_database()
            cursor   = conexion.cursor()

            # 4️⃣ Actualizar los datos en la tabla DatosUsuarios
            cursor.execute("""
                UPDATE DatosUsuarios 
                SET Nombre = %s, Cedula = %s, CorreoElectronico = %s, Telefono = %s, Direccion = %s
                WHERE UsuarioID = %s
            """, (nombre, cedula, correo, telefono, direccion, self.client_id))

            # 5️⃣ Si el usuario ingresó una nueva contraseña, actualizarla en la tabla Usuarios
            if nueva_contra:
                # Generar un nuevo hash con bcrypt
                salt = bcrypt.gensalt()
                nueva_contra_cifrada = bcrypt.hashpw(nueva_contra.encode(), salt)

                cursor.execute("""
                    UPDATE Usuarios 
                    SET Contraseña = %s 
                    WHERE ID = %s
                """, (nueva_contra_cifrada, self.client_id))

            conexion.commit()

            # 6️⃣ Confirmación
            QMessageBox.information(None, "Éxito", "Tus datos han sido actualizados correctamente.")

            # 7️⃣ Limpiar los campos de la interfaz
            
            self.lineEditContrasenia.clear()  # Limpiar contraseña después de cambiarla

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudo actualizar los datos: {err}")

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
                
    def cargar_lista_mascotas(self):
        """Carga TODAS las mascotas registradas en la base de datos en la tabla."""
        conexion = connect_to_database()
        cursor = conexion.cursor()

        try:
            query = """
                SELECT m.ID, m.Nombre, m.Especie, m.Raza, m.Tamano, u.NombreUsuario, d.Cedula
                FROM Mascotas m
                JOIN Usuarios u ON m.UsuarioID = u.ID
                JOIN DatosUsuarios d ON u.ID = d.UsuarioID
                ORDER BY m.Nombre
            """
            cursor.execute(query)  # Ejecutar consulta
            registros = cursor.fetchall()

            # Configurar la tabla
            self.tableWidgetListaMascotas.setRowCount(len(registros))
            self.tableWidgetListaMascotas.setColumnCount(7)
            self.tableWidgetListaMascotas.setHorizontalHeaderLabels(
                ["ID", "Mascota", "Especie", "Raza", "Tamaño", "Dueño", "Cédula"]
            )
            self.tableWidgetListaMascotas.setSelectionBehavior(QTableWidget.SelectRows)
            self.tableWidgetListaMascotas.setEditTriggers(QTableWidget.NoEditTriggers)
            self.tableWidgetListaMascotas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # Llenar la tabla
            for row_idx, registro in enumerate(registros):
                for col_idx, dato in enumerate(registro):
                    item = QTableWidgetItem(str(dato))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidgetListaMascotas.setItem(row_idx, col_idx, item)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudieron cargar las mascotas: {err}")

        finally:
            cursor.close()
            conexion.close()

    def llenar_combo_especies(self):
        """Llena el comboBoxTipoEspecieLista con las especies disponibles en la base de datos."""
        conexion = connect_to_database()
        cursor = conexion.cursor()

        query = "SELECT DISTINCT Especie FROM Mascotas ORDER BY Especie"
        cursor.execute(query)
        especies = cursor.fetchall()

        self.comboBoxTipoEspecieLista.clear()
        self.comboBoxTipoEspecieLista.addItem("Todos")  # Opción para ver todas las especies
        for especie in especies:
            self.comboBoxTipoEspecieLista.addItem(especie[0])

        cursor.close()
        conexion.close()

    
    def filtrar_lista_usuarios_mascotas(self):
        """Filtra la lista en tiempo real según la cédula, nombre, especie y raza."""

        texto_nombre = self.lineEditNombreMascota.text().strip().lower()
        texto_especie = self.comboBoxTipoEspecieLista.currentText()
        texto_raza = self.lineEditRazaLista.text().strip().lower()

        for fila in range(self.tableWidgetListaMascotas.rowCount()):
            item_cedula = self.tableWidgetListaMascotas.item(fila, 6)  # Cédula
            item_nombre = self.tableWidgetListaMascotas.item(fila, 5)  # Dueño
            item_especie = self.tableWidgetListaMascotas.item(fila, 2)  # Especie
            item_raza = self.tableWidgetListaMascotas.item(fila, 3)  # Raza

            if item_cedula and item_nombre and item_especie and item_raza:
                nombre_coincide = texto_nombre in item_nombre.text().lower() if texto_nombre else True
                especie_coincide = texto_especie in item_especie.text() if texto_especie and texto_especie != "Todos" else True
                raza_coincide = texto_raza in item_raza.text().lower() if texto_raza else True

                self.tableWidgetListaMascotas.setRowHidden(
                    fila, not ( nombre_coincide and especie_coincide and raza_coincide)
                )

    
    def conectar_filtros_lista(self):
        """Conecta los filtros a la función de filtrado."""
        self.lineEditNombreMascota.textChanged.connect(self.filtrar_lista_usuarios_mascotas)
        self.comboBoxTipoEspecieLista.currentTextChanged.connect(self.filtrar_lista_usuarios_mascotas)
        self.lineEditRazaLista.textChanged.connect(self.filtrar_lista_usuarios_mascotas)

    def seleccionar_mascota(self):
        """Guarda el ID de la mascota seleccionada y cambia de página."""
        fila_seleccionada = self.tableWidgetListaMascotas.currentRow()

        if fila_seleccionada != -1:  # Verifica que haya una fila seleccionada
            item_id = self.tableWidgetListaMascotas.item(fila_seleccionada, 0)  # Columna ID

            if item_id:
                self.mascota_seleccionada_id = int(item_id.text())  # Guarda el ID de la mascota seleccionada
                self.stackedWidget.setCurrentIndex(3)  # Cambia a la página deseada
                self.abrir_detalles_mascota()  # Llama a la función para cargar los detalles
        else:
            QMessageBox.warning(None, "Selección requerida", "Por favor, seleccione una mascota de la lista.")

    def conectar_boton_abrir(self):
        """Conecta el botón Abrir con la función para seleccionar y abrir la mascota."""
        self.pushButtonAbrirLista.clicked.connect(self.seleccionar_mascota)


    def abrir_detalles_mascota(self):
        """Carga los detalles del propietario y la mascota seleccionada, deshabilita los campos y muestra la foto."""
        
        if not hasattr(self, 'mascota_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna mascota.")
            return

        conexion = connect_to_database()
        cursor = conexion.cursor()

        # Consultar los datos del propietario y la mascota
        query = """
            SELECT d.Nombre, d.Cedula, d.CorreoElectronico, d.Telefono, d.Direccion,
                   m.Nombre, m.Especie, m.Raza, m.Color, m.Tamano, m.FechaNacimiento, m.Foto
            FROM Mascotas m
            JOIN DatosUsuarios d ON m.UsuarioID = d.UsuarioID
            WHERE m.ID = %s
        """
        cursor.execute(query, (self.mascota_seleccionada_id,))
        datos = cursor.fetchone()

        if datos:
            (nombre, cedula, correo, telefono, direccion, 
             nombre_mascota, especie, raza, color, tamano, fecha_nacimiento, foto) = datos

            self.lineEditNombreDetalles.setText(nombre)
            self.lineEditCedulaDetalles.setText(cedula)
            self.lineEditCorreoDetalles.setText(correo)
            self.lineEditTelefonoDetalles.setText(telefono)
            self.lineEditDireccion_2.setText(direccion)
            self.lineEditNombreMascotaDetalles.setText(nombre_mascota)
            self.lineEditEspeciesDetalles.setText(especie)
            self.lineEditRazaDetalles.setText(raza)
            self.lineEditColorDetalles.setText(color)
            self.lineEditTamanioDetalles.setText(tamano)
            self.lineEditfechaNacimientoDetalles.setText(str(fecha_nacimiento))

            # Deshabilitar edición en los lineEdit
            for campo in [
                self.lineEditNombreDetalles, self.lineEditCedulaDetalles, 
                self.lineEditCorreoDetalles, self.lineEditTelefonoDetalles, 
                self.lineEditDireccion_2, self.lineEditNombreMascotaDetalles, 
                self.lineEditEspeciesDetalles, self.lineEditRazaDetalles, 
                self.lineEditColorDetalles, self.lineEditTamanioDetalles, 
                self.lineEditfechaNacimientoDetalles]:
                campo.setReadOnly(True)

            # Cargar la foto de la mascota si existe
            self.mostrar_foto_mascota(foto if foto else "")

        else:
            QMessageBox.warning(None, "Error", "No se encontraron detalles para la mascota seleccionada.")

        cursor.close()
        conexion.close()
        
    def configurar_label_foto(self):
        """Configura el QLabel para detectar clics y mostrar un mensaje cuando no haya imagen."""
        self.labelFotoMascota.setText("Clic para subir foto")
        self.labelFotoMascota.setAlignment(Qt.AlignCenter)
        self.labelFotoMascota.setStyleSheet("border: 2px dashed gray; color: gray;")  
        self.labelFotoMascota.mousePressEvent = self.subir_foto_mascota  # Detectar clic en QLabel

    def subir_foto_mascota(self, event):
        """Abre un cuadro de diálogo para seleccionar una imagen y la guarda en la base de datos."""
        if not hasattr(self, 'mascota_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna mascota.")
            return

        opciones = QFileDialog.Options()
        ruta_imagen, _ = QFileDialog.getOpenFileName(
            None, "Seleccionar Foto de Mascota", "", 
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*)", 
            options=opciones
        )

        if ruta_imagen:
            self.guardar_foto_mascota(ruta_imagen)

    def guardar_foto_mascota(self, ruta_origen):
        """Guarda la imagen en la carpeta images-mascotas/[NombreMascota] y actualiza la base de datos."""
        conexion = connect_to_database()
        cursor = conexion.cursor()

        # Obtener el nombre de la mascota
        query = "SELECT Nombre FROM Mascotas WHERE ID = %s"
        cursor.execute(query, (self.mascota_seleccionada_id,))
        resultado = cursor.fetchone()

        if resultado:
            nombre_mascota = resultado[0]
            carpeta_destino = os.path.join("images-mascotas", nombre_mascota)

            # Crear la carpeta si no existe
            os.makedirs(carpeta_destino, exist_ok=True)

            # Guardar la imagen con el nombre de la mascota
            extension = os.path.splitext(ruta_origen)[1]
            ruta_destino = os.path.join(carpeta_destino, f"{nombre_mascota}{extension}")

            # Copiar la imagen al destino
            shutil.copy(ruta_origen, ruta_destino)

            # Guardar la ruta en la base de datos
            update_query = "UPDATE Mascotas SET Foto = %s WHERE ID = %s"
            cursor.execute(update_query, (ruta_destino, self.mascota_seleccionada_id))
            conexion.commit()

            # Mostrar la imagen en el QLabel
            self.mostrar_foto_mascota(ruta_destino)

        else:
            QMessageBox.warning(None, "Error", "No se pudo obtener el nombre de la mascota.")

        cursor.close()
        conexion.close()

    def mostrar_foto_mascota(self, ruta_foto):
        """Carga y muestra la imagen en el QLabel. Si no existe, muestra el mensaje predeterminado."""
        if ruta_foto and os.path.exists(ruta_foto):
            pixmap = QPixmap(ruta_foto)
            self.labelFotoMascota.setPixmap(
                pixmap.scaled(self.labelFotoMascota.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
            self.labelFotoMascota.setText("")  # Elimina el texto
        else:
            self.labelFotoMascota.clear()  # Limpia cualquier imagen anterior
            self.labelFotoMascota.setText("Clic para subir foto")
            self.labelFotoMascota.setAlignment(Qt.AlignCenter)
            self.labelFotoMascota.setStyleSheet("border: 2px dashed gray; color: gray;")

    def cargar_foto_mascota_desde_bd(self):
        """Carga la foto desde la base de datos y la muestra en el QLabel."""
        if not hasattr(self, 'mascota_seleccionada_id'):
            return

        conexion = connect_to_database()
        cursor = conexion.cursor()

        query = "SELECT Foto FROM Mascotas WHERE ID = %s"
        cursor.execute(query, (self.mascota_seleccionada_id,))
        resultado = cursor.fetchone()

        ruta_foto = resultado[0] if resultado and resultado[0] else None

        cursor.close()
        conexion.close()

        self.mostrar_foto_mascota(ruta_foto)

    def cargar_citas(self):
        """Carga todas las citas registradas en la base de datos y las muestra en la tabla."""
        try:
            # 1️⃣ Conectar a la base de datos
            conexion = connect_to_database()
            cursor = conexion.cursor()

            # 2️⃣ Consulta SQL para obtener todas las citas
            consulta = """
                SELECT 
                    Citas.ID, 
                    DatosUsuarios.Cedula AS Cedula,
                    DatosUsuarios.Nombre AS Cliente,
                    Mascotas.Nombre AS Mascota, 
                    Mascotas.Especie AS Especie,
                    Mascotas.Raza AS Raza,
                    Servicios.Nombre AS Servicio,
                    Citas.FechaHora, 
                    Citas.Estado
                FROM Citas
                INNER JOIN Mascotas ON Citas.MascotaID = Mascotas.ID
                INNER JOIN Usuarios AS Clientes ON Citas.UsuarioID = Clientes.ID
                INNER JOIN DatosUsuarios ON Clientes.ID = DatosUsuarios.UsuarioID
                INNER JOIN Servicios ON Citas.ServicioID = Servicios.ID
                ORDER BY Citas.FechaHora DESC
            """
            cursor.execute(consulta)
            resultados = cursor.fetchall()

            # 3️⃣ Verificar si hay resultados
            if not resultados:
                self.tableWidgetListaCitas.setRowCount(0)
                return  # Si no hay citas, salir del método

            # 4️⃣ Configurar la tabla
            self.tableWidgetListaCitas.setRowCount(len(resultados))
            self.tableWidgetListaCitas.setColumnCount(len(resultados[0]))
            self.tableWidgetListaCitas.setHorizontalHeaderLabels(
                ["ID", "Cédula", "Cliente", "Mascota", "Especie", "Raza", "Servicio", "Fecha", "Estado"]
            )

            # 5️⃣ Llenar la tabla con los resultados
            for fila, datos in enumerate(resultados):
                for columna, valor in enumerate(datos):
                    item = QTableWidgetItem(str(valor) if valor is not None else "")
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 🔒 No editable pero seleccionable
                    self.tableWidgetListaCitas.setItem(fila, columna, item)

            # 6️⃣ Ajustar el tamaño de las columnas para que se expandan proporcionalmente
            header = self.tableWidgetListaCitas.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)  # Ocupa todo el ancho

            # 7️⃣ Ajustar el alto de las filas automáticamente
            self.tableWidgetListaCitas.resizeRowsToContents()

            # 8️⃣ 🔒 Solo permitir selección de una fila a la vez
            self.tableWidgetListaCitas.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableWidgetListaCitas.setSelectionMode(QAbstractItemView.SingleSelection)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudieron cargar las citas: {err}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    def seleccionar_cita(self):
        """Guarda el ID de la cita seleccionada y cambia de página para mostrar los detalles."""
        fila_seleccionada = self.tableWidgetListaCitas.currentRow()

        if fila_seleccionada != -1:  # Verifica que haya una fila seleccionada
            item_id = self.tableWidgetListaCitas.item(fila_seleccionada, 0)  # Columna ID

            if item_id:
                self.cita_seleccionada_id = int(item_id.text())  # Guarda el ID de la cita seleccionada
                self.stackedWidget.setCurrentIndex(5)  # Cambia a la página de detalles
                self.abrir_detalles_cita()  # Llama a la función para cargar los detalles
        else:
            QMessageBox.warning(None, "Selección requerida", "Por favor, seleccione una cita de la lista.")

    def conectar_boton_abrir_cita(self):
        """Conecta el botón de detalles con la función para seleccionar y abrir la cita."""
        self.pushButtonDetallesCita.clicked.connect(self.seleccionar_cita)

    def abrir_detalles_cita(self):
        """Carga los detalles del cliente, mascota y cita seleccionada, deshabilita los campos y muestra la información."""
        
        if not hasattr(self, 'cita_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna cita.")
            return

        conexion = connect_to_database()
        cursor = conexion.cursor()

        # Consultar los datos de la cita, el cliente y la mascota
        query = """
            SELECT d.Nombre, d.Cedula, d.Telefono, d.Direccion,
                   m.Nombre, m.Raza, s.Nombre, c.Estado, c.FechaHora
            FROM Citas c
            JOIN Mascotas m ON c.MascotaID = m.ID
            JOIN DatosUsuarios d ON c.UsuarioID = d.UsuarioID
            JOIN Servicios s ON c.ServicioID = s.ID
            WHERE c.ID = %s
        """
        cursor.execute(query, (self.cita_seleccionada_id,))
        datos = cursor.fetchone()

        if datos:
            (nombre, cedula, telefono, direccion, 
             nombre_mascota, raza, servicio, estado, fecha_hora) = datos

            # Separar fecha y hora
            fecha = fecha_hora.date()
            hora = fecha_hora.time()

            self.lineEditNombreDetallesCita.setText(nombre)
            self.lineEditCedulaDetallesCita.setText(cedula)
            self.lineEditTelefonoDetallesCita.setText(telefono)
            self.lineEditDireccionDetallesCita.setText(direccion)
            self.lineEditNombreMascotaCita.setText(nombre_mascota)
            self.lineEditRazaCita.setText(raza)
            self.lineEditServicioDetallesCita.setText(servicio)
            self.lineEditEstadoCita.setText(estado)
            self.lineEditFechaCita.setText(str(fecha))
            self.lineEditHoraCita.setText(str(hora))

            # Deshabilitar edición en los lineEdit
            for campo in [
                self.lineEditNombreDetallesCita, self.lineEditCedulaDetallesCita, 
                self.lineEditTelefonoDetallesCita, self.lineEditDireccionDetallesCita,
                self.lineEditNombreMascotaCita, self.lineEditRazaCita, 
                self.lineEditServicioDetallesCita, self.lineEditEstadoCita, 
                self.lineEditFechaCita, self.lineEditHoraCita]:
                campo.setReadOnly(True)

        else:
            QMessageBox.warning(None, "Error", "No se encontraron detalles para la cita seleccionada.")

        cursor.close()
        conexion.close()

    def asignar_cita_a_mi(self):
        """Asigna la cita actualmente seleccionada al veterinario logueado (self.client_id)."""

        if not hasattr(self, 'cita_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna cita.")
            return

        try:
            # Conectar a la base de datos
            conexion = connect_to_database()
            cursor = conexion.cursor()

            # Actualizar la cita con el ID del veterinario logueado
            consulta = """
                UPDATE Citas
                SET VeterinarioID = %s, Estado = 'Confirmada'
                WHERE ID = %s
            """
            cursor.execute(consulta, (self.client_id, self.cita_seleccionada_id))
            conexion.commit()

            QMessageBox.information(None, "Cita Asignada", "Te has asignado esta cita exitosamente.")

            # Recargar los detalles de la cita para reflejar el cambio
            self.abrir_detalles_cita()

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudo asignar la cita: {err}")

        finally:
            cursor.close()
            conexion.close()
            

    def cargar_citas_veterinario(self):
        """Carga solo las citas asignadas al veterinario actual y las muestra en la tabla."""
        try:
            # 1️⃣ Conectar a la base de datos
            conexion = connect_to_database()
            cursor = conexion.cursor()

            # Obtener el ID del veterinario actual (asegúrate de que `self.client_id` tenga el ID del veterinario logueado)
            veterinario_id = self.client_id  # El client_id debe contener el ID del veterinario actual

            # 2️⃣ Consulta SQL para obtener solo las citas asignadas al veterinario actual
            consulta = """
                SELECT 
                    Citas.ID, 
                    DatosUsuarios.Cedula AS Cedula,
                    DatosUsuarios.Nombre AS Cliente,
                    Mascotas.Nombre AS Mascota, 
                    Mascotas.Especie AS Especie,
                    Mascotas.Raza AS Raza,
                    Servicios.Nombre AS Servicio,
                    Citas.FechaHora, 
                    Citas.Estado
                FROM Citas
                INNER JOIN Mascotas ON Citas.MascotaID = Mascotas.ID
                INNER JOIN Usuarios AS Clientes ON Citas.UsuarioID = Clientes.ID
                INNER JOIN DatosUsuarios ON Clientes.ID = DatosUsuarios.UsuarioID
                INNER JOIN Servicios ON Citas.ServicioID = Servicios.ID
                WHERE Citas.VeterinarioID = %s  -- Filtramos las citas por el ID del veterinario actual
                ORDER BY Citas.FechaHora DESC
            """
            cursor.execute(consulta, (veterinario_id,))  # Pasamos el `veterinario_id` como parámetro a la consulta

            resultados = cursor.fetchall()

            # 3️⃣ Verificar si hay resultados
            if not resultados:
                self.tableWidgetListaCitas.setRowCount(0)
                return  # Si no hay citas, salir del método

            # 4️⃣ Configurar la tabla
            self.tableWidgetListaCitas.setRowCount(len(resultados))
            self.tableWidgetListaCitas.setColumnCount(len(resultados[0]))
            self.tableWidgetListaCitas.setHorizontalHeaderLabels(
                ["ID", "Cédula", "Cliente", "Mascota", "Especie", "Raza", "Servicio", "Fecha", "Estado"]
            )

            # 5️⃣ Llenar la tabla con los resultados
            for fila, datos in enumerate(resultados):
                for columna, valor in enumerate(datos):
                    item = QTableWidgetItem(str(valor) if valor is not None else "")
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 🔒 No editable pero seleccionable
                    self.tableWidgetListaCitas.setItem(fila, columna, item)

            # 6️⃣ Ajustar el tamaño de las columnas para que se expandan proporcionalmente
            header = self.tableWidgetListaCitas.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)  # Ocupa todo el ancho

            # 7️⃣ Ajustar el alto de las filas automáticamente
            self.tableWidgetListaCitas.resizeRowsToContents()

            # 8️⃣ 🔒 Solo permitir selección de una fila a la vez
            self.tableWidgetListaCitas.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableWidgetListaCitas.setSelectionMode(QAbstractItemView.SingleSelection)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudieron cargar las citas: {err}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    def seleccionar_cita_asignada(self):
        """Guarda el ID de la cita seleccionada y cambia de página para mostrar los detalles."""
        
        fila_seleccionada = self.tableWidgetListaCitas.currentRow()

        if fila_seleccionada != -1:  # Verifica que haya una fila seleccionada
            item_id = self.tableWidgetListaCitas.item(fila_seleccionada, 0)  # Columna ID

            if item_id:
                self.cita_seleccionada_id = int(item_id.text())  # Guarda el ID de la cita seleccionada
                
                # Verificar si la cita está asignada al veterinario y si es para el día de hoy
                conexion = connect_to_database()
                cursor = conexion.cursor()

                # Consultar la cita seleccionada para verificar el veterinario y la fecha
                query = """
                    SELECT c.VeterinarioID, c.FechaHora
                    FROM Citas c
                    WHERE c.ID = %s
                """
                cursor.execute(query, (self.cita_seleccionada_id,))
                cita = cursor.fetchone()

                if cita:
                    veterinario_id, fecha_hora = cita
                    fecha_actual = QDate.currentDate()  # Fecha actual
                    hora_actual = QTime.currentTime()  # Hora actual

                    # Verificar si la cita está asignada al veterinario actual
                    if veterinario_id != self.client_id:
                        QMessageBox.warning(None, "Error", "No tienes asignada esta cita.")
                        self.cargar_citas()
                        return

                    # Verificar si la cita es para el día de hoy y la hora correcta
                    fecha_cita = fecha_hora.date()
                    hora_cita = fecha_hora.time()

                    if fecha_cita != fecha_actual:
                        QMessageBox.warning(None, "Error", f"La cita es para el {fecha_cita.toString()} a las {hora_cita.toString()}.")
                        return

                    if hora_cita > hora_actual:
                        QMessageBox.warning(None, "Error", "La cita no es para hoy o está en el futuro.")
                        self.cargar_citas()
                        return

                    # Si todo está correcto, cambiar a la página de detalles
                    self.stackedWidget.setCurrentIndex(6)  # Cambia a la página de detalles
                    self.abrir_detalles_cita_asignada()  # Llama a la función para cargar los detalles
                    self.cargar_citas()
                else:
                    QMessageBox.warning(None, "Error", "No se encontró información de la cita.")

                cursor.close()
                conexion.close()
        else:
            QMessageBox.warning(None, "Selección requerida", "Por favor, seleccione una cita de la lista.")



    def conectar_boton_abrir_cita_asignada(self):
        """Conecta el botón de detalles con la función para seleccionar y abrir la cita."""
        
        self.pushButtonAtender.clicked.connect(self.seleccionar_cita_asignada)


    def abrir_detalles_cita_asignada(self):
        """Carga los detalles del cliente, mascota y cita seleccionada, deshabilita los campos y muestra la información."""
        
        if not hasattr(self, 'cita_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna cita.")
            return

        conexion = connect_to_database()
        cursor = conexion.cursor()

        # Consultar los datos de la cita, el cliente y la mascota
        query = """
            SELECT d.Nombre, d.Cedula, d.Telefono, d.Direccion,
                   m.Nombre, m.Raza, s.Nombre, c.Estado, c.FechaHora, c.Notas
            FROM Citas c
            JOIN Mascotas m ON c.MascotaID = m.ID
            JOIN DatosUsuarios d ON c.UsuarioID = d.UsuarioID
            JOIN Servicios s ON c.ServicioID = s.ID
            WHERE c.ID = %s
        """
        cursor.execute(query, (self.cita_seleccionada_id,))
        datos = cursor.fetchone()

        if datos:
            (nombre, cedula, telefono, direccion, 
             nombre_mascota, raza, servicio, estado, fecha_hora, notas) = datos

            # Separar fecha y hora
            fecha = fecha_hora.date()
            hora = fecha_hora.time()

            # Llenar los campos con los datos obtenidos
            self.lineEditUsuarioProductos.setText(nombre)
            self.lineEditNombreMascotaCita_2.setText(nombre_mascota)
            self.lineEditEspecie.setText(raza)
            self.lineEditServicio.setText(servicio)
            self.textEditAnotaciones.setText(notas)
            self.lineEditEstadoCita.setText(estado)
            self.lineEditFechaCita.setText(str(fecha))
            self.lineEditHoraCita.setText(str(hora))

            # Deshabilitar edición en los lineEdit y textEdit
            for campo in [
                self.lineEditUsuarioProductos, self.lineEditNombreMascotaCita_2, 
                self.lineEditEspecie, self.lineEditServicio, self.textEditAnotaciones, 
                self.lineEditEstadoCita, self.lineEditFechaCita, self.lineEditHoraCita]:
                campo.setReadOnly(True)

        else:
            QMessageBox.warning(None, "Error", "No se encontraron detalles para la cita seleccionada.")

        cursor.close()
        conexion.close()

    def conectar_boton_guardar(self):
        """Conecta el botón de guardar con la función para actualizar las anotaciones y el estado de la cita."""
        self.pushButtonGuardar.clicked.connect(self.guardar_atencion_cita)

    def guardar_atencion_cita(self):
        """Guarda las anotaciones y cambia el estado de la cita a 'Atendida'."""
        
        if not hasattr(self, 'cita_seleccionada_id'):
            QMessageBox.warning(None, "Error", "No se ha seleccionado ninguna cita.")
            return

        # Obtener las anotaciones del textEdit
        anotaciones = self.textEditAnotaciones.toPlainText()

        # Conectar a la base de datos
        conexion = connect_to_database()
        cursor = conexion.cursor()

        try:
            # Actualizar el estado de la cita a 'Atendida' y guardar las anotaciones
            query = """
                UPDATE Citas
                SET Estado = 'Atendida', Notas = %s
                WHERE ID = %s
            """
            cursor.execute(query, (anotaciones, self.cita_seleccionada_id))

            # Confirmar cambios
            conexion.commit()

            # Mostrar mensaje de éxito
            QMessageBox.information(None, "Éxito", "La cita ha sido marcada como atendida y las anotaciones se han guardado.")

            # Cambiar la página a la lista de citas (o cualquier otra que desees)
            self.stackedWidget.setCurrentIndex(5)  # Regresar a la página anterior (ajusta el índice si es necesario)
        
        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"No se pudo actualizar la cita: {err}")
        
        finally:
            cursor.close()
            conexion.close()

    def cerrar_ventana(self):
        widget = QtWidgets.QApplication.activeWindow()  # Obtiene la ventana activa
        if widget:
          widget.close()  # Cierra la ventana actual
