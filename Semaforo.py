from Controladora.Temporizador import Temporizador


class Semaforo:

    def __init__(self):

        self.luzRoja = False
        self.luzVerde = False
        self.luzAmarilla = False

        self.estado = 0
        self.TON_0 = Temporizador("TON_0", 4)
        self.TON_1 = Temporizador("TON_1", 6)
        self.TON_2 = Temporizador("TON_2", 2)

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

    def __str__(self):
        return "Rojo: " + str(self.luzRoja) + \
            ", Amarillo: " + str(self.luzAmarilla) + \
            ", Verde: " + str(self.luzVerde)


def main():
    miSemaforo = Semaforo()
    print(miSemaforo)
    miSemaforo.iniciarSemaforo()


if __name__ == "__main__":
    main()
