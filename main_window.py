from PyQt4.QtGui import (QWidget, QAction, QApplication)


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(self.tr('MainWindow'))
        self.setMinimumSize(400, 300)

        self.accionSalir = QAction('Salir', self)
        self.accionSalir.setShortcut('Ctrl+Q')


if __name__ == '__main__':
    import sys

    app = QApplication([])
    w = MainWindow()
    w.show()


    sys.exit(app.exec_())
