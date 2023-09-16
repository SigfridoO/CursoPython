import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        #super().__init__()
        QMainWindow.__init__(self)
        # Propiedades de la ventana
        self.resize(500, 200)
        self.setMinimumSize(300, 100)
        self.setMaximumSize(600, 500)
        self.setWindowTitle('Mi primera interfaz gráfica')

        # Boton
        boton = QPushButton('presioname')

        # El boton se agrega a la ventana principal
        self.setCentralWidget(boton)

        # Funciones del botón
        boton.clicked.connect(self.botonClicado)
        boton.pressed.connect(self.botonPresionado)
        boton.released.connect(self.botonLiberado)

    def botonClicado(self):
        print('Boton clicado')

    def botonPresionado(self):
        print('Boton presionado')

    def botonLiberado(self):
        print('boton liberado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())
