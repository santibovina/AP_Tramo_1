def intercambio(num1, num2):
    return f"Los números intercambiados son {num1} y {num2}."


user_num_1 = int(input("Ingrese un número: "))
user_num_2 = int(input("Ingrese un número: "))

user_num_1, user_num_2 = user_num_2, user_num_1

print(intercambio(user_num_1, user_num_2))
