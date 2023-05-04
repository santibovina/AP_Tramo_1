def promedio(num1, num2):
    result = (num1 + num2) / 2
    return f"El promedio del alumno es {result}."


nota_1 = int(input("Ingrese la nota del primer parcial: "))
nota_2 = int(input("Ingrese la nota del segundo parcial: "))

print(promedio(nota_1, nota_2))
