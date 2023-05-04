def mayor_que_diez(num):
    if num > 10:
        print(f"Tu número {num} es mayor que 10!")
    elif num <= 10:
        print(f"El número {num} es menor o igual que 10!")
        print("Saludos!")


user_input = int(input("Ingresá un número: "))

mayor_que_diez(user_input)
