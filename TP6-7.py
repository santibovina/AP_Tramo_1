def lados_triángulo(a, b, c):
    if a == b == c:
        return "El triángulo es equilátero."
    elif a != b != c:
        return "El triángulo es escaleno."
    else:
        return "El triángulo es isósceles."


lado_1 = int(input("Ingrese el primer lado: "))
lado_2 = int(input("Ingrese el segundo lado: "))
lado_3 = int(input("Ingrese el tercer lado: "))

print(lados_triángulo(lado_1, lado_2, lado_3))
