def longitud_nombres(name1, name2):
    if len(name1) > len(name2):
        return True
    else:
        return False


nombre_1 = input("Ingrese el primer nombre: ")
nombre_2 = input("Ingrese el segundo nombre: ")

print(longitud_nombres(nombre_1, nombre_2))
