__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"

import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)

from Semaforo.ControladoraRasp import Controladora
from Controladora.Temporizador import Temporizador
from enum import Enum


class ProyectoBase:

    def __init__(self):

        # Estableciendo señales digitales fisicas
        self.botonArranque = False
        self.botonPAro = False

        self.lamparaMotor1 = False
        self.lamparaMotor2 = False
        self.lamparaGiroMotor2 = False
        self.lamparaEnOperacion = False
        self.lamparaAlarma = False

        #self.motor1 = MotorPasos()
        #self.motor2 = MotorConPuenteH()


        self.estado = SecuenciaDeOperacion.inicializacion
        self.TON_0 = Temporizador("TON_0", 1)
        self.TON_1 = Temporizador("TON_1", 6)
        self.TON_2 = Temporizador("TON_2", 2)

        self.worker = None
        self.controladora: Controladora = None

    def run(self):
        tarea1 = threading.Thread(target=self.iniciar)
        tarea1.start()

    def iniciar(self):
        while True:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()

            if self.TON_0.salida:

                print(self)

            # if self.controladora:
            #     self.controladora.activarPin(0, self.luzRoja)
            #     self.controladora.activarPin(1, self.luzAmarilla)
            #     self.controladora.activarPin(2, self.luzVerde)
            #     self.entrada_00 = self.controladora.X_01

            # if self.worker:
            #     self.worker.senal_luz_roja(self.luzRoja)
            #     self.worker.senal_luz_amarilla(self.luzAmarilla)
            #     self.worker.senal_luz_verde(self.luzVerde)
            #     self.worker.actualizar_variable_digital(self.entrada_00)
            #     self.worker.actualizar_variable_analogica(str(self.TON_0.tiempoActual))

    def establecer_worker(self, worker):
        self.worker = worker

    def establecer_controladora(self, controladora):
        self.controladora = controladora

    def __str__(self):
        return "Arranque: " + str(self.botonArranque) + \
            ", Paro: " + str(self.botonPAro) 

class SecuenciaDeOperacion(Enum):
    inicializacion = 0
    calibracion =1

def main():
    miProyecto = ProyectoBase()
    # print(miSemaforo)
    # miSemaforo.iniciarSemaforo()
    miProyecto.run()


if __name__ == "__main__":
    main()
