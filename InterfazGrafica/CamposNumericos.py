from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox
import sys


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)

        # numero = QSpinBox()
        # numero.setRange(5, 15)
        # self.setCentralWidget(numero)

        numero = QDoubleSpinBox()
        numero.setRange(15, 90)
        numero.setSingleStep(0.5)
        numero.setSuffix(" º")
        numero.setPrefix(" $ ")

        numero.valueChanged.connect(self.cambiarValor)

        self.setCentralWidget(numero)

    def cambiarValor(self, numero):
        print(numero)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())