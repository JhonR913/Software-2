import sys
from PyQt5 import QtWidgets
import mysql.connector
from captcha import CaptchaWindow
from Inicio import Ui_Form as Ui_Login 
from GestionAdmin import Ui_Form as Ui_Admin
from olvidarContraseña import Ui_Dialog as Ui_RecuperarContrasena
import bcrypt




def connect_to_database():
    return mysql.connector.connect(
        host="34.70.72.185",
        port=3306,
        user="root",
        password="Jhonr2005",
        database="veterinaria"
    )

class MainWindow(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_id = None  # Guardar el ID del usuario
        self.user_role = None
        self.admin_window = None
        
        self.pushButtonIngresar.clicked.connect(self.login)
        self.passwordVisible = False
        self.pushButtonVer.clicked.connect(self.togglePasswordVisibility)
        self.forgotPasswordButton.clicked.connect(self.openForgotPasswordWindow)

    def login(self):
        username = self.lineEditUsuario.text()
        password = self.lineEditContrasenia.text()

        db = connect_to_database()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Usuarios WHERE NombreUsuario = %s", (username,))
        result = cursor.fetchone()

        if result:
            if result['Estado'] == 'Inactivo':
                QtWidgets.QMessageBox.warning(self, "Usuario inactivo", "Su usuario está inactivo, contacte al administrador.")
                cursor.execute("INSERT INTO IntentosDeAcceso (UsuarioID, FechaHora, Estado) VALUES (%s, CURRENT_TIMESTAMP, 'Fallido')", (result['ID'],))
                db.commit()
            else:
                if bcrypt.checkpw(password.encode('utf-8'), result['Contraseña'].encode('utf-8')):
                    if result['IntentosFallidos'] == 2:
                        self.open_captcha(result)  # Abre captcha si ya falló dos veces
                    else:
                        self.handle_successful_login(result)
                else:
                    self.handle_failed_login(result)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")
            cursor.execute("INSERT INTO IntentosDeAcceso (UsuarioID, FechaHora, Estado) VALUES (NULL, CURRENT_TIMESTAMP, 'Fallido')")
            db.commit()
        
        db.close()

    def handle_failed_login(self, user_result):
        nuevos_intentos = user_result['IntentosFallidos'] + 1
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("UPDATE Usuarios SET IntentosFallidos = %s WHERE ID = %s", (nuevos_intentos, user_result['ID']))
        cursor.execute("INSERT INTO IntentosDeAcceso (UsuarioID, FechaHora, Estado) VALUES (%s, CURRENT_TIMESTAMP, 'Fallido')", (user_result['ID'],))
        db.commit()
        db.close()

        if nuevos_intentos == 2:
            QtWidgets.QMessageBox.warning(self, "Atención", "Último intento antes de bloquearse. Complete el captcha.")
        elif nuevos_intentos >= 3:
            cursor.execute("UPDATE Usuarios SET Estado = 'Inactivo' WHERE ID = %s", (user_result['ID'],))
            db.commit()
            QtWidgets.QMessageBox.warning(self, "Usuario bloqueado", "Su usuario ha sido desactivado por intentos fallidos.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", f"Contraseña incorrecta. Intento {nuevos_intentos} de 3.")

    def open_captcha(self, user_result):
        self.captcha_window = CaptchaWindow()
        self.captcha_window.show()
        self.captcha_window.accepted.connect(lambda: self.handle_captcha_success(user_result))
        self.captcha_window.rejected.connect(lambda: QtWidgets.QMessageBox.critical(self, "Error", "Captcha no completado correctamente"))

    def handle_captcha_success(self, user_result):
        self.handle_successful_login(user_result)

    def handle_successful_login(self, user_result):
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("UPDATE Usuarios SET IntentosFallidos = 0, UltimoAcceso = CURRENT_TIMESTAMP WHERE ID = %s", (user_result['ID'],))
        cursor.execute("INSERT INTO IntentosDeAcceso (UsuarioID, FechaHora, Estado) VALUES (%s, CURRENT_TIMESTAMP, 'Exitoso')", (user_result['ID'],))
        db.commit()
        db.close()

        QtWidgets.QMessageBox.information(self, "Acceso concedido", "Bienvenido al sistema.")
        
        self.user_id = user_result['ID']
        self.user_role = user_result['Rol']

        if self.user_role == 'Administrador':
            self.open_admin_window()
            
    def open_admin_window(self):
     self.admin_window = QtWidgets.QMainWindow()  # Crea una nueva ventana
     self.ui = Ui_Admin()  # Instancia la interfaz
     self.ui.setupUi(self.admin_window)  # Aplica la UI a la ventana
     self.admin_window.show()
     self.close()

    def openForgotPasswordWindow(self):
        # Crear una nueva instancia de la ventana de recuperación de contraseña
         self.recover_password_window = QtWidgets.QDialog()
         self.ui_recover_password = Ui_RecuperarContrasena()
         self.ui_recover_password.setupUi(self.recover_password_window)

        # Conectar el botón de regresar a una función
         self.ui_recover_password.pushButtonRegresar.clicked.connect(self.show_login_window)
        
        # Mostrar la ventana de recuperación de contraseña
         self.recover_password_window.show()
        # Ocultar la ventana de inicio de sesión
         self.hide()
        
    def show_login_window(self):
        # Cerrar ventana de recuperación de contraseña si está abierta
         if self.recover_password_window:
             self.recover_password_window.close()
             self.recover_password_window = None

        # Cerrar las ventanas secundarias si están abiertas
         for window_attr in ['admin_window', 'client_window', 'lawyer_window']:
             window = getattr(self, window_attr, None)
             if window:
                 window.close()
                 setattr(self, window_attr, None)

        # Mostrar la ventana de inicio de sesión
         self.limpiar_campos()
         self.show()
         
    def togglePasswordVisibility(self):
        if self.passwordVisible:
            self.lineEditContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)  # Ocultar contraseña
        else:
            self.lineEditContrasenia.setEchoMode(QtWidgets.QLineEdit.Normal)  # Mostrar contraseña
        self.passwordVisible = not self.passwordVisible
        
    def limpiar_campos(self):
        self.lineEditContrasenia.clear()  
        self.lineEditUsuario.clear()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Cambiado de exec_() a show()
    sys.exit(app.exec_())
