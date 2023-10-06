import platform

sistema = platform.system()
plataforma = platform.uname()

if sistema == "Windows":
    print('Estamos en Windows')
elif sistema == 'Linux':
    print('Estamos en Linux')
    if plataforma.node == "raspberrypy":
        print('Es una raspberry')
        import RPi.GPIO as GPIO


class Controladora:
    def __init__(self):
        print('Iniciando la controladora')

        if plataforma.node == "raspberrypy":
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            self.DO_00 = 4
            self.DO_01 = 17
            self.DO_01 = 27
            self.DO_01 = 22

            self.DI_00 = 23

            GPIO.setup(self.DO_00, GPIO.OUT)
            GPIO.setup(self.DO_01, GPIO.OUT)

            GPIO.setup(self.DI_00, GPIO.IN)

            # while True:
            #     GPIO.output(self.DO_00, GPIO.input(self.DI_00))

    def activarPin(self, direccion, valor):
        if plataforma.node == "raspberrypy":

            if direccion == 0:
                GPIO.output(self.DO_00, valor)

            if direccion == 1:
                GPIO.output(self.DO_01, valor)

            if direccion == 2:
                GPIO.output(self.DO_02, valor)

def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
