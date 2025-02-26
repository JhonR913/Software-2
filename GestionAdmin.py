
from PyQt5 import QtCore, QtGui, QtWidgets
import data_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1257, 822)
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
        self.label_2.setGeometry(QtCore.QRect(320, 30, 591, 51))
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
        self.pushButtonRegistrarUsuarios = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonRegistrarUsuarios.setGeometry(QtCore.QRect(20, 130, 101, 81))
        self.pushButtonRegistrarUsuarios.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/agregar-usuario.png); /* Imagen en el botón */\n"
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
        self.pushButtonRegistrarUsuarios.setText("")
        self.pushButtonRegistrarUsuarios.setObjectName("pushButtonRegistrarUsuarios")
        self.label_7 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 81, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButtonTarifas = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonTarifas.setGeometry(QtCore.QRect(20, 250, 101, 81))
        self.pushButtonTarifas.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image:url(:/images/images/moneda.png); /* Imagen en el botón */\n"
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
        self.pushButtonTarifas.setText("")
        self.pushButtonTarifas.setObjectName("pushButtonTarifas")
        self.label_8 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_8.setGeometry(QtCore.QRect(30, 450, 81, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButtonContaduria = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonContaduria.setGeometry(QtCore.QRect(20, 370, 101, 81))
        self.pushButtonContaduria.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image:url(:/images/images/contabilidad.png); /* Imagen en el botón */\n"
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
        self.pushButtonContaduria.setText("")
        self.pushButtonContaduria.setObjectName("pushButtonContaduria")
        self.label_9 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_9.setGeometry(QtCore.QRect(30, 570, 81, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButtonUsuarios = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonUsuarios.setGeometry(QtCore.QRect(20, 490, 101, 81))
        self.pushButtonUsuarios.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/cliente.png); /* Imagen en el botón */\n"
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
        self.pushButtonUsuarios.setText("")
        self.pushButtonUsuarios.setObjectName("pushButtonUsuarios")
        self.pushButtonRegistros = QtWidgets.QPushButton(self.widgetBarraVertical)
        self.pushButtonRegistros.setGeometry(QtCore.QRect(20, 610, 101, 81))
        self.pushButtonRegistros.setStyleSheet("QPushButton {\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"    image: url(:/images/images/historial-de-pedidos.png); /* Imagen en el botón */\n"
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
        self.pushButtonRegistros.setText("")
        self.pushButtonRegistros.setObjectName("pushButtonRegistros")
        self.label_10 = QtWidgets.QLabel(self.widgetBarraVertical)
        self.label_10.setGeometry(QtCore.QRect(30, 690, 81, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 100, 1171, 741))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageGeneral = QtWidgets.QWidget()
        self.pageGeneral.setObjectName("pageGeneral")
        self.widgetDinero = QtWidgets.QWidget(self.pageGeneral)
        self.widgetDinero.setGeometry(QtCore.QRect(90, 110, 321, 91))
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
        self.label_4 = QtWidgets.QLabel(self.widgetDinero)
        self.label_4.setGeometry(QtCore.QRect(190, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:/images/images/dinero.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEditMesDineroEnCaja = QtWidgets.QLineEdit(self.widgetDinero)
        self.lineEditMesDineroEnCaja.setGeometry(QtCore.QRect(180, 10, 121, 31))
        self.lineEditMesDineroEnCaja.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"border: 2px solid #a8daff; /* Borde gris */")
        self.lineEditMesDineroEnCaja.setObjectName("lineEditMesDineroEnCaja")
        self.widgetCarrosEnParqueadero = QtWidgets.QWidget(self.pageGeneral)
        self.widgetCarrosEnParqueadero.setGeometry(QtCore.QRect(100, 310, 281, 191))
        self.widgetCarrosEnParqueadero.setStyleSheet("QWidget#widgetCarrosEnParqueadero {\n"
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
        self.widgetCarrosEnParqueadero.setObjectName("widgetCarrosEnParqueadero")
        self.label_13 = QtWidgets.QLabel(self.widgetCarrosEnParqueadero)
        self.label_13.setGeometry(QtCore.QRect(50, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("background-color: #e7e4e4; /* Azul claro */")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widgetCarrosEnParqueadero)
        self.label_14.setGeometry(QtCore.QRect(60, 50, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("background-color: #e7e4e4; /* Azul claro */\n"
"image: url(:/images/images/completada.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.lcdNumberCitasCompletadas = QtWidgets.QLCDNumber(self.widgetCarrosEnParqueadero)
        self.lcdNumberCitasCompletadas.setGeometry(QtCore.QRect(100, 150, 64, 23))
        self.lcdNumberCitasCompletadas.setObjectName("lcdNumberCitasCompletadas")
        self.widgetMotosEnParqueadero = QtWidgets.QWidget(self.pageGeneral)
        self.widgetMotosEnParqueadero.setGeometry(QtCore.QRect(450, 310, 281, 191))
        self.widgetMotosEnParqueadero.setStyleSheet("QWidget#widgetMotosEnParqueadero {\n"
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
        self.widgetMotosEnParqueadero.setObjectName("widgetMotosEnParqueadero")
        self.label_15 = QtWidgets.QLabel(self.widgetMotosEnParqueadero)
        self.label_15.setGeometry(QtCore.QRect(50, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet("background-color: #e7e4e4; /* Azul claro */")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widgetMotosEnParqueadero)
        self.label_16.setGeometry(QtCore.QRect(60, 50, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet("background-color: #e7e4e4; /* Azul claro */\n"
"image: url(:/images/images/reloj.png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.lcdNumberCitasAgendadas = QtWidgets.QLCDNumber(self.widgetMotosEnParqueadero)
        self.lcdNumberCitasAgendadas.setGeometry(QtCore.QRect(110, 150, 64, 23))
        self.lcdNumberCitasAgendadas.setObjectName("lcdNumberCitasAgendadas")
        self.widgetParqueaderosDisponibles = QtWidgets.QWidget(self.pageGeneral)
        self.widgetParqueaderosDisponibles.setGeometry(QtCore.QRect(780, 110, 281, 451))
        self.widgetParqueaderosDisponibles.setStyleSheet("QWidget#widgetParqueaderosDisponibles {\n"
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
        self.widgetParqueaderosDisponibles.setObjectName("widgetParqueaderosDisponibles")
        self.label_17 = QtWidgets.QLabel(self.widgetParqueaderosDisponibles)
        self.label_17.setGeometry(QtCore.QRect(70, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widgetParqueaderosDisponibles)
        self.label_18.setGeometry(QtCore.QRect(60, 70, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:/images/images/perro.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.lcdNumberPerros = QtWidgets.QLCDNumber(self.widgetParqueaderosDisponibles)
        self.lcdNumberPerros.setGeometry(QtCore.QRect(110, 180, 64, 23))
        self.lcdNumberPerros.setObjectName("lcdNumberPerros")
        self.lcdNumberGatos = QtWidgets.QLCDNumber(self.widgetParqueaderosDisponibles)
        self.lcdNumberGatos.setGeometry(QtCore.QRect(110, 390, 64, 23))
        self.lcdNumberGatos.setObjectName("lcdNumberGatos")
        self.label_19 = QtWidgets.QLabel(self.widgetParqueaderosDisponibles)
        self.label_19.setGeometry(QtCore.QRect(60, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:/images/images/gato.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.widgetParqueaderosDisponibles)
        self.label_22.setGeometry(QtCore.QRect(120, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widgetParqueaderosDisponibles)
        self.label_23.setGeometry(QtCore.QRect(120, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_23.setObjectName("label_23")
        self.widgetMoneda = QtWidgets.QWidget(self.pageGeneral)
        self.widgetMoneda.setGeometry(QtCore.QRect(450, 110, 261, 91))
        self.widgetMoneda.setStyleSheet("QWidget#widgetMoneda {\n"
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
        self.widgetMoneda.setObjectName("widgetMoneda")
        self.label_20 = QtWidgets.QLabel(self.widgetMoneda)
        self.label_20.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setStyleSheet("background-color: #a8daff; /* Azul claro */")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widgetMoneda)
        self.label_21.setGeometry(QtCore.QRect(140, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setStyleSheet("background-color: #a8daff; /* Azul claro */\n"
"image: url(:images/images/pesos.png);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.labelFecha = QtWidgets.QLabel(self.pageGeneral)
        self.labelFecha.setGeometry(QtCore.QRect(260, 240, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFecha.setFont(font)
        self.labelFecha.setObjectName("labelFecha")
        self.stackedWidget.addWidget(self.pageGeneral)
        self.pageAgregarUsuarios = QtWidgets.QWidget()
        self.pageAgregarUsuarios.setObjectName("pageAgregarUsuarios")
        self.label_11 = QtWidgets.QLabel(self.pageAgregarUsuarios)
        self.label_11.setGeometry(QtCore.QRect(380, 50, 221, 41))
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
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.comboBoxRol = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxRol.setFont(font)
        self.comboBoxRol.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxRol.setObjectName("comboBoxRol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxRol)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEditNombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombre.setFont(font)
        self.lineEditNombre.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditNombre)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEditCedula = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedula.setFont(font)
        self.lineEditCedula.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedula.setObjectName("lineEditCedula")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditCedula)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEditCorreo = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCorreo.setFont(font)
        self.lineEditCorreo.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCorreo.setObjectName("lineEditCorreo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditCorreo)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEditTelefono_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTelefono_2.setFont(font)
        self.lineEditTelefono_2.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTelefono_2.setObjectName("lineEditTelefono_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditTelefono_2)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEditDireccion = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDireccion.setFont(font)
        self.lineEditDireccion.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditDireccion.setObjectName("lineEditDireccion")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditDireccion)
        self.pushButtonRegresarRegistrar = QtWidgets.QPushButton(self.pageAgregarUsuarios)
        self.pushButtonRegresarRegistrar.setGeometry(QtCore.QRect(240, 560, 191, 51))
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
        self.pushButtonAgregarMascota = QtWidgets.QPushButton(self.pageAgregarUsuarios)
        self.pushButtonAgregarMascota.setGeometry(QtCore.QRect(700, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonAgregarMascota.setFont(font)
        self.pushButtonAgregarMascota.setStyleSheet("QPushButton {\n"
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
        self.pushButtonAgregarMascota.setObjectName("pushButtonAgregarMascota")
        self.pushButtonCrear = QtWidgets.QPushButton(self.pageAgregarUsuarios)
        self.pushButtonCrear.setGeometry(QtCore.QRect(470, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonCrear.setFont(font)
        self.pushButtonCrear.setStyleSheet("QPushButton {\n"
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
        self.pushButtonCrear.setObjectName("pushButtonCrear")
        self.stackedWidget.addWidget(self.pageAgregarUsuarios)
        self.pageAgregarMascota = QtWidgets.QWidget()
        self.pageAgregarMascota.setObjectName("pageAgregarMascota")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.pageAgregarMascota)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(130, 90, 811, 441))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_96 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_96.setFont(font)
        self.label_96.setObjectName("label_96")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_96)
        self.lineEditNombre_2 = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombre_2.setFont(font)
        self.lineEditNombre_2.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombre_2.setObjectName("lineEditNombre_2")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombre_2)
        self.label_98 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_98.setFont(font)
        self.label_98.setObjectName("label_98")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_98)
        self.label_99 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_99)
        self.label_100 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_100)
        self.comboBoxEspecie = QtWidgets.QComboBox(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxEspecie.setFont(font)
        self.comboBoxEspecie.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxEspecie.setObjectName("comboBoxEspecie")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxEspecie)
        self.lineEditRaza = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRaza.setFont(font)
        self.lineEditRaza.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRaza.setObjectName("lineEditRaza")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRaza)
        self.lineEditColor = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditColor.setFont(font)
        self.lineEditColor.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditColor.setObjectName("lineEditColor")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditColor)
        self.label_102 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_102.setFont(font)
        self.label_102.setObjectName("label_102")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_102)
        self.comboBoxTamanio = QtWidgets.QComboBox(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxTamanio.setFont(font)
        self.comboBoxTamanio.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxTamanio.setObjectName("comboBoxTamanio")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxTamanio)
        self.label_103 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_103)
        self.calendarWidgetFechaDeNacimiento = QtWidgets.QCalendarWidget(self.formLayoutWidget_8)
        self.calendarWidgetFechaDeNacimiento.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.calendarWidgetFechaDeNacimiento.setObjectName("calendarWidgetFechaDeNacimiento")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.calendarWidgetFechaDeNacimiento)
        self.pushButtonRegistrarMascota = QtWidgets.QPushButton(self.pageAgregarMascota)
        self.pushButtonRegistrarMascota.setGeometry(QtCore.QRect(550, 570, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegistrarMascota.setFont(font)
        self.pushButtonRegistrarMascota.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegistrarMascota.setObjectName("pushButtonRegistrarMascota")
        self.pushButtonRegresarMascota = QtWidgets.QPushButton(self.pageAgregarMascota)
        self.pushButtonRegresarMascota.setGeometry(QtCore.QRect(340, 570, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarMascota.setFont(font)
        self.pushButtonRegresarMascota.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarMascota.setObjectName("pushButtonRegresarMascota")
        self.label_29 = QtWidgets.QLabel(self.pageAgregarMascota)
        self.label_29.setGeometry(QtCore.QRect(410, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.stackedWidget.addWidget(self.pageAgregarMascota)
        self.pageListaUsuariosMascotas = QtWidgets.QWidget()
        self.pageListaUsuariosMascotas.setObjectName("pageListaUsuariosMascotas")
        self.label_36 = QtWidgets.QLabel(self.pageListaUsuariosMascotas)
        self.label_36.setGeometry(QtCore.QRect(320, 10, 371, 31))
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
        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.lineEditCedulaLista = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaLista.setFont(font)
        self.lineEditCedulaLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaLista.setObjectName("lineEditCedulaLista")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaLista)
        self.label_45 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.lineEditNombreLista = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreLista.setFont(font)
        self.lineEditNombreLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreLista.setObjectName("lineEditNombreLista")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreLista)
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.comboBoxTipoEspecieLista = QtWidgets.QComboBox(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxTipoEspecieLista.setFont(font)
        self.comboBoxTipoEspecieLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxTipoEspecieLista.setObjectName("comboBoxTipoEspecieLista")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxTipoEspecieLista)
        self.label_44 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.lineEditRazaLista = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaLista.setFont(font)
        self.lineEditRazaLista.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaLista.setObjectName("lineEditRazaLista")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaLista)
        self.tableWidgetListaUsuariosMascotas = QtWidgets.QTableWidget(self.pageListaUsuariosMascotas)
        self.tableWidgetListaUsuariosMascotas.setGeometry(QtCore.QRect(145, 260, 861, 331))
        self.tableWidgetListaUsuariosMascotas.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetListaUsuariosMascotas.setObjectName("tableWidgetListaUsuariosMascotas")
        self.tableWidgetListaUsuariosMascotas.setColumnCount(0)
        self.tableWidgetListaUsuariosMascotas.setRowCount(0)
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
        self.label_37.setGeometry(QtCore.QRect(360, -10, 281, 61))
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
        self.label_53 = QtWidgets.QLabel(self.pageTarifas)
        self.label_53.setGeometry(QtCore.QRect(360, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.pageTarifas)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(120, 120, 821, 204))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_54 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.comboBoxTipoServicio = QtWidgets.QComboBox(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxTipoServicio.setFont(font)
        self.comboBoxTipoServicio.setStyleSheet("\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"")
        self.comboBoxTipoServicio.setObjectName("comboBoxTipoServicio")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxTipoServicio)
        self.label_57 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.label_56 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.doubleSpinBoxTarifa = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxTarifa.setFont(font)
        self.doubleSpinBoxTarifa.setStyleSheet("\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"")
        self.doubleSpinBoxTarifa.setObjectName("doubleSpinBoxTarifa")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxTarifa)
        self.pushButtonTarifaHorario = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonTarifaHorario.setFont(font)
        self.pushButtonTarifaHorario.setStyleSheet("QPushButton {\n"
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
        self.pushButtonTarifaHorario.setObjectName("pushButtonTarifaHorario")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButtonTarifaHorario)
        self.comboBoxHorarioTarifa = QtWidgets.QComboBox(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxHorarioTarifa.setFont(font)
        self.comboBoxHorarioTarifa.setStyleSheet("\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"")
        self.comboBoxHorarioTarifa.setObjectName("comboBoxHorarioTarifa")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxHorarioTarifa)
        self.tableWidgetTarifas = QtWidgets.QTableWidget(self.pageTarifas)
        self.tableWidgetTarifas.setGeometry(QtCore.QRect(120, 340, 821, 241))
        self.tableWidgetTarifas.setStyleSheet("\n"
"    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */\n"
"")
        self.tableWidgetTarifas.setObjectName("tableWidgetTarifas")
        self.tableWidgetTarifas.setColumnCount(0)
        self.tableWidgetTarifas.setRowCount(0)
        self.pushButtonRegresarTarifa = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonRegresarTarifa.setGeometry(QtCore.QRect(300, 630, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresarTarifa.setFont(font)
        self.pushButtonRegresarTarifa.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarTarifa.setObjectName("pushButtonRegresarTarifa")
        self.pushButtonEliminarTarifa = QtWidgets.QPushButton(self.pageTarifas)
        self.pushButtonEliminarTarifa.setGeometry(QtCore.QRect(520, 630, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonEliminarTarifa.setFont(font)
        self.pushButtonEliminarTarifa.setStyleSheet("QPushButton {\n"
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
        self.pushButtonEliminarTarifa.setObjectName("pushButtonEliminarTarifa")
        self.stackedWidget.addWidget(self.pageTarifas)
        self.pageContaduria = QtWidgets.QWidget()
        self.pageContaduria.setObjectName("pageContaduria")
        self.label_70 = QtWidgets.QLabel(self.pageContaduria)
        self.label_70.setGeometry(QtCore.QRect(420, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.pageContaduria)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 1011, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(23)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_71 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_2.addWidget(self.label_71)
        self.dateEditDesdeContaduria = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEditDesdeContaduria.setFont(font)
        self.dateEditDesdeContaduria.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.dateEditDesdeContaduria.setObjectName("dateEditDesdeContaduria")
        self.horizontalLayout_2.addWidget(self.dateEditDesdeContaduria)
        self.label_72 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_2.addWidget(self.label_72)
        self.dateEditHastaContaduria = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEditHastaContaduria.setFont(font)
        self.dateEditHastaContaduria.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.dateEditHastaContaduria.setObjectName("dateEditHastaContaduria")
        self.horizontalLayout_2.addWidget(self.dateEditHastaContaduria)
        self.label_73 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_2.addWidget(self.label_73)
        self.comboBoxPeriodoContaduria = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxPeriodoContaduria.setFont(font)
        self.comboBoxPeriodoContaduria.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxPeriodoContaduria.setObjectName("comboBoxPeriodoContaduria")
        self.horizontalLayout_2.addWidget(self.comboBoxPeriodoContaduria)
        self.label_74 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_2.addWidget(self.label_74)
        self.comboBoxEstadoContaduria = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxEstadoContaduria.setFont(font)
        self.comboBoxEstadoContaduria.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.comboBoxEstadoContaduria.setObjectName("comboBoxEstadoContaduria")
        self.horizontalLayout_2.addWidget(self.comboBoxEstadoContaduria)
        self.tableWidgetContaduria = QtWidgets.QTableWidget(self.pageContaduria)
        self.tableWidgetContaduria.setGeometry(QtCore.QRect(60, 160, 1011, 361))
        self.tableWidgetContaduria.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetContaduria.setObjectName("tableWidgetContaduria")
        self.tableWidgetContaduria.setColumnCount(0)
        self.tableWidgetContaduria.setRowCount(0)
        self.pushButtonRegresarContaduria = QtWidgets.QPushButton(self.pageContaduria)
        self.pushButtonRegresarContaduria.setGeometry(QtCore.QRect(210, 580, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarContaduria.setFont(font)
        self.pushButtonRegresarContaduria.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarContaduria.setObjectName("pushButtonRegresarContaduria")
        self.pushButtonDetallesContaduria = QtWidgets.QPushButton(self.pageContaduria)
        self.pushButtonDetallesContaduria.setGeometry(QtCore.QRect(440, 580, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDetallesContaduria.setFont(font)
        self.pushButtonDetallesContaduria.setStyleSheet("QPushButton {\n"
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
        self.pushButtonDetallesContaduria.setObjectName("pushButtonDetallesContaduria")
        self.pushButtonExportarContaduria = QtWidgets.QPushButton(self.pageContaduria)
        self.pushButtonExportarContaduria.setGeometry(QtCore.QRect(670, 580, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonExportarContaduria.setFont(font)
        self.pushButtonExportarContaduria.setStyleSheet("QPushButton {\n"
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
        self.pushButtonExportarContaduria.setObjectName("pushButtonExportarContaduria")
        self.stackedWidget.addWidget(self.pageContaduria)
        self.pageDetallesContaduria = QtWidgets.QWidget()
        self.pageDetallesContaduria.setObjectName("pageDetallesContaduria")
        self.label_75 = QtWidgets.QLabel(self.pageDetallesContaduria)
        self.label_75.setGeometry(QtCore.QRect(380, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.pageDetallesContaduria)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(30, 50, 601, 501))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_10 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_80 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_80)
        self.lineEditNombreDetallesFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreDetallesFactura.setFont(font)
        self.lineEditNombreDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreDetallesFactura.setObjectName("lineEditNombreDetallesFactura")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreDetallesFactura)
        self.label_81 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_81)
        self.lineEditCedulaDetallesFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaDetallesFactura.setFont(font)
        self.lineEditCedulaDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaDetallesFactura.setObjectName("lineEditCedulaDetallesFactura")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaDetallesFactura)
        self.label_82 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_82)
        self.lineEditTelefonoDetallesFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTelefonoDetallesFactura.setFont(font)
        self.lineEditTelefonoDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTelefonoDetallesFactura.setObjectName("lineEditTelefonoDetallesFactura")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditTelefonoDetallesFactura)
        self.label_83 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_83)
        self.lineEditDireccionDetallesFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDireccionDetallesFactura.setFont(font)
        self.lineEditDireccionDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditDireccionDetallesFactura.setObjectName("lineEditDireccionDetallesFactura")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditDireccionDetallesFactura)
        self.label_85 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.lineEditNombreMascotaFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreMascotaFactura.setFont(font)
        self.lineEditNombreMascotaFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreMascotaFactura.setObjectName("lineEditNombreMascotaFactura")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreMascotaFactura)
        self.lineEditRazaFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditRazaFactura.setFont(font)
        self.lineEditRazaFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditRazaFactura.setObjectName("lineEditRazaFactura")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditRazaFactura)
        self.label_76 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_76)
        self.label_77 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_77)
        self.label_78 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_78)
        self.lineEditServicioDetallesFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServicioDetallesFactura.setFont(font)
        self.lineEditServicioDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditServicioDetallesFactura.setObjectName("lineEditServicioDetallesFactura")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditServicioDetallesFactura)
        self.lineEditTipoServicioFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditTipoServicioFactura.setFont(font)
        self.lineEditTipoServicioFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditTipoServicioFactura.setObjectName("lineEditTipoServicioFactura")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditTipoServicioFactura)
        self.label_79 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_79)
        self.lineEditEstadoFactura = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditEstadoFactura.setFont(font)
        self.lineEditEstadoFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditEstadoFactura.setObjectName("lineEditEstadoFactura")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEditEstadoFactura)
        self.label_84 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_84)
        self.dateEditFechaDetallesFactura = QtWidgets.QDateEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEditFechaDetallesFactura.setFont(font)
        self.dateEditFechaDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.dateEditFechaDetallesFactura.setObjectName("dateEditFechaDetallesFactura")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dateEditFechaDetallesFactura)
        self.label_86 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.formLayout_10.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_86)
        self.label_87 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.formLayout_10.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_87)
        self.lineEditValorPagadoDetalles = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditValorPagadoDetalles.setFont(font)
        self.lineEditValorPagadoDetalles.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditValorPagadoDetalles.setObjectName("lineEditValorPagadoDetalles")
        self.formLayout_10.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEditValorPagadoDetalles)
        self.timeEditHoraDetallesFactura = QtWidgets.QTimeEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEditHoraDetallesFactura.setFont(font)
        self.timeEditHoraDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.timeEditHoraDetallesFactura.setObjectName("timeEditHoraDetallesFactura")
        self.formLayout_10.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.timeEditHoraDetallesFactura)
        self.labelDetallesFactura = QtWidgets.QLabel(self.pageDetallesContaduria)
        self.labelDetallesFactura.setGeometry(QtCore.QRect(670, 50, 421, 501))
        self.labelDetallesFactura.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.labelDetallesFactura.setFrameShape(QtWidgets.QFrame.Box)
        self.labelDetallesFactura.setText("")
        self.labelDetallesFactura.setObjectName("labelDetallesFactura")
        self.pushButtonImprimirDetalles = QtWidgets.QPushButton(self.pageDetallesContaduria)
        self.pushButtonImprimirDetalles.setGeometry(QtCore.QRect(520, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonImprimirDetalles.setFont(font)
        self.pushButtonImprimirDetalles.setStyleSheet("QPushButton {\n"
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
        self.pushButtonImprimirDetalles.setObjectName("pushButtonImprimirDetalles")
        self.pushButtonRegresarDetallesFactura = QtWidgets.QPushButton(self.pageDetallesContaduria)
        self.pushButtonRegresarDetallesFactura.setGeometry(QtCore.QRect(290, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarDetallesFactura.setFont(font)
        self.pushButtonRegresarDetallesFactura.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarDetallesFactura.setObjectName("pushButtonRegresarDetallesFactura")
        self.stackedWidget.addWidget(self.pageDetallesContaduria)
        self.pageRegistrosPropietarios = QtWidgets.QWidget()
        self.pageRegistrosPropietarios.setObjectName("pageRegistrosPropietarios")
        self.tableWidgetUsuarios = QtWidgets.QTableWidget(self.pageRegistrosPropietarios)
        self.tableWidgetUsuarios.setGeometry(QtCore.QRect(60, 250, 1011, 291))
        self.tableWidgetUsuarios.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetUsuarios.setObjectName("tableWidgetUsuarios")
        self.tableWidgetUsuarios.setColumnCount(0)
        self.tableWidgetUsuarios.setRowCount(0)
        self.pushButtonRegresarUsuarios = QtWidgets.QPushButton(self.pageRegistrosPropietarios)
        self.pushButtonRegresarUsuarios.setGeometry(QtCore.QRect(340, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarUsuarios.setFont(font)
        self.pushButtonRegresarUsuarios.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarUsuarios.setObjectName("pushButtonRegresarUsuarios")
        self.label_55 = QtWidgets.QLabel(self.pageRegistrosPropietarios)
        self.label_55.setGeometry(QtCore.QRect(430, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.pushButtonModificarUsuarios = QtWidgets.QPushButton(self.pageRegistrosPropietarios)
        self.pushButtonModificarUsuarios.setGeometry(QtCore.QRect(570, 600, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonModificarUsuarios.setFont(font)
        self.pushButtonModificarUsuarios.setStyleSheet("QPushButton {\n"
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
        self.pushButtonModificarUsuarios.setObjectName("pushButtonModificarUsuarios")
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.pageRegistrosPropietarios)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(180, 60, 731, 151))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setHorizontalSpacing(7)
        self.formLayout_8.setVerticalSpacing(16)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_48 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.lineEditCedulaUsuarios = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCedulaUsuarios.setFont(font)
        self.lineEditCedulaUsuarios.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditCedulaUsuarios.setObjectName("lineEditCedulaUsuarios")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCedulaUsuarios)
        self.label_49 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.lineEditNombreUsuarios = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditNombreUsuarios.setFont(font)
        self.lineEditNombreUsuarios.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditNombreUsuarios.setObjectName("lineEditNombreUsuarios")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNombreUsuarios)
        self.label_58 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.lineEditUsuarioUsuarios = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditUsuarioUsuarios.setFont(font)
        self.lineEditUsuarioUsuarios.setStyleSheet("    background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.lineEditUsuarioUsuarios.setObjectName("lineEditUsuarioUsuarios")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditUsuarioUsuarios)
        self.stackedWidget.addWidget(self.pageRegistrosPropietarios)
        self.pageDetallesRegistro = QtWidgets.QWidget()
        self.pageDetallesRegistro.setObjectName("pageDetallesRegistro")
        self.pushButtonRegresarRegistro = QtWidgets.QPushButton(self.pageDetallesRegistro)
        self.pushButtonRegresarRegistro.setGeometry(QtCore.QRect(420, 580, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRegresarRegistro.setFont(font)
        self.pushButtonRegresarRegistro.setStyleSheet("QPushButton {\n"
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
        self.pushButtonRegresarRegistro.setObjectName("pushButtonRegresarRegistro")
        self.tableWidgetDetallesRegistro = QtWidgets.QTableWidget(self.pageDetallesRegistro)
        self.tableWidgetDetallesRegistro.setGeometry(QtCore.QRect(80, 90, 961, 451))
        self.tableWidgetDetallesRegistro.setStyleSheet("   background-color: #a4a8a5; /* Color del botón */\n"
"    border-radius: 15px;       /* Borde redondeado, ajusta el valor para más curvatura */\n"
"    border: 2px solid #808080; /* Opcional: agrega un borde de color gris */")
        self.tableWidgetDetallesRegistro.setObjectName("tableWidgetDetallesRegistro")
        self.tableWidgetDetallesRegistro.setColumnCount(0)
        self.tableWidgetDetallesRegistro.setRowCount(0)
        self.label_62 = QtWidgets.QLabel(self.pageDetallesRegistro)
        self.label_62.setGeometry(QtCore.QRect(380, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.stackedWidget.addWidget(self.pageDetallesRegistro)
        self.widgetBarraVertical.raise_()
        self.widgetTitulo.raise_()
        self.stackedWidget.raise_()
        self.configurar_botones()
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Veterinaria"))
        self.label_2.setText(_translate("Form", "Veterinaria "))
        self.label_5.setText(_translate("Form", "General"))
        self.label_6.setText(_translate("Form", "Agregar Usuarios "))
        self.label_7.setText(_translate("Form", "Tarifas"))
        self.label_8.setText(_translate("Form", "Contaduria"))
        self.label_9.setText(_translate("Form", "Usuarios"))
        self.label_10.setText(_translate("Form", "Registros"))
        self.label_3.setText(_translate("Form", "Dinero En Caja Mes "))
        self.label_13.setText(_translate("Form", "Citas Completadas"))
        self.label_15.setText(_translate("Form", "Citas Agendadas"))
        self.label_17.setText(_translate("Form", "Animales Atendidos"))
        self.label_22.setText(_translate("Form", "Perros"))
        self.label_23.setText(_translate("Form", "Gatos"))
        self.label_20.setText(_translate("Form", "Moneda: COP"))
        self.labelFecha.setText(_translate("Form", "Miercoles 19 de febrero 2025"))
        self.label_11.setText(_translate("Form", "Datos Propietario:"))
        self.label_24.setText(_translate("Form", "Usuario:"))
        self.label_93.setText(_translate("Form", "Contraseña:"))
        self.label_30.setText(_translate("Form", "Rol:"))
        self.label_12.setText(_translate("Form", "Nombre: "))
        self.label_25.setText(_translate("Form", "Cedula: "))
        self.label_26.setText(_translate("Form", "Correo:"))
        self.label_27.setText(_translate("Form", "Telefono:"))
        self.label_28.setText(_translate("Form", "Direccion:"))
        self.pushButtonRegresarRegistrar.setText(_translate("Form", "Regresar"))
        self.pushButtonAgregarMascota.setText(_translate("Form", "Agregar Mascotas"))
        self.pushButtonCrear.setText(_translate("Form", "Crear"))
        self.label_96.setText(_translate("Form", "Nombre"))
        self.label_98.setText(_translate("Form", "Especie:"))
        self.label_99.setText(_translate("Form", "Raza:"))
        self.label_100.setText(_translate("Form", "Color:"))
        self.label_102.setText(_translate("Form", "Tamaño:"))
        self.label_103.setText(_translate("Form", "Fecha de Nacimiento:"))
        self.pushButtonRegistrarMascota.setText(_translate("Form", "Registrar Mascota"))
        self.pushButtonRegresarMascota.setText(_translate("Form", "Regresar"))
        self.label_29.setText(_translate("Form", "Datos Mascota:"))
        self.label_36.setText(_translate("Form", "Lista de Usuarios Y Mascotas:"))
        self.label_42.setText(_translate("Form", "Cedula: "))
        self.lineEditCedulaLista.setPlaceholderText(_translate("Form", "Buscar por cedula..."))
        self.label_45.setText(_translate("Form", "Nombre Cliente:"))
        self.lineEditNombreLista.setPlaceholderText(_translate("Form", "Buscar por Nombre..."))
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
        self.label_53.setText(_translate("Form", "Establecer Tarifas"))
        self.label_54.setText(_translate("Form", "Tipo de Servicio: "))
        self.label_57.setText(_translate("Form", "Horario:"))
        self.label_56.setText(_translate("Form", "Tarifa Por Periodo:"))
        self.pushButtonTarifaHorario.setText(_translate("Form", "Agregar Tarifa "))
        self.pushButtonRegresarTarifa.setText(_translate("Form", "Regresar"))
        self.pushButtonEliminarTarifa.setText(_translate("Form", "Eliminar Tarifa"))
        self.label_70.setText(_translate("Form", "Contaduría "))
        self.label_71.setText(_translate("Form", "Desde:"))
        self.label_72.setText(_translate("Form", "Hasta:"))
        self.label_73.setText(_translate("Form", "Periodo:"))
        self.label_74.setText(_translate("Form", "Estado"))
        self.pushButtonRegresarContaduria.setText(_translate("Form", "Regresar"))
        self.pushButtonDetallesContaduria.setText(_translate("Form", "Ver Detalles"))
        self.pushButtonExportarContaduria.setText(_translate("Form", "Exportar"))
        self.label_75.setText(_translate("Form", "Detalles del Registro"))
        self.label_80.setText(_translate("Form", "Nombre: "))
        self.label_81.setText(_translate("Form", "Cedula: "))
        self.label_82.setText(_translate("Form", "Telefono:"))
        self.label_83.setText(_translate("Form", "Direccion:"))
        self.label_85.setText(_translate("Form", "Nombre Mascota:"))
        self.label_76.setText(_translate("Form", "Raza:"))
        self.label_77.setText(_translate("Form", "Servicio:"))
        self.label_78.setText(_translate("Form", "Tipo Vehiculo:"))
        self.label_79.setText(_translate("Form", "Estado:"))
        self.label_84.setText(_translate("Form", "Fecha: "))
        self.label_86.setText(_translate("Form", "Hora:"))
        self.label_87.setText(_translate("Form", "Valor Pagado:"))
        self.pushButtonImprimirDetalles.setText(_translate("Form", "Imprimir Factura"))
        self.pushButtonRegresarDetallesFactura.setText(_translate("Form", "Regresar"))
        self.pushButtonRegresarUsuarios.setText(_translate("Form", "Regresar"))
        self.label_55.setText(_translate("Form", "Usuarios:"))
        self.pushButtonModificarUsuarios.setText(_translate("Form", "Modificar"))
        self.label_48.setText(_translate("Form", "Cedula: "))
        self.lineEditCedulaUsuarios.setPlaceholderText(_translate("Form", "Buscar por cedula..."))
        self.label_49.setText(_translate("Form", "Nombre Cliente:"))
        self.lineEditNombreUsuarios.setPlaceholderText(_translate("Form", "Buscar por Nombre..."))
        self.label_58.setText(_translate("Form", "Usuario:"))
        self.lineEditUsuarioUsuarios.setPlaceholderText(_translate("Form", "Buscar por Usuario..."))
        self.pushButtonRegresarRegistro.setText(_translate("Form", "Regresar"))
        self.label_62.setText(_translate("Form", "Detalles del Registro"))


    def configurar_botones(self):
        
        """Asigna cada botón a la página correspondiente en el QStackedWidget."""
        self.pushButtonGeneral.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonRegistrarUsuarios.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButtonTarifas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.pushButtonContaduria.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.pushButtonUsuarios.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.pushButtonRegistros.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))

