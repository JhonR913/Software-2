from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QSlider, QMessageBox, QPushButton, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

class CaptchaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Captcha')
        self.setGeometry(700, 400, 600, 200)

        # Cambiar el fondo de la ventana a negro
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta de instrucción
        self.label = QLabel('Desliza esto para verificar', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 18px;")  # Estilo de la etiqueta
        layout.addWidget(self.label)

        # Slider (barra deslizante)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setStyleSheet("QSlider::groove:horizontal { background: #444; height: 20px; }"  # Aumentar el grosor de la barra
                                  "QSlider::handle:horizontal { background: #888; width: 20px; }"  # Estilo del handle
                                  "QSlider::sub-page:horizontal { background: blue; }")  # Parte deslizante en azul
        layout.addWidget(self.slider)

        # Botón para verificar si el captcha se completó correctamente
        self.verify_button = QPushButton('Verificar', self)
        self.verify_button.setStyleSheet("background-color: #1E1E1E; color: white; font-size: 16px;")  # Estilo del botón
        layout.addWidget(self.verify_button)

        # Conectar el botón de verificación a la función de validación
        self.verify_button.clicked.connect(self.check_captcha)

        # Conectar el slider para actualizar el progreso
        self.slider.valueChanged.connect(self.update_slider)

        # Configurar el layout en la ventana
        self.setLayout(layout)

    def update_slider(self):
        # Actualizar el color del slider
        self.slider.setStyleSheet(
            f"QSlider::groove:horizontal {{ background: #444; height: 20px; }}"  # Grosor aumentado
            f"QSlider::handle:horizontal {{ background: #888; width: 20px; }}"
            f"QSlider::sub-page:horizontal {{ background: blue; width: {self.slider.value()}px; }}")  # Cambiar el ancho de la sub-página a medida que se desliza

    def check_captcha(self):
        if self.slider.value() == 100:
            QMessageBox.information(self, 'Captcha', 'Verificación completada.')
            self.accept()  # Cerrar el diálogo de captcha y permitir el acceso
        else:
            QMessageBox.warning(self, 'Captcha', 'Por favor, desliza la barra hasta el final para verificar.')

