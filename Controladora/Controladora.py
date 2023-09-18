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

            self.DI_00 = 18

            self.DI_01 = 27
            self.DI_02 = 22
            self.DI_03 = 10

            self.DO_03 = 9

            GPIO.setup(self.DI_00, GPIO.IN)
            GPIO.setup(self.DI_01, GPIO.IN)
            GPIO.setup(self.DI_02, GPIO.IN)
            GPIO.setup(self.DI_03, GPIO.IN)

            GPIO.setup(self.DO_03, GPIO.OUT)




def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
