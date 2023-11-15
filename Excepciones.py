
def main():

    print('Antes de iniciar una excepcion, intentando dividir dos números')
    try:
        print ("TRY:", 4/0)
    except ZeroDivisionError as error:
        print ('EXCEPT: El denominador es cero por favor intenta con un diferente de cero')
    else:
        print('ELSE: Codigo que se ejecuta si no hay ningun error')
    finally:
        print ('FINALLY: Codigo que se ejecuta siempre haya o no haya errores')
    print('después de iniciar la excepción')

if __name__=="__main__":
    main()