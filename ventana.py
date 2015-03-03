# stdlib imports
import sys

# core pyqt
from PyQt4.QtGui import QWidget, QApplication, QIcon

# import app
import settings


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

        logo = settings.STATIC + 'img/python.svg'

        # Cambiar icono
        self.setWindowIcon(QIcon('%s' % logo))

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

# Mainoop: mantiene viva a la aplicacion
sys.exit(app.exec_())
