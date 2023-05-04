'''Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
uno, informarle si el mismo es positivo, negativo, o cero.'''


def cero_pos_neg():

    contador = 10
    
    for n in range(10):
    
        print(contador)
        
        user_input = int(input("Ingrese un número por favor: "))
        
        contador -= 1
        
        if user_input == 0:
            print ("El número ingresado es cero")
        elif user_input < 0:
            print ("El número ingresado es negativo")
        else:
            print ("El número ingresado es positivo")
        
        if contador == 0:
            break

cero_pos_neg()
