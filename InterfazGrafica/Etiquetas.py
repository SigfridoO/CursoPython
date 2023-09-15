from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    app =QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())