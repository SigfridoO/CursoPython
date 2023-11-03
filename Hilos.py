from Controladora.Temporizador import Temporizador
import threading

class Control:
    def __init__(self, nombre):

        self.TON_01 = Temporizador("TON_01", 1)
        self.nombre = nombre

        tarea = threading.Thread(target=self.run)
        tarea.start()

    def run(self):
        contador = 0
        banderaDeFuncionamiento = True

        while banderaDeFuncionamiento:
            self.TON_01.entrada = not self.TON_01.salida
            self.TON_01.actualizar()

            if self.TON_01.salida:
                contador += 1
                print(self.nombre, ' contador: ', contador)

            if contador == 10:
                banderaDeFuncionamiento=False





def main():
    print('Iniciando main')
    programa1 = Control("Programa 1")

    programa2 = Control("Programa 2")

    print('finalizando main')

if __name__ == "__main__":
    main()