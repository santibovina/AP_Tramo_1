def perímetro_rectángulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro


user_base = int(input("Ingrese la base del rectángulo: "))
user_altura = int(input("Ingrese la altura del rectángulo: "))

print(perímetro_rectángulo(user_base, user_altura))
