from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        layout = QVBoxLayout()

        miCaja1 = Caja("green")
        miCaja2 = Caja("blue")
        miCaja3 = Caja("red")

        layout.addWidget(miCaja1)
        layout.addWidget(miCaja2)
        layout.addWidget(miCaja3)

        self.setCentralWidget()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())