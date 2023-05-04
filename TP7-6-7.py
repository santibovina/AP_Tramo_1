'''Cree un script que le solicite al usuario ingresar 10 números, y una vez
ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.
Extienda el script del ejercicio anterior para que también informe el número
mínimo ingresado, y su posición.'''


def informe_numerico():
    lista_usuario = []
    for x in range(1, 10):
        x = int(input("Ingrese un número: "))
        lista_usuario.append(x)

    max_input = max(lista_usuario)
    min_input = min(lista_usuario)
    index_max = lista_usuario.index(max(lista_usuario)) + 1
    index_min = lista_usuario.index(min(lista_usuario)) + 1

    return f"El mayor número introducido es {max_input} y se ingresó en la posición {index_max}, " \
           f"y el menor número introducido es {min_input} y se ingresó en la posición {index_min}."


print(informe_numerico())

