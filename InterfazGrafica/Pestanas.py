from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
import sys
from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        tabs = QTabWidget()

        tabs.addTab(Caja('orange'), 'Naranja')
        tabs.addTab(Caja('green'), 'Verde')
        tabs.addTab(Caja('yellow'), 'Amarillo')
        tabs.setTabPosition(QTabWidget.South)

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
