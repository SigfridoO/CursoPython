__author__ = "Sigfrido"
__date__ = "$25-ene-2020 12:43:00$"

import os
import platform

from blessed import Terminal

term = Terminal()

sistema = platform.system()
plataforma = platform.uname()

if sistema == "Windows":
    print('Estamos en Windows')
elif sistema == "Linux":
    print('Estamos en Linux')
    if plataforma.node == "raspberrypi":
        print('Es una raspberry')
        import RPi.GPIO as GPIO


class Controladora:
    def __init__(self):
        print('Iniciando controladora')

        if plataforma.node == 'raspberrypi':

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            self.DO_00 = 17
            self.DO_01 = 27

            self.DI_00 = 22

            GPIO.setup(self.DI_00, GPIO.IN)

            GPIO.setup(self.DO_00, GPIO.OUT)
            GPIO.setup(self.DO_01, GPIO.OUT)

            # GPIO.output(self.DO_00, True)
            # self.boton01 = GPIO.input(self.DI_00)
            # print(self.boton01)

            while True:
                GPIO.output(self.DO_00, GPIO.input(self.DI_00))


def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
