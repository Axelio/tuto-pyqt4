from PyQt4.QtGui import (QWidget, QMenuBar, QApplication, QVBoxLayout)


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.setWindowTitle(self.tr('QMenuBar'))

        menu = QMenuBar(self)
        vbox = QVBoxLayout(self)
        self.archivo = menu.addMenu('&Archivo')
        self.editar = menu.addMenu('&Editar')
        self.cerrar = menu.addMenu('&Cerrar')

        vbox.addWidget(menu)


if __name__ == '__main__':
    import sys

    app = QApplication([])
    w = Widget()
    w.show()


    sys.exit(app.exec_())
