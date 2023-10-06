from Controladora.Temporizador import Temporizador
import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep)

from ControladoraRasp import Controladora


class Semaforo:

    def __init__(self):

        self.entrada_00 = None
        self.luzRoja = False
        self.luzVerde = False
        self.luzAmarilla = False

        self.estado = 0
        self.TON_0 = Temporizador("TON_0", 4)
        self.TON_1 = Temporizador("TON_1", 6)
        self.TON_2 = Temporizador("TON_2", 2)

        self.worker = None
        self.controladora: Controladora = None

    def run(self):
        tarea1 = threading.Thread(target=self.iniciarSemaforo)
        tarea1.start()

    def iniciarSemaforo(self):
        while True:
            self.TON_0.entrada = not self.TON_2.salida
            self.TON_0.actualizar()

            self.TON_1.entrada = self.TON_0.salida
            self.TON_1.actualizar()

            self.TON_2.entrada = self.TON_1.salida
            self.TON_2.actualizar()

            # print(self.TON_0, self.TON_1, self.TON_2)

            if not self.TON_0.salida and not self.TON_1.salida:
                self.estado = 0

            if self.TON_0.salida and not self.TON_1.salida:
                self.estado = 1

            if self.TON_0.salida and self.TON_1.salida:
                self.estado = 2

            # print ("Estado: ",  self.estado, ", Tiempo: ", self.TON_0.tiempoActual)

            if self.estado == 0:
                self.luzRoja = True
                self.luzVerde = False
                self.luzAmarilla = False

            if self.estado == 1:
                self.luzRoja = False
                self.luzVerde = True
                self.luzAmarilla = False

            if self.estado == 2:
                self.luzRoja = False
                self.luzVerde = False
                self.luzAmarilla = True

            print(self)

            if self.controladora:
                self.controladora.activarPin(0, self.luzRoja)
                self.controladora.activarPin(1, self.luzAmarilla)
                self.controladora.activarPin(2, self.luzVerde)
                self.entrada_00 = self.controladora.X_01

            if self.worker:
                self.worker.activarLuzRoja(self.luzRoja)
                self.worker.activarLuzAmarilla(self.luzAmarilla)
                self.worker.activarLuzVerde(self.luzVerde)
                self.worker.activarCajaAzul(self.entrada_00)

    def establecerWorker(self, worker):
        self.worker = worker

    def establecerControladora(self, controladora):
        self.controladora = controladora

    def __str__(self):
        return "Rojo: " + str(self.luzRoja) + \
            ", Amarillo: " + str(self.luzAmarilla) + \
            ", Verde: " + str(self.luzVerde)


def main():
    miSemaforo = Semaforo()
    # print(miSemaforo)
    # miSemaforo.iniciarSemaforo()
    miSemaforo.run()


if __name__ == "__main__":
    main()
