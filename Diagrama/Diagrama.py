import threading

from Controladora.Temporizador import Temporizador

class Secuencia:

    def __init__(self):

        self.entrada_00 = True
        self.salida_00 = False

        self.estado = 0
        self.TON_0 = Temporizador("TON_0", 3)

    def run(self):
        tarea1 = threading.Thread(target=self.iniciar)
        tarea1.start()

    def iniciar(self):

        while True:
            self.TON_0.entrada = not self.TON_0.salida
            self.TON_0.actualizar()

            if self.TON_0.salida:

                aux = self.estado
                if aux == 0:
                    if self.entrada_00:
                        self.estado = 1

                if aux == 1:
                    if self.entrada_00:
                        self.estado = 3
                    else:
                        self.estado = 2

                if aux == 2:
                    if self.entrada_00:
                        self.estado = 0
                    else:
                        self.estado = 3

                if aux == 3:
                    if self.entrada_00:
                        self.estado = 0


                print(self)


    def __str__(self):
        return "Variables: " + str(1 if self.entrada_00 else 0) + \
            " " + str(1 if self.salida_00 else 0) + \
            ", ESTADO: " + str(1 if self.estado else 0)


def main():
    secuencia = Secuencia()
    secuencia.run()

if __name__ == "__main__":
    main()

