__author__ = "Sigfrido Soria"
__date__ = "14-mar-2023 21:10:00"

import platform
import threading

sistema = platform.system()
plataforma = platform.uname()

if sistema == "Windows":
    print('Estamos en Windows')
elif sistema == 'Linux':
    print('Estamos en Linux')
    if plataforma.node == "raspberrypi":
        print('Es una raspberry')
        import RPi.GPIO as GPIO


class Controladora:
    def __init__(self):
        print('Iniciando la controladora')

def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
