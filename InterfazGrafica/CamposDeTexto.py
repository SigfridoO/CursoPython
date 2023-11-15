from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 50)

        self.texto = QLineEdit()
        self.texto.setMaxLength(15)
        self.texto.setPlaceholderText("Escribe algo")
        # texto.textChanged.connect(self.cambiarTexto)
        self.texto.returnPressed.connect(self.cambiarTextoConEnter)
        self.setCentralWidget(self.texto)

    def cambiarTexto(self, texto):
        print(texto)

    def cambiarTextoConEnter(self):
        print(self.texto.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())