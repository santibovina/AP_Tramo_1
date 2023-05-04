def base_por_exponente(base, exponente):
    result = base ** exponente
    return result


user_choice_base = int(input("Ingrese un número: "))
user_choice_exponente = int(input("Ingrese otro número: "))

print(base_por_exponente(user_choice_base, user_choice_exponente))
