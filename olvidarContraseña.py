
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from datetime import datetime, timedelta
import data_rc
from cambiarContraseña import Ui_Dialog as Ui_cambiarContrasena


def connect_to_database():
    return mysql.connector.connect(
        host="34.70.72.185",
        port=3306,
        user="root",
        password="Jhonr2005",
        database="veterinaria"
    )
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1041, 714)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1091, 761))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1201, 801))
        self.label.setStyleSheet("background-color:rgba(0,0,0);\n"
"border-top-left-radius: 7px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1041, 761))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/images/images/fondo2.png);\n"
"border-top-left-radius: 7px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 711, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0)")
        self.label_3.setObjectName("label_3")
        self.lineEditCorreo = QtWidgets.QLineEdit(self.widget)
        self.lineEditCorreo.setGeometry(QtCore.QRect(480, 260, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditCorreo.setFont(font)
        self.lineEditCorreo.setStyleSheet("background-color: rgba(100, 100, 100);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEditCorreo.setText("")
        self.lineEditCorreo.setMaxLength(32788)
        self.lineEditCorreo.setObjectName("lineEditCorreo")
        self.lineEditCodigo = QtWidgets.QLineEdit(self.widget)
        self.lineEditCodigo.setGeometry(QtCore.QRect(480, 360, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditCodigo.setFont(font)
        self.lineEditCodigo.setStyleSheet("background-color: rgba(100, 100, 100);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEditCodigo.setText("")
        self.lineEditCodigo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditCodigo.setObjectName("lineEditCodigo")
        self.pushButtonEnviar = QtWidgets.QPushButton(self.widget)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(470, 470, 260, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonEnviar.setFont(font)
        self.pushButtonEnviar.setStyleSheet("QPushButton#pushButtonEnviar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100), stop:1 rgba(60, 60, 60));\n"
"    color: rgba(0, 0, 0);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonEnviar:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150), stop:1 rgba(80, 80, 80));\n"
"}\n"
"\n"
"QPushButton#pushButtonEnviar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120);\n"
"}\n"
"")
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(80, 260, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(90, 360, 371, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0,0,0)")
        self.label_5.setObjectName("label_5")
        self.pushButtonRegresar = QtWidgets.QPushButton(self.widget)
        self.pushButtonRegresar.setGeometry(QtCore.QRect(380, 600, 260, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRegresar.setFont(font)
        self.pushButtonRegresar.setStyleSheet("QPushButton#pushButtonRegresar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100), stop:1 rgba(60, 60, 60));\n"
"    color: rgba(0, 0, 0);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonRegresar:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150), stop:1 rgba(80, 80, 80));\n"
"}\n"
"\n"
"QPushButton#pushButtonRegresar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120);\n"
"}\n"
"")
        self.pushButtonRegresar.setObjectName("pushButtonRegresar")
        self.pushButtonVerificar = QtWidgets.QPushButton(self.widget)
        self.pushButtonVerificar.setGeometry(QtCore.QRect(740, 470, 260, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonVerificar.setFont(font)
        self.pushButtonVerificar.setStyleSheet("QPushButton#pushButtonVerificar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100), stop:1 rgba(60, 60, 60));\n"
"    color: rgba(0, 0,0);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonVerificar:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150), stop:1 rgba(80, 80, 80));\n"
"}\n"
"\n"
"QPushButton#pushButtonVerificar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120);\n"
"}\n"
"")
        self.pushButtonVerificar.setObjectName("pushButtonVerificar")
        self.pushButtonEnviar.clicked.connect(self.generar_y_enviar_codigo)
        self.pushButtonVerificar.clicked.connect(self.verificar_codigo)
        self.codigo_guardado = None
        self.usuario_id = None
        self.dialog_cambiar_contrasena = None

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Recuperar"))
        self.label_3.setText(_translate("Dialog", "Recuperación de Contraseña"))
        self.pushButtonEnviar.setText(_translate("Dialog", "Enviar Codigo"))
        self.label_4.setText(_translate("Dialog", " Correo Electronico:"))
        self.label_5.setText(_translate("Dialog", "Codigo Recuperacion:"))
        self.pushButtonRegresar.setText(_translate("Dialog", "Regresar"))
        self.pushButtonVerificar.setText(_translate("Dialog", "Verificar"))


    def generar_codigo(self):
        return str(random.randint(100000, 999999))

    def enviar_codigo_correo(self, correo, codigo):
        remitente = "soporte.sig2024@gmail.com"
        password = "ayrk muxo vzdv mesl"
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = correo
        mensaje['Subject'] = "Código de recuperación de contraseña"
        cuerpo = f"Tu código de recuperación es: {codigo}. Este código expira en 10 minutos."
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        try:
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()
            servidor.login(remitente, password)
            servidor.sendmail(remitente, correo, mensaje.as_string())
            servidor.quit()
            QtWidgets.QMessageBox.information(None, "Éxito", "Correo enviado correctamente.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error al enviar el correo: {e}")

    def generar_y_enviar_codigo(self):
        correo = self.lineEditCorreo.text().strip()
        conexion = connect_to_database()
        if not conexion:
            return  # Finaliza si no hay conexión

        cursor = conexion.cursor()
        cursor.execute("SELECT ID FROM DatosUsuarios WHERE CorreoElectronico = %s", (correo,))
        usuario = cursor.fetchone()
        
        if usuario:
            # Almacena la ID del usuario en la variable de instancia
            self.usuario_id = usuario[0]
            self.codigo_guardado = self.generar_codigo()
            self.enviar_codigo_correo(correo, self.codigo_guardado)
        else:
            QtWidgets.QMessageBox.warning(None, "Usuario no encontrado", "No se encontró un usuario con ese correo electrónico.")
        
        cursor.close()
        conexion.close()

    def verificar_codigo(self):
     codigo_ingresado = self.lineEditCodigo.text().strip()
     if codigo_ingresado == self.codigo_guardado:
         QtWidgets.QMessageBox.information(None, "Código correcto", "El código es correcto.")
         self.lineEditCorreo.clear()
         self.codigo_guardado = None
         # Llama al método para abrir la ventana de cambio de contraseña
         self.abrir_cambiar_contrasena(self.usuario_id)
     else:
         QtWidgets.QMessageBox.warning(None, "Código incorrecto", "El código ingresado no es correcto.")

    def abrir_cambiar_contrasena(self, usuario_id):
     # Inicializa y muestra la ventana de cambio de contraseña
      self.dialog_cambiar_contrasena = QtWidgets.QDialog()
      self.ui_cambiar_contrasena = Ui_cambiarContrasena(usuario_id)
      self.ui_cambiar_contrasena.setupUi(self.dialog_cambiar_contrasena)
      self.ui_cambiar_contrasena.pushButtonRegresar.clicked.connect(self.close_cambiar_contrasena_window)
      self.dialog_cambiar_contrasena.exec_()
    
    def close_cambiar_contrasena_window(self):
    
      if self.dialog_cambiar_contrasena:
        self.dialog_cambiar_contrasena.close()
        self.dialog_cambiar_contrasena = None
