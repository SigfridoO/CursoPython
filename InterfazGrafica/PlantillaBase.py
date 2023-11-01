from PySide6.QtWidgets import QApplication, QMainWindow
import sys


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
