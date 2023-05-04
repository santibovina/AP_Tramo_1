def área_rectángulo(base, altura):
    area = base * altura
    return area


user_base = int(input("Ingrese la base del rectángulo: "))
user_altura = int(input("Ingrese la altura del rectángulo: "))

print(área_rectángulo(user_base, user_altura))
