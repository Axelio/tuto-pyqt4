'''
Un widget determinado emite una senal determinada

Widget > Senal
Boton > click

Un Slot es una funcion o metodo en python
'''

# stdlib imports
import sys

# core pyqt
from PyQt4.QtGui import (QApplication, QIcon, QWidget, QComboBox, QLineEdit,
        QVBoxLayout)

# import app
from settings import base as config


class Signals(QWidget):

    def __init__(self):
        super(Signals, self).__init__()

        # Titulo de la ventana
        self.setWindowTitle("Combobox y Line edit")

        #self.resize(600, 600)

        # Mover posicion de la ventana
        # 200 hacia abajo, 100 hacia la derecha
        self.move(200, 100)

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % config.LOGO_APP))

        # Widgets
        vbox = QVBoxLayout(self)

        self.combo = QComboBox()
        self.line = QLineEdit()

        vbox.addWidget(self.combo)
        vbox.addWidget(self.line)

app = QApplication(sys.argv)
ventana = Signals()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
