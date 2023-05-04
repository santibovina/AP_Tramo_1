dict_semana = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miércoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sábado"
}

for k, v in dict_semana.items():
    print(f"{k}: {v}")

print()


def dia_de_la_semana(num):
    try:
        return f"El número ingresado corresponde al día {dict_semana[num]}."
    except:
        return "Número no válido"


user_input = int(input("Ingrese el número de día: "))

print(dia_de_la_semana(user_input))
