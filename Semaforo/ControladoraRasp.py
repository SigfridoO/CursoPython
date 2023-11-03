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
        
        # Entradas Digitales
        self.X_00 = False
        self.X_01 = False
        self.X_02 = False
        self.X_03 = False
        self.X_04 = False
        self.X_05 = False
        self.X_06 = False
        self.X_07 = False


        # Salidas digitales
        self.Y_00 = False
        self.Y_01 = False
        self.Y_02 = False
        self.Y_03 = False

        self.Y_04 = False
        self.Y_05 = False
        self.Y_06 = False
        self.Y_07 = False

        self.Y_08 = False
        self.Y_09 = False
        self.Y_10 = False
        self.Y_11 = False

        self.Y_12 = False
        self.Y_13 = False
        self.Y_14 = False
        self.Y_15 = False




        self.instruccionLeida=""
        self.instruccionEscrita=""

        self.estado = False

        if plataforma.node == "raspberrypi":
            self.configurarSenales()

            tarea1 = threading.Thread(target=self.loop)
            tarea1.start()
            # while True:
            #     GPIO.output(self.DO_00, GPIO.input(self.DI_00))

    def activarPin(self, direccion, valor):
        if plataforma.node == "raspberrypi":

            if direccion == 0:
                GPIO.output(self.DO_00, valor)

            if direccion == 1:
                GPIO.output(self.DO_01, valor)

            if direccion == 2:
                GPIO.output(self.DO_02, valor)

            if direccion == 3:
                GPIO.output(self.DO_03, valor)


    def configurarSenales(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)




        # --------------  Entradas
        #Botones 

        self.DI_00 = 18
        self.DI_01 = 23
        self.D2_02 = 24
        self.D3_03 = 25

        #Sensores

        self.DI_04 = 8
        self.DI_05 = 7
        self.DI_06 = 12
        self.DI_07 = 16


        # --------------  Salidas
        #Lamparas
        self.DO_00 = 4
        self.DO_01 = 17
        self.DO_02 = 27
        self.DO_03 = 22

        # Motor de Corriente directa
        self.DI_05 = 10
        self.DI_06 = 9

        # Motor de CD con PWM
        self.DI_07 = 11
        self.DI_08 = 5

        # Motor a pasos
        self.DO_09 = 6
        self.DO_10 = 13
        self.DO_11 = 19
        self.DO_12 = 26

        # Motor Trifasico
        self.DO_13 = 20
        self.DO_14 = 21

        GPIO.setup(self.DI_00, GPIO.OUT)
        GPIO.setup(self.DI_01, GPIO.OUT)
        GPIO.setup(self.DI_02, GPIO.OUT)
        GPIO.setup(self.DI_03, GPIO.OUT)
        
        GPIO.setup(self.DI_04, GPIO.OUT)
        GPIO.setup(self.DI_05, GPIO.OUT)
        GPIO.setup(self.DI_06, GPIO.OUT)
        GPIO.setup(self.DI_07, GPIO.OUT)

        GPIO.setup(self.DO_00, GPIO.OUT)
        GPIO.setup(self.DO_01, GPIO.OUT)
        GPIO.setup(self.DO_02, GPIO.OUT)
        GPIO.setup(self.DO_03, GPIO.OUT)

        GPIO.setup(self.DO_04, GPIO.OUT)
        GPIO.setup(self.DO_05, GPIO.OUT)
        GPIO.setup(self.DO_06, GPIO.OUT)
        GPIO.setup(self.DO_07, GPIO.OUT)

        GPIO.setup(self.DO_08, GPIO.OUT)
        GPIO.setup(self.DO_09, GPIO.OUT)
        GPIO.setup(self.DO_10, GPIO.OUT)
        GPIO.setup(self.DO_11, GPIO.OUT)


        GPIO.setup(self.DI_12, GPIO.IN)
        GPIO.setup(self.DI_13, GPIO.IN)
        GPIO.setup(self.DI_14, GPIO.IN)
        # GPIO.setup(self.DI_15, GPIO.IN)


        # configurar puerto serie

    def loop(self):
        self.estado = True
        while self.estado:
            

            self.leerYEscribirPines()
            #recibirDatos()

            


    def leerYEscribirPines(self):
        # Lo que tenga en los pines de entrada me lo manda a las X
        self.X_00 = GPIO.input(self.DI_00)
        self.X_01 = GPIO.input(self.DI_01)

        # Lo que tenga en las Y me lo manda a los pines

        GPIO.output(self.DO_00, self.Y_00)

        GPIO.output(self.DO_01, self.Y_01)

        GPIO.output(self.DO_02, self.Y_01)

    def recibirDatos():
        # self.instruccionLeida = serial.read(50)
        pass

    def transmitirDatos(instruccion):
        serial.write(50)

def main():
    controladora = Controladora()


if __name__ == "__main__":
    main()
