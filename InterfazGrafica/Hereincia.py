class Padre:
    def __init__(self):
        print ('Soy padre')

class Madre:
    def __init__(self):
        print('Soy Madre')

class Hijo(Madre, Padre ):
    def __init__(self):
        #super().__init__() # Llama a la superclase
        Madre.__init__(self)
        Padre.__init__(self)
        print('Soy hijo')
def inicio():
    juan = Hijo()


if __name__ == '__main__':
    inicio()