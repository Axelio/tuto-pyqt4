'''
Un widget determinado emite una senal determinada

Widget > Senal
Boton > click

Un Slot es una funcion o metodo en python
'''

# stdlib imports
import sys

# core pyqt
from PyQt4.QtGui import (QWidget, QApplication, QIcon, QPushButton,
    QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout)

# import app
from settings import base as config


class Signals(QWidget):

    def __init__(self):
        super(Signals, self).__init__()

        # Titulo de la ventana
        self.setWindowTitle("Signals and Slots")

        # Dimensione de la ventana
        self.resize(1200, 600)

        # Mover posicion de la ventana
        # 200 hacia abajo, 100 hacia la derecha
        self.move(200, 100)

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % config.LOGO_APP))

        boton = QPushButton("Saludar", self)
        cerrar = QPushButton("Cerrar", self)
        cerrar.move(0, 50)

        # Signal
        boton.clicked.connect(self.saludar)
        cerrar.clicked.connect(self.close)

    def saludar(self):
        print "Hola mundo!"

app = QApplication(sys.argv)
ventana = Signals()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
