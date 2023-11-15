from Actuadores.Motor import Motor

class Impresora3D:
    def __init__(self):
        # actuadres
        motorX = Motor()
        motorY = Motor()
        motorZ = Motor()

        # Sensores

        # Interfaz Grafica



def inicio():
    print('Iniciando la impresora')
    miImpresora = Impresora3D()

    archivo = ArchivoAImpimir("C:/")

    miImpresora.imprimir(archivo)
    miImpresora.iniciar()


if __name__ == '__main__':
    inicio()