__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)

ruta = os.path.dirname(os.path.abspath(__file__)) + os.sep
rutaUsuario = os.path.expanduser('~') + os.sep

# from blessed import Terminal
# term = Terminal()

sys.path.append(ruta)
sys.path.append(os.path.join(ruta, ".."))

from ProyectoBase import ProyectoBase
from InterfazProyectoBase import InterfazProyectoBase
#from ControladoraRasp import Controladora


class Inicio(InterfazProyectoBase):
    def __init__(self):
        InterfazProyectoBase.__init__(self)

        miProyecto = ProyectoBase()
        miProyecto.run()
            
        miProyecto.establecer_worker(self.obtener_worker())

        #controladora = Controladora()
        #semaforo.establecer_controladora(controladora)

        # self.establecerInterfaz(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec())
