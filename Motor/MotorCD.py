

class MotorCD:
    def __init__(self, *args, **kwargs):


        # Número de pin de las salidas del puente H
        self.pinA = 1
        self.pinB = 2

        self.velocidad = 0
        self.sentidoDeGiro = 0


        pass

    def configurar(self, opcion, *args, **kwargs):
        if args:
            print(args)

        if kwargs:
            for key, value in kwargs.items():
                print (key, value)



    def prender(self):
        pass

    def apagar(self):
        pass

    def girarDerecha(self):
        pass

    def girarIzquierda(self):
        pass


    def __str__(self):
        return ""

def main():
    motor =   MotorCD()
    motor.configurar(3, 4, pin=2, animal = 'gato')

    print ('finalizando main')

if __name__ == "__main__":
    main()