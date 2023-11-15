from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from disenio1 import Ui_MainWindow


class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
