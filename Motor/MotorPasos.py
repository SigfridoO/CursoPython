__author__ = "Sigfrido Soria"
__date__ = "13-oct-2023 04:17:00"

from Controladora.Temporizador import Temporizador
import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)

from Semaforo.ControladoraRasp import Controladora


class MotorPasos:

    def __init__(self):

        self.entrada_00 = None
        self.salida_00 = False
        self.salida_01 = False
        self.salida_02 = False
        self.salida_03 = False

        self.estado = 0
        self.TON_0 = Temporizador("TON_0", 1)
        self.TON_1 = Temporizador("TON_1", 6)
        self.TON_2 = Temporizador("TON_2", 2)

        self.worker = None
        self.controladora: Controladora = None
        print('Dentro del motor a pasos')

    def run(self):
        tarea1 = threading.Thread(target=self.iniciar_semaforo)
        tarea1.start()

    def iniciar_semaforo(self):
        self.estado = 0
        cuentaMaxima = 3
        print('Iniciando control')
        while True:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()

            if self.TON_0.salida:
                self.estado += 1

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
                #     self.entrada_00 = self.controladora.X_01
                #
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
        return "Sal: " + str(1 if self.salida_00 else 0) + \
            " " + str(1 if self.salida_01 else 0) + \
            " " + str(1 if self.salida_02 else 0) + \
            " " + str(1 if self.salida_03 else 0)


def main():
    motor = MotorPasos()
    # print(miSemaforo)
    # miSemaforo.iniciarSemaforo()
    motor.run()


if __name__ == "__main__":
    main()
