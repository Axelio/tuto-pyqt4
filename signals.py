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

        #self.resize(600, 600)

        # Mover posicion de la ventana
        # 200 hacia abajo, 100 hacia la derecha
        self.move(200, 100)

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % config.LOGO_APP))

        #LAYOUT
        vbox = QVBoxLayout(self)

        self.boton = QPushButton("Saludar")
        self.cerrar = QPushButton("Cerrar")
        self.label = QLabel("")
        self.label.hide() #Esconder el texto

        # Signal
        self.boton.clicked.connect(self.saludar)
        self.cerrar.clicked.connect(self.close)

        vbox.addWidget(self.boton)
        vbox.addWidget(self.cerrar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def saludar(self):
        self.label.setText("<h1>Hola mundo!</h1>")

        if self.label.isHidden():
            self.label.show()
        else:
            self.label.hide()

app = QApplication(sys.argv)
ventana = Signals()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
