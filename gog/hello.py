#функция имя функции переменная
# def is_even(number):
#если number делим на 2 а если потом оно будет равен 0 то True
	# num = 
	# 	return True
	
	# else:
	# 	return False
	
	# print(is_even(4))
	# print(is_even(7))
	# try:
	# 	def say(name):
	# 					print(f"хз {name}")
	# 	say()
	# except SyntaxError as e:
	# 	print(e, 'super')
		

# try:
#     def say(name):
#         print(f"хз {name}")
    
#     say()  # This will raise a TypeError because `name` is missing.
# except TypeError as e:
#     print(e, 'super')
# def say(name):
#  	print(f"hi bro {name}")
	 
# my_list = ["xxxd", "xxxc"]
# say(my_list)

# def my_func():
# 	return 2 + 2

# print(my_func())
# print("hello bro")

# def say(name, age, heinth):
#  	print(f"имя-{name}", f"возвраст-{age}",  f"рост-{heinth}")

# # def say(name, age, height):
# #     print(f"имя-{name}", f"возраст-{age}", f"рост-{height}")
# # say(name=ZeroDivisionError, age=180, heinth=13)

# gg = ["xx", 13, 180]

# say(*"Symon", 13, *gg)
#def  is_even(number):

# def is_even(number):
	
# value = float(int(input("Введите число: ")))
# # print(isinstance(value, int))
# # print("Первое float второе int (значения)")
# if value == 123:
# 	print(value.is_integer())
# else: 
# 	value == 123.0
# print(isinstance(value, int))

# # #value = float(input("Введите число: "))

# print(value.is_integer())
# # def is_integer(x):
#     if isinstance(x, float):
#         return x.is_integer()
#     if isinstance(x, int):
#         return True
#     raise TypeError()

# def isPrime(n):
#     num = int(input("Введите число: "))
#     '''Check if integer n is a prime'''
#     n = abs(int(n))
#     if n < 2:
#         return False
#     if n == 2: 
#         return True    
#     if not n & 1: 
#         return False
#     for x in range(3, n):
#         if n % x == 0:
#             return False
#     return True



# def add(a, b):
# 	return a + b

# result = add(3, 2)
# print(result)



# def sing_up(name, age, gender):
# 	print(f"имя-{name}, возвраст-{age}, пол-{gender}")
# 	sing_up(gender='Мужской', name='имя', age='возврст')





num = int(input("Введите первое число: "))
num_1 = int(input("Введите второе число: "))

if num > num_1:
    print(f"{num} больше, чем {num_1}")
elif num < num_1:
    print(f"{num} меньше, чем {num_1}")
else:
    print(f"{num} равно {num_1}")
