from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PySide6.QtCore import Qt
import sys

from InterfazGrafica.Caja import Caja

from pathlib import Path


def absPath(archivo):
    return str(Path(__file__).parent.absolute() / archivo)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 600)

        layout = QGridLayout()
        miCaja = Caja('green')
        # miCaja.setFixedWidth(50)
        miCaja.setFixedSize(50,80)
        layout.addWidget(miCaja,0, 0)

        self.cajaDeAnimacion = QLabel()
        layout.addWidget(self.cajaDeAnimacion, 1, 2)

        layout.addWidget(Caja('red'),2, 1, 2, 2)
        layout.addWidget(Caja('orange'),1, 0, 3, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        milistaDeImagenes = []
        imagen1 = QPixmap(absPath('ELEMENTOS2/KV102A_ROJO.bmp'))
        imagen2 = QPixmap(absPath('ELEMENTOS2/KV102A_VERDE.bmp'))
        milistaDeImagenes.append(imagen1)
        milistaDeImagenes.append(imagen2)



        self.cajaDeAnimacion.setPixmap(imagen1)



    def activarAnimacion(self, valor):
        self.cajaDeAnimacion.setPixmap()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
