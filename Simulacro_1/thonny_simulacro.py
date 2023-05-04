def potencia(a,b): #No cambiar este encabezado
    if a == b:
        return "Los números deben ser distintos."
    elif a > b:
        return a ** b
    else:
        return b ** a
        
print(potencia(9.5,9))