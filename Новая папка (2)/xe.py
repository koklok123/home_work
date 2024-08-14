# num = float(input("Введите первое число: "))
# num_1 = float(input("Введите второе число: "))

# if num > num_1:
#     print(f"{num} больше, чем {num_1}")
# elif num < num_1:
#     print(f"{num} меньше, чем {num_1}")
# else:
#     print(f"{num} равно {num_1}")




# if name == user_name and password == user_password:
# 	print("Доступ разрешен:")
# elif name != user_name:
# 	print("Не верный логин:")
# elif  password != user_password:
# 	print("Не верный пароль:")
# else:
# 	print("Неизвестное действие")


name = 12
password = 12

user_name = input("Введите логин: ")
user_password = input("Введите пароль: ")



if name == user_name and password == user_password:
    print("Доступ разрешен")
elif name != user_name:
    print("Неверное имя пользователя")
elif password != user_password:
    print("Неверный пароль")
else:
    print("Неизвестное действие")
