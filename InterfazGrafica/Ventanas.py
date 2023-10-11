from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
import sys

class SubVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 280)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle('Ventana Principal')

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        boton = QPushButton("Mostrar")
        boton.clicked.connect(self.mostrar)
        layout.addWidget(boton)


    def mostrar(self):
        self.subventana = SubVentana()
        self.subventana.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())