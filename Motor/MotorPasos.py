__author__ = "Sigfrido Soria"
__date__ = "13-oct-2023 04:17:00"


import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)
from Controladora.Temporizador import Temporizador
from Semaforo.ControladoraRasp import Controladora


class MotorPasos:

    def __init__(self):

        self.entrada_00 = None
        
        self.salida_00 = False
        self.salida_01 = False
        self.salida_02 = False
        self.salida_03 = False

        self.estado = 0
        self.TON_0 = Temporizador("TON_0", 0.05)


        self.worker = None
        self.controladora: Controladora = None
        print('Dentro del motor a pasos')

    def run(self):
        tarea1 = threading.Thread(target=self.iniciar)
        tarea1.start()

    def iniciar(self):
        self.estado = 0
        cuentaMaxima = 3
        print('Iniciando control')
        while True:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()

            if self.TON_0.salida:
                self.estado -= 1

                if self.estado > cuentaMaxima:
                    self.estado = 0

                if self.estado < 0:
                    self.estado = cuentaMaxima
                print("estado:", self.estado)

                if self.estado == 0:
                    self.salida_00 = True
                    self.salida_01 = False
                    self.salida_02 = False
                    self.salida_03 = False

                if self.estado == 1:
                    self.salida_00 = False
                    self.salida_01 = True
                    self.salida_02 = False
                    self.salida_03 = False

                if self.estado == 2:
                    self.salida_00 = False
                    self.salida_01 = False
                    self.salida_02 = True
                    self.salida_03 = False

                if self.estado == 3:
                    self.salida_00 = False
                    self.salida_01 = False
                    self.salida_02 = False
                    self.salida_03 = True

                print(self)

                if self.controladora:
                    self.controladora.activarPin(0, self.salida_00)
                    self.controladora.activarPin(1, self.salida_01)
                    self.controladora.activarPin(2, self.salida_02)
                    self.controladora.activarPin(3, self.salida_03)

    def establecer_worker(self, worker):
        self.worker = worker

    def establecer_controladora(self, controladora):
        self.controladora = controladora

    def __str__(self):
        return "Sal: " + str(1 if self.salida_00 else 0) + \
            " " + str(1 if self.salida_01 else 0) + \
            " " + str(1 if self.salida_02 else 0) + \
            " " + str(1 if self.salida_03 else 0)


def main():
    motorAPasos = MotorPasos()
    # print(miSemaforo)
    # miSemaforo.iniciarSemaforo()



    controladora = Controladora()
    motorAPasos.establecer_controladora(controladora)

    motorAPasos.run()

if __name__ == "__main__":
    main()
