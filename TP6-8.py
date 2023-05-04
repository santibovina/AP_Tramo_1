def división(a, b):
    if b == 0:
        return 'No se puede dividir por cero!'
    else:
        return round((a / b), 2)


num1 = float(input("Ingrese el numerador: "))
num2 = float(input("Ingrese el denominador: "))

print(división(num1, num2))
