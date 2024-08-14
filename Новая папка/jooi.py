# a = 12
# b = 12
# res = a - 2 if a > b else b -3
# print(res)

# s = 'total war'
# r = 'upper'
# res = s.upper() if  r == 'upper' else s 
# print(res)


# a = 12
# b = 11


# age = int(input("Enter your age: "))
# message = "Welcome" if age > 18 else "Forbidden"
# print(message)


# age = int(input("Enter your age: "))

# message = ""

# if age < 18:
# 		message = "Forbidden"
# else:
# 		message = "Welcome"

# print(message)	

# def my_function(name, last_name, occupation, age, lol, dyk):
#     print(f'Сотрудник номер 1 по лживости - {name} {last_name} {occupation} {age} {lol} {dyk}')

# info1, info2, info3, info4, info5, info6 = 'Сулик', 'Сулайманович', 'скам-мастер',  '14 лет', 'мастер смотреть списывать', 'а так же мастер духа(драк)' 
# my_function(info1, info2, info3, info4, info5, info6)                  
# my_function(info1, info2, info3, info4, info5, info6)  
# my_function(info1, info2, info3, info4, info5, info6)    
# suslik = input("")



# i = 1
# while i < 6:
# 	print(i)
# 	if i == 3:
# 		print("Конец цикла")
# 		break
# 	i += 1
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     continue
#   i += 1



# class Fruits:
# 	def __init__(self, name, color, weight):
# 		self.name = name
# 		self.color = color
# 		self.weight = weight
# 	def info(self):
# 		print(f"Название-{self.name}, color-{self.color}, weight-{self.weight}")

# pe = Fruits('Яблоко', 'xx', 'xx',)
# pe.info()
# def info(self):
# 		print(f"Название-{self.name}, color-{self.color}, weight-{self.weight}")
# pe = Fruits('Яблоко', 'xx', 'xx',)
# pe.info()
# def info(self):
# 		print(f"Название-{self.name}, color-{self.color}, weight-{self.weight}")
# pe = Fruits('Яблоко', 'xx', 'xx',)
# pe.info()


# # kok = int(input("Введите сколько страниц у вашей книги: "))

# class Book:
# 	def __init__(self, title, author, pages ):
# 		self.title = title
# 		self.author = author
# 		self.pages = pages
# 		self.user_input = int(input("Введите сколько страниц у вашей книги: "))

# 	def drive(self):
# 		print(f"name-{self.title}, avtor-{self.author}, list-{self.pages}")

# 	def start(self):
# 		if self.user_input > 300:
# 			print("Толстая книга")

# 		elif self.user_input < 100:
# 			print("Маленькая книга")

# 		else:
# 			print("Средняя книга")
			
# po = Book('ds', 'ds', 'ew')
# po.drive()






























# class GamePlayer:
#     def init(self, iq, power, height):
#         self.iq = iq
#         self.power = power
#         self.height = height

#     def dannie(self):
#         self.vibor = int(input("\n Выберите варианты IQ: 1-60, 2-80, 3-100, 4-120 "))
#         if self.vibor == 1:
#             print("Ваш выбор 1 - ваш персонаж глуповат")
#         elif self.vibor == 2:
#             print("Ваш выбор 2 - ваш персонаж noob")
#         elif self.vibor == 3:
#             print("Ваш выбор 3 - ваш персонаж norm")
#         elif self.vibor == 4:
#             print("Ваш выбор 4 - ваш персонаж слишком умный добавляем ему дебав 'смертельная болезнь'")
#         else:
#             print("Ты чё ахуэл?")

#         self.vibor1 = int(input(" \n Выберите варианты роста: 1-100, 2-120, 3-160, 4-190 "))
#         if self.vibor1 == 1:
#             print("Ваш выбор 1 - ваш персонаж гном")
#         elif self.vibor1 == 2:
#             print("Ваш выбор 2 - ваш персонаж коротышка")
#         elif self.vibor1 == 3:
#             print("Ваш выбор 3 - ваш персонаж находится в золотой середине")
#         elif self.vibor1 == 4:
#             print("Ваш выбор 4 - шкаф")
#         else:
#             print("Такого варианта нет")

#         self.vibor2 = int(input("\n Выберите варианты силы: 1-10, 2-30, 3-60, 4-90 "))
#         if self.vibor2 == 1:
#             print("Ваш выбор 1 - ваш персонаж слаб")
#         elif self.vibor2 == 2:
#             print("Ваш выбор 2 - ваш персонаж слабоват")
#         elif self.vibor2 == 3:
#             print("Ваш выбор 3 - ваш персонаж находится в золотой середине")
#         elif self.vibor2 == 4:
#             print("Ваш выбор 4 - Майк Тайсон")
#         else:
#             print("Такого варианта нет")

#     def info(self):
#         print(f'Выбор вашего персонажа: IQ - {self.iq}, рост - {self.height}, сила - {self.power}')

#         with open('baza.txt', 'w', encoding="UTF-8") as file:
#             file.write(f'Выбор вашего персонажа: IQ - {self.iq}, рост - {self.height}, сила - {self.power}')
#             print("вы ввели данные в базу данных")
    
# player = GamePlayer(100, 60, 160)
# player.dannie()
# player.info()


















class Car:
    def __init__(self, model, year, color, city):
        self.model = model
        self.year = year
        self.color = color
        self.city = city
        self.baal = True
        self.fuel = 0

    def tanks(self, agoutg):
        if self.fuel + agoutg > 40:
            print(f"Вы не можите залить более 40л")
        else:
            self.fuel += agoutg
            print(f"Бак заполнен на {self.fuel} литров")

    def drive(self, distan):
        xx = distan / 10
        if self.fuel >= xx:
            self.fuel -= xx
        
            print(f"Вы доехали до пункта назначения {self.city}, осталось топлива {xx} ")
        else:
            print("Недостаточно топлива")



class Car2(Car):
    def __init__(self, model, year, color, city):
        super().__init__(model, year, color, city)
        self.city = input("Введите куда хотите поехать: ")    
        self.distan = float(input("Введите сколько к/м нужно проехать до пункта назначения: "))
        self.bak = int(input("Введите на сколько литров хотите заполнить бак (огранечение 40л): "))

        self.fill_tank(self.bak)

    def travel(self):
        self.drive(self.distance)

# Пример использования
my_car = Car2("Toyota", 2020, "Red")
my_car.travel()