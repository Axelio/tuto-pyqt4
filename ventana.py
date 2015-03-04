# stdlib imports
import sys

# core pyqt
from PyQt4.QtGui import (QWidget, QApplication, QIcon, QPushButton,
    QLabel, QHBoxLayout)

# import app
from settings import base as config


class Ventana(QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        # Titulo de la ventana
        self.setWindowTitle("Tutorial de PyQt")

        # Dimensione de la ventana
        self.resize(1200, 600)

        # Mover posicion de la ventana
        # 200 hacia abajo, 100 hacia la derecha
        self.move(200, 100)

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % config.LOGO_APP))

        # Botones
        boton = QPushButton('Boton 1', self)
        boton2 = QPushButton('Boton 2', self)

        # Posiciones
        # Forma 1
        boton2.move(300, 300)

        # Dimensiones
        boton.setGeometry(100, 200, 40, 70) # X, Y, Ancho, Alto

        # Etiquetas
        label = QLabel('<h1>Esto es una etiqueta</h1>', self)
        label.move(300, 0)

        # Layouts
        layout_horizontal = QHBoxLayout(self)
        layout_horizontal.addWidget(boton)
        layout_horizontal.addWidget(boton2)
        layout_horizontal.addWidget(label)
        self.setLayout(layout_horizontal)

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
