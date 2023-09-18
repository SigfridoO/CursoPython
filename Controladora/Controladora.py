__author__ = "Sigfrido"
__date__ = "$25-ene-2020 12:43:00$"

import os
import platform
import sys
import threading
import time
from datetime import datetime, timedelta

from blessed import Terminal


term = Terminal()

sistema = platform.system()
plataforma = platform.uname()
version = ""

caracterDirectorio = ""
if sistema == "Windows":
    caracterDirectorio = '\\'
elif sistema == "Linux":
    caracterDirectorio = '/'
    if plataforma.node == "raspberrypi":
        version = plataforma.node
        import RPi.GPIO as GPIO

class Controladora:
    def __init__(self):
        print('Iniciando controladora')



        if version == 'raspberrypi':
            print('Es una raspberry')
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            self.DO_00 = 17
            self.DO_01 = 27

            self.DI_00 = 22

            GPIO.setup(self.DI_00, GPIO.IN)

            GPIO.setup(self.DO_00, GPIO.OUT)
            GPIO.setup(self.DO_01, GPIO.OUT)


            #GPIO.output(self.DO_00, True)
            #self.boton01 = GPIO.input(self.DI_00)
            #print(self.boton01)


            while True:
                GPIO.output(self.DO_00, GPIO.input(self.DI_00))





def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
