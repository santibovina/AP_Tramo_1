def condición_alumno(nota1, nota2):

    promedio = (nota1 + nota2) / 2

    if nota1 < 4 or nota2 < 4:
        return "Su condición es libre. Deberá rendir un final extendido."
    else:
        if promedio >= 8:
            return f"El promedio es {promedio}. Su condición es promovido. " \
                   f"Buen trabajo!"
        else:
            return f"El promedio es {promedio}. Su condición es regular. " \
                   f"Deberá rendir el examen final."


parcial_1 = int(input("Ingrese la nota del primer parcial: "))
parcial_2 = int(input("Ingrese la nota del segundo parcial: "))

print(condición_alumno(parcial_1, parcial_2))
