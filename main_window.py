from PyQt4.QtGui import (QMainWindow, QAction, QApplication, QTextEdit, QStatusBar)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(self.tr('MainWindow'))
        self.setMinimumSize(400, 300)

        widget = QTextEdit()
        self.setCentralWidget(widget)

        self.accionSalir = QAction('Salir', self)
        self.accionSalir.setShortcut('Ctrl+Q')
        self.accionSalir.setStatusTip('Salir de la aplicacion')

        # Barra de estado
        self.setStatusBar(QStatusBar())

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(self.accionSalir)


if __name__ == '__main__':
    import sys

    app = QApplication([])
    w = MainWindow()
    w.show()


    sys.exit(app.exec_())
