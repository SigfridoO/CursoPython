from Funciones import nuevoTema



# -----------------  variables
nuevoTema('variables')

print('hola mundo')
a = 5
print("a:", a)

b = 4.342
print('b:', b)

print("a, b:", a, b)

opcion = True
print('opcion:', opcion)


# -----------------  if-else
nuevoTema('instrucciones de control (if-else)')
c = 2

if c > 5:
    print('c es mayor a 5')
    # ESTE BLOQUE DE CÓDIGO NUNCA SE EJECUTA (PARA DEMOSTRAR QUE PYTHON ES UN LENGUAJE INTERPRETADO)
    kjsfdhflkjsdfhkljdhsdkjlfhsdkflhklhyetrtrey34
else:
    print('c NO es mayor a 5')


# -----------------  listas
nuevoTema('listas')
frutas = ['piñas', 'peras', 'manzanas', 'platanos']
print('frutas', frutas)

varios = ['zapatos', 3, 78.45, True, frutas]
print('varios: ', varios)

print('\n')
alumnos = ['Oswaldo', 'Carlos', 'Carolina', 'Johana', 'Karla', 'Alan', 'Alejandra', 'Eduardo', 'Luis']
print('alumnos', alumnos)

print('alumnos[4]: ', alumnos[4])       # Selecciona el objeto con índice 4
print('alumnos[1:3]:', alumnos[1:3])    # Selecciona el objeto desde el 1 hasta el 2
print('alumnos[:]:', alumnos[:])        # Dame todos los alumnos
print('alumnos[-1]:', alumnos[-1])      # Dame el último elemento de la lista
print('alumnos[-2]:', alumnos[-2])      # Dame el penultimo elemento de la lista
print('alumnos[1:8:2]', alumnos[1:8:2]) # Dame los elementos del 1 al 7 pero con un salto del 2

# -----------------  for
nuevoTema('Instrucciones de control - for')
for fruta in frutas:
    print(fruta)




