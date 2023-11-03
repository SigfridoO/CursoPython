__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"


import threading
import sys
import os
import serial

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)
from Controladora.Temporizador import Temporizador


class Comunicacion:

    def __init__(self):

        self.TON_0 = Temporizador("TON_0", 1)
        self.puerto_serie = serial.Serial("/dev/ttyS0", baudrate
        =9600, timeout = 1)


    def run(self):
        tarea1 = threading.Thread(target=self.iniciar)
        tarea1.start()

    def iniciar(self):

        contador = 0
        while True:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()


            if self.TON_0.salida:
                
                print (contador)
                contador+=1

                self.puerto_serie.write(contador)


    def __str__(self):
        return "contador: " 


def main():
    comunicacion = Comunicacion()
    # print(miSemaforo)
    # miSemaforo.iniciarSemaforo()
    comunicacion.run()


if __name__ == "__main__":
    main()





import serial

import os
import time

puerto = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

