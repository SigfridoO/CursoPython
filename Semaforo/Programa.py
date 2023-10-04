__author__ = "Sigfrido"
__date__ = "4-oct-2023 05:10:00"

import os
import sys
import threading


ruta = os.path.dirname(os.path.abspath(__file__)) + os.sep
rutaUsuario = os.path.expanduser('~') + os.sep
# term = Terminal()

sys.path.append(ruta)
sys.path.append(os.path.join(ruta, ".."))

from Controladora.Temporizador import Temporizador

class Programa(threading.Thread):


    def __init__(self):
        threading.Thread.__init__(self)

        self.funcionando = None
        self.TON_01 = Temporizador("TON_01", 1)


    def run(self):
        self.funcionando = True
        contador = 0

        while self.funcionando:

            self.TON_01.entrada = not self.TON_01.salida
            self.TON_01.actualizar()

            if self.TON_01.salida:
                contador += 1
                print('Contador {}'.format(contador))

            if contador >= 65535:
                contador = 0

def main():
    programa = Programa()
    programa.start()

if __name__ == "__main__":
    main()



