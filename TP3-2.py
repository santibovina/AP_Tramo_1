def mi_nombre(name, long):
    return f"El nombre {name} tiene {long} letras."


nombre = input("Cómo es tu nombre? ")
longitud = len(nombre)


print(mi_nombre(nombre, longitud))
