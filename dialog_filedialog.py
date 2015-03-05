from PyQt4.QtGui import (QApplication, QDialog, QVBoxLayout, QPushButton,
        QFileDialog, QLabel)
import sys

LINEA = 0

'''
with open('signals.py', 'r') as f:
    for line in f:
        LINEA += 1
    print LINEA
'''


class CuentaL(QDialog):

    def __init__(self):
        super(CuentaL, self).__init__()

        self.setWindowTitle('Cuenta lineas')

        vbox = QVBoxLayout(self)

        self.boton = QPushButton('Abrir archivo')
        self.label = QLabel('')
        self.label.hide()

        vbox.addWidget(self.boton)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.boton.clicked.connect(self.dialogo)

    def dialogo(self):
        self.lineas = 0

        archivo = QFileDialog.getOpenFileName(self, 'Abrir archivo')
        if archivo:
            self.abrir_archivo(archivo)

    def abrir_archivo(self, archivo):
        with open(archivo, 'r') as f:
            for line in f:
                self.lineas += 1

        self.mostrar(self.lineas)

    def mostrar(self, lineas):
        self.label.setText('El archivo tiene <b>%d</b> lineas' % (self.lineas))
        self.label.show()

app = QApplication(sys.argv)
w = CuentaL()
w.show()

sys.exit(app.exec_())
