def reporte_alumno(name, nota1, nota2):
    promedio = (nota1 + nota2) / 2
    return f"Alumno {name}:\n" \
           f"-Primer parcial: {nota1}.\n" \
           f"-Segundo parcial: {nota2}.\n" \
           f"-Promedio: {promedio}."


user_apellido = input("Por favor, ingrese su apellido: ").upper()
user_nota1 = int(input("Ingrese nota del primer parcial: "))
user_nota2 = int(input("Ingrese nota del segundo parcial: "))

print(reporte_alumno(user_apellido, user_nota1, user_nota2))
