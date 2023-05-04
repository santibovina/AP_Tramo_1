
"""
Realice las funciones solicitadas a continuación.
No cambie los nombres de las funciones.
Ninguna función necesita ingreso por teclado ni
mostrar algo por pantalla por lo cual ninguna lleva
ni la instrucción "input" ni la instrucción "print".

El archivo se debe guardar con el nombre:
    DNIxxxxxxxx.py
Donde DNI va con MAYÚSCULAS y xxxxxxxx debe ser su Nro de DNI.

Al final del archivo hay un espacio para que haga las pruebas
de funcionamiento, una vez finalizadas se debe borrar
lo que allí se escribió.


COLOQUE SUS DATOS
  Apellido y Nombre: Bovina Santiago
  DNI: 33162622

"""


"""
Realice una función que reciba una lista con números enteros y 
RETORNE otra lista con los números de la primera que sean divisibles por 5.
Ejemplo lista=[3,15,12,20,25,42,75,23] RETORNA [15,20,25,75]
"""
def divx5(lista): #No cambiar este encabezado
    lista_2 = []
    for n in lista:
        if n % 5 == 0:
            lista_2.append(n)
    return lista_2


"""
Realice una función que reciba una lista con números enteros y 
RETORNE un número que sea el resultado de sumar todos los números
de las posiciones impares de la lista.
Ejemplo Lista=[7,3,12,23,15,11] RETORNA   34 
Ejemplo Lista=[4,22,10,54,27,12] RETORNA  41 
"""
def sumaposimpares(lista): #No cambiar este encabezado
    suma_impares = sum(lista[::2])
    return suma_impares



"""
Realice una función que reciba dos números distintos como parámetros y 
RETORNE una lista con los cuadrados de todos los números entre ellos dos 
incluidos ambos.
Por ejemplo: recibe  3 y 8 RETORNA [9,16,25,36,49,64]
Por ejemplo: recibe 10 y 6 RETORNA [36,49,64,81,100]

"""
def cuadrados(n1, n2): #No cambiar este encabezado
    lista_cuadrados = []
    if n1 == n2:
        return "Ingrese números distintos por favor."
    elif n2 < n1:
        n1, n2 = n2, n1
    for x in range (n1, n2 + 1):
        num_al_cuadrado = x * x
        lista_cuadrados.append(num_al_cuadrado)
    return lista_cuadrados

#***********************************************************************
#  Espacio para pruebas,  BORRAR las pruebas antes de entregar
#***********************************************************************


#***********************************************************************
# FIN  Espacio para pruebas
#***********************************************************************

