# stdlib imports
import sys

# core pyqt
from PyQt4.QtGui import (QWidget, QApplication, QIcon, QPushButton,
    QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout)

# import app
from settings import base as config


class Ventana(QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        # Titulo de la ventana
        self.setWindowTitle("Grid Layout")

        # Dimensione de la ventana
        self.resize(1200, 600)

        # Mover posicion de la ventana
        # 200 hacia abajo, 100 hacia la derecha
        self.move(200, 100)

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % config.LOGO_APP))

        btn_1 = QPushButton('1', self)
        btn_2 = QPushButton('2', self)
        btn_3 = QPushButton('3', self)
        btn_4 = QPushButton('4', self)
        btn_5 = QPushButton('5', self)

        grilla = QGridLayout(self)
        grilla.addWidget(btn_1, 0, 0)
        grilla.addWidget(btn_2, 0, 1)
        grilla.addWidget(btn_3, 1, 0)
        grilla.addWidget(btn_4, 1, 1)
        grilla.addWidget(btn_5, 2, 0)


app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
