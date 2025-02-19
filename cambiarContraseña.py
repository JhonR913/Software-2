

from PyQt5 import QtCore, QtGui, QtWidgets
import bcrypt
import mysql.connector
import data_rc


class Ui_Dialog(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
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
        self.label_3.setGeometry(QtCore.QRect(190, 60, 691, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0)")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(480, 260, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(100, 100, 100);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32788)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 360, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(100, 100, 100);  /* Color de fondo gris oscuro */\n"
"    border: none;\n"
" \n"
"    color: rgba(255, 255, 255);  /* Color del texto blanco */\n"
"    padding-bottom: 7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(470, 450, 260, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 100, 100), stop:1 rgba(60, 60, 60));\n"
"    color: rgba(0, 0, 0);  /* Color del texto en blanco */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 150, 150), stop:1 rgba(80, 80, 80));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(120, 120, 120);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(90, 260, 341, 51))
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
        self.label_5.setGeometry(QtCore.QRect(90, 360, 361, 60))
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
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(50, 600, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(0,0,0)")
        self.label_6.setObjectName("label_6")
        self.pushButtonRegresar = QtWidgets.QPushButton(self.widget)
        self.pushButtonRegresar.setGeometry(QtCore.QRect(740, 450, 260, 61))
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
        self.pushButton.clicked.connect(self.actualizar_contrasena)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def connect_to_database(self):       
      return mysql.connector.connect(
      host="34.70.72.185",
      port=3306,
      user="root",
      password="Jhonr2005",
      database="veterinaria"
      )
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Recuperación de Contraseña"))
        self.pushButton.setText(_translate("Dialog", "Cambiar"))
        self.label_4.setText(_translate("Dialog", "Nueva Contraseña:"))
        self.label_5.setText(_translate("Dialog", "Confirmar Contraseña:"))
        self.label_6.setText(_translate("Dialog", "la contraseña es unica y intransferible"))
        self.pushButtonRegresar.setText(_translate("Dialog", "Regresar"))

    def actualizar_contrasena(self):
        nueva_contraseña = self.lineEdit.text()
        confirmar_contraseña = self.lineEdit_2.text()

        if nueva_contraseña == confirmar_contraseña:
            # Cifrar la contraseña
            hashed_password = bcrypt.hashpw(nueva_contraseña.encode('utf-8'), bcrypt.gensalt())
            
            # Conectar a la base de datos y actualizar la contraseña
            conn = None
            cursor = None
            try:
                conn = self.connect_to_database()
                cursor = conn.cursor()
                query = "UPDATE Usuarios SET Contraseña = %s WHERE ID = %s"
                cursor.execute(query, (hashed_password, self.usuario_id))
                conn.commit()
                
                QtWidgets.QMessageBox.information(None, "Éxito", "Contraseña actualizada exitosamente.")
                
            except mysql.connector.Error as e:
                QtWidgets.QMessageBox.critical(None, "Error", f"No se pudo actualizar la contraseña: {e}")
                
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Las contraseñas no coinciden. Por favor, intente nuevamente.")