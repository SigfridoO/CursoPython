__author__ = "Sigfrido"
__date__ = "14-mar-2023 21:10:00"

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Semaforo.InterfazPantalla import InterfazPantalla
from Semaforo.Programa import Programa

from blessed import Terminal

ruta = os.path.dirname(os.path.abspath(__file__)) + os.sep
rutaUsuario = os.path.expanduser('~') + os.sep
term = Terminal()

sys.path.append(ruta)
sys.path.append(os.path.join(ruta, ".."))


class Inicio(InterfazPantalla, Programa):
    def __init__(self):
        InterfazPantalla.__init__(self)
        Programa.__init__(self)
        self.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec())
