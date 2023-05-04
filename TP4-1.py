def saludo(name):
    long_name = len(name)
    return f"Hola, {name}, tu nombre tiene {long_name} letras."


user_name = input("Por favor, ingresá tu nombre: ")

print(saludo(user_name))
