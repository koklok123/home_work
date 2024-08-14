# class Car: # шаблон или чертеж
#     "Атрибут класса"
#     # marka = 'mercedes'
#     # model = 'cls'
#     # color = 'black'
#     def __init__(self, marka, model, color): # __init__ - конструктор
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model 
#         self.color = color
#         self.bak = 0
#         self.is_start = False
#         self.gorod = False
        
#     def info(self):
#         print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена')
#         elif self.bak < 0:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 
#         elif self.bak > 0:
#             self.gorod = True
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена, Едем в {self.gorod}')
#         elif self.bak < 0:
#             self.gorod = False
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива не едем в город') 


# toyota = Car('Toyota', 'camry', 'white')
# # toyota.info()
# toyota.start()







# class Car: # шаблон или чертеж
#     "Атрибут класса"
#     # marka = 'mercedes'
#     # model = 'cls'
#     # color = 'black'
#     def __init__(self, marka, model, color): # __init__ - конструктор
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model 
#         self.color = color
#         self.bak = 0
#         self.is_start = False
        
#     def info(self):
#         print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена')
#         else:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена, Едет в {city}')
            
# toyota = Car('Toyota', 'camry', 'white')
# toyota.info()
# toyota.start()
# class Car: # шаблон или чертеж
#     "Атрибут класса"
#     # marka = 'mercedes'
#     # model = 'cls'
#     # color = 'black'
#     def __init__(self, marka, model, color): # __init__ - конструктор
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model 
#         self.color = color
#         self.bak = 0
#         self.is_start = False
        
#     def info(self):
#         print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена')
#         else:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 
        
        
# toyota = Car('Toyota', 'camry', 'white')
# toyota.info()
# toyota.start()

# class Book:
#      def __init__(gog, avtor, book_name, year):
#          gog.avtor = avtor
#          gog.book_name = book_name
#          gog.year = year

#      def info(gog):
#         print(f'Автор-{gog.avtor}, Название книги-{gog.book_name}, Какого года книга-{gog.year}')
        
# hok = Book('Дель Кастильо, Кейт', 'Книга жизни', '2014')
# hok.info


# class Book:
#     def __init__(self, avtor, book_name, year):
#         self.avtor = avtor
#         self.book_name = book_name
#         self.year = year

#     def info(self):
#         print(f'Автор-{self.avtor}, Название книги-{self.book_name}, Какого года книга-{self.year}')
        
# hok = Book('Дель Кастильо, Кейт', 'Книга жизни', '2014')
# hok.info()




# """Создайте класс Car c атрибутами - (model, year, color)
# Создайте метод drive с входящим параметром city(город) который будет выводить текст (Машина - модель вашей машины  едет в  - ваш город)

# Доп. Задание:
# Улучшите класс Car:
# Добавьте атрибут fuel со значением 0
# Добавьте метод refuel который будет пополнять бак и  поставьте ограничение - (за раз можно пополнить  только на 40 литров) 
# Измените метод drive :
#  Теперь он должен запрашивать не только город но и  расстояние до этого города, так же учитывайте что  машина  расходует 1л / 10км. Если у машины не хватит  бензина доехать, то должна появится надпись которая  будет предупреждать сколько км может проехать  машина"""










# class Car:
	
# 	def __init__(self, model, year, color, city):
		
# 		self.model = model
# 		self.year = year
# 		self.color = color
# 		self.city = city
# 		self.baal = True

# 	def drive(self):
# 		if self.baal == True:
#             		print(f"модель-{self.model}, лет-{self.year}, Цвет-{self.color}, В какой город едем-{self.city}")
# 		elif self.baal == False:
# 			print(f"модель-{self.model}, лет-{self.year}, Цвет-{self.color}, К намшему величайшему сожеление поездку в Амстерда отменяем")
				
			
# pop = Car('тесла', '13', 'белая', 'В АМСТЕРДАМ НАХУЙ')
# pop.drive()



# class Car:
#     def __init__(self, model, year, color, city):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.city = city
#         self.baal = True

#     def drive(self):
#         if self.baal:
#             print(f"Модель: {self.model}, Год: {self.year}, Цвет: {self.color}, Город: {self.city}")
#         else:
#             print(f"Поездка в Амстердам отменяется.")

# pop = Car('Tesla', '2013', 'белая', 'Амстердам')
# pop.drive()



# """Доп. Задание:
# Улучшите класс Car:
# Добавьте атрибут fuel со значением 0
# Добавьте метод refuel который будет пополнять бак и  поставьте ограничение - (за раз можно пополнить  только на 40 литров) 
# Измените метод drive :
#  Теперь он должен запрашивать не только город но и  расстояние до этого города, так же учитывайте что  машина  расходует 1л / 10км. Если у машины не хватит  бензина доехать, то должна появится надпись которая  будет предупреждать сколько км может проехать  машина"""


# class Car:
#     def __init__(self, model, year, color, city):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.city = city
#         self.baal = True
#         self.fuel = 0

#     def tanks(self, agoutg):
#         if self.fuel + agoutg > 40:
#             print(f"Вы не можите залить более 40л")
#         else:
#             self.fuel += agoutg
#             print(f"Бак заполнен на {self.fuel} литров")

#     def drive(self, distan):
#         xx = distan / 10
#         if self.fuel >= xx:
#             self.fuel -= xx
        
#             print(f"Вы доехали до пункта назначения {self.city}, осталось топлива {xx} ")
#         else:
#             print("Недостаточно топлива")



# class Car2(Car):
#     def __init__(self, model, year, color, city):
#         super().__init__(model, year, color, city)
#         self.city = input("Введите куда хотите поехать: ")    
#         self.distan = float(input("Введите сколько к/м нужно проехать до пункта назначения: "))
#         self.bak = int(input("Введите на сколько литров хотите заполнить бак (огранечение 40л): "))

#         self.fill_tank(self.bak)

#     def travel(self):
#         self.drive(self.distance)

# # Пример использования
# my_car = Car2("Toyota", 2020, "Red")
# my_car.travel()











# num_1 = 1
# num_2 = 2


# class Cat:
	
# 	def __init__(self, name, prefectens):
# 		self.name - name 
# 		self.prefectent = prefectens
		
#     def info(self):
# 	    print(f"Я кот. Меня зовут {self.name}, Мне {self.prefectens}")
		
#     def make_soud(self):
#         print("Мяу")
		
# class Dog:
# 	def __init__(self, name, prefectens):
# 		self.name - name 
# 		self.prefectent = prefectens
		
# 	def info(self):
# 	    print(f"Я собака. Меня зовут {self.name}, Мне {self.prefectens}")
		
#     def make_soud(self):
#         print("Гаф")
		
# cat = Cat('Ноунейм', 'Док')
# dog = Dog('Ыыыы', 'ГАф')

# for animal in (cat, dog):
# 	animal.make_soud()
# 	animal.info()
# 	animal.make_soud()

# class Payment:
# 	def pay(self, amount):
# 		pass

# class Creditcard(Payment):
# 	def pay(self, amount):
#             return f'Сумма {amount}, сумма оплачиваеться по кредитной карте'
	
# class PayPal(Payment):
# 	def pay(self, amount):
#             return f'Сумма {amount}, сумма оплачиваеться по пейпалу'
	
# class Transver(Payment):
# 	def pay(self, amount):
#             return f'Сумма оплачиваеться {amount}, сумма оплачиваеться по банковскому переводу'
	
# peymant = [Creditcard(), PayPal(), Transver()]

# for play in peymant:
# 	print(play.pay(100))
	

    

"""
1. **Базовый класс `User`:**
    - Свойства:
        - `username` (имя пользователя)
        - `email` (электронная почта)
        - `password` (пароль)
    - Методы:
        - `display_info()`: выводит информацию о пользователе (кроме пароля).

2. **Класс-наследник `Admin` (пользователь с административными правами):**
    - Свойства:
        - `admin_level` (уровень доступа)
    - Методы:
        - Переопределить метод `display_info()`, чтобы также выводить `admin_level`.

3. **Класс-наследник `Guest` (гость):**
    - Свойства:
        - `expiry_date` (дата истечения действия гостевого доступа)
    - Методы:
        - Переопределить метод `display_info()`, чтобы также выводить `expiry_date`.

4. **Класс `UserManager`:**
    - Свойства:
        - `users` (список пользователей)
    - Методы:
        - `add_user(user)`: добавляет пользователя в список.
        - `remove_user(username)`: удаляет пользователя по имени.
        - `display_all_users()`: выводит информацию о всех пользователях, используя полиморфизм для вызова метода `display_info()`.

"""

# class User:

# 	def __init__(self, username, email, password):
# 		self.username = username
# 		self.email = email
# 		self.password = password

# 	def display_info(self):
# 		print(f"NickName-{self.username}, Emeil-{self.email}")
# class Admin(User):
# 	def __init__(self, username, email, password, admin_level):
# 		super().__init__(username, email, password)
# 		self.admin_level = admin_level

# 	def display_info(self):
# 		print(f"NickName-{self.username}, Emeil-{self.email}, Права администратора-{self.admin_level}")

# class Guest(Admin):
# 	def __init__(self, username, email, password, admin_level, expiry_date):
# 		super().__init__(username, email, password, admin_level)
# 		self.expiry_date = expiry_date
	
# 	def display_info(self):
# 		print(f"NickName-{self.username}, Emeil-{self.email}, Права администратора-{self.admin_level}, Дата источения всего срока-{self.expiry_date}")

# class UserManager(Guest):
# 	def __init__(self, username, email, password, admin_level, expiry_date, users):
# 		super().__init__(username, email, password, admin_level, expiry_date)
# 		self.users = users

# 	def add_user(self):
# 		self.users = [f"NickName-{self.username}, Emeil-{self.email}, Права администратора-{self.admin_level}, Дата источения всего срока-{self.expiry_date}"]
# 		self.users.append(self.users)
# 		# self.users.remove(f"NickName-{self.username}")
		

# 	def remove_user(self, username):
# 		for self.users in self.users:
# 			if f"NickName-{username}" in self.users:
# 				self.users.remove(self.users)
# 				break

# 	def display_all_users(self):
# 		for self.users in self.users:
#             print(self.users)


# kok = UserManager('None', 'None', 'None', 'None', 'None', 'none')
# kok.add_user()



# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def display_info(self):
#         print(f"NickName-{self.username}, Email-{self.email}")

# class Admin(User):
#     def __init__(self, username, email, password, admin_level):
#         super().__init__(username, email, password)
#         self.admin_level = admin_level

#     def display_info(self):
#         print(f"NickName-{self.username}, Email-{self.email}, Права администратора-{self.admin_level}")

# class Guest(Admin):
#     def __init__(self, username, email, password, admin_level, expiry_date):
#         super().__init__(username, email, password, admin_level)
#         self.expiry_date = expiry_date
    
#     def display_info(self):
#         print(f"NickName-{self.username}, Email-{self.email}, Права администратора-{self.admin_level}, Дата истечения всего срока-{self.expiry_date}")

# class UserManager(Guest):
#     def __init__(self, username, email, password, admin_level, expiry_date, users):
#         super().__init__(username, email, password, admin_level, expiry_date)
#         self.users = users

#     def add_user(self):
#         user_info = f"NickName-{self.username}, Email-{self.email}, Права администратора-{self.admin_level}, Дата истечения всего срока-{self.expiry_date}"
#         self.users.append(user_info)

#     def remove_user(self, username):
#         for user in self.users:
#             if f"NickName-{username}" in user:
#                 self.users.remove(user)
#                 break

#     def display_all_users(self):
#         for user in self.users:
#             print(user)


# users_list = []
# kok = UserManager('none', 'none', 'none', 'none', 'none', users_list)
# kok.add_user()
# kok.display_all_users()


# class Vehicle:
	
#     def move(self):
#         self.movement = True
#         self.full_bak = None
    
#     def fuel(self):
#         return self.full_bak

# class Car(Vehicle):
#     def move(self):
#         self.movement = True 
#         if self.movement == True:
#             print(f"Машина едет по дороге")
#         elif self.movement == False:
#             print("Машина не едет")
#         else:
#             print("Неизвестное действие")

#     def fuel(self):
#         self.full_bak = "Бензин, дизель, электричество, сжатый природный газ (СПГ), сжиженный нефтяной газ (СНГ), водород, этанол, биодизель, пропан."
#         return self.full_bak
    
# class Boat(Vehicle):
#     def move(self):
#         self.movement = True 
#         if self.movement == True:
#             print(f"Лодка плывёт по морю")
#         elif self.movement == False:
#             print("Лодка не плывёт")
#         else:
#             print("Неизвестное действие")

#     def fuel(self):
#         self.full_bak = "Физическая сила/Электро мотор"
#         return self.full_bak 
    
# class Bicycle(Vehicle):
#     def move(self):
#         self.movement = True 
#         if self.movement == True:
#             print(f"Велосипед едет по дороге")
#         elif self.movement == False:
#             print("Велосипед не едет")
#         else:
#             print("Неизвестное действие")

#     def fuel(self):
#         self.full_bak = "Физическая сила/Электроэнергия"
#         return self.full_bak
    
# class Airplane(Vehicle):
#     def move(self):
#         self.movement = True 
#         if self.movement == True:
#             print(f"Самалёт летит по маршруту")
#         elif self.movement == False:
#             print("Самалёт не летит")
#         else:
#             print("Неизвестное действие")

#     def fuel(self):
#         self.full_bak = "ДВС"
#         return self.full_bak 
    
# dz_car = Car()
# velik = Bicycle()
# camal = Airplane()
# lodka = Boat()


# for animal in (dz_car, velik, camal, lodka):
#     animal.move()
#     print(f"Тип топлива: {animal.fuel()}")
    


# Из бюблятеки tkinter импортировать *-Всё  и с рандомом так-же
# from tkinter import *
# from random import *

# # Переменная ну и содаем окно
# root = Tk()
# #тут размер окна 
# root.geometry('300x400')
# # это строка кода вопше не обезательна в принципе она просто запрещает изминять разрешение приложения ну экрана короче
# root.resizable(width = False, height = False)
# #title переобразует первое слово в заглавное
# root.title('камень, ножницы, бумага')
# # Это делает фон зеленым
# root['bg'] = 'Green'


# def kamen():
# 	knb = ['Камень','Ножница','Бумага']
# 	camputer = choice(knb)
# 	text_2['text']   = f'ГЕНИЙ ИИ: {camputer}'
	
# 	if camputer ==  knb[0]:
# 		text_3['text'] = 'Выиграли: Ничья'
# 	if camputer ==  knb[1]:
# 		text_3['text'] = 'Выиграли: Вы. На самом деле вам просто повезло ТРАТЬТЕ ЖЕ СВОЮ УДАЧУ'
# 	if camputer ==  knb[2]:
# 		text_3['text'] = 'Выиграл: ГЕНИЙ ИИ. Вы же, не кто по сравнению с ии-)'
		
# def nojnic():
# 	noj = ['Камень','Ножница','Бумага']
# 	camputer = choice(noj)
# 	text_2['text']   = f'ГЕНИЙ ИИ: {camputer}'
	
# 	if camputer ==  noj[0]:
# 		text_3['text'] = 'Выиграли: Ничья'
# 	if camputer ==  noj[1]:
# 		text_3['text'] = 'Выиграли: Вы. На самом деле вам просто повезло ТРАТЬТЕ ЖЕ СВОЮ УДАЧУ'
# 	if camputer ==  noj[2]:
# 		text_3['text'] = 'Выиграл: ГЕНИЙ ИИ. Вы же, не кто по сравнению с ии-)'
		

# def bym():
# 	bymaga = ['Камень','Ножница','Бумага']
# 	camputer = choice(bymaga)
# 	text_2['text']   = f'ГЕНИЙ ИИ: {camputer}'
	
# 	if camputer ==  bymaga[0]:
# 		text_3['text'] = 'Выиграли: Ничья'
# 	if camputer ==  bymaga[1]:
# 		text_3['text'] = 'Выиграли: Вы. На самом деле вам просто повезло ТРАТЬТЕ ЖЕ СВОЮ УДАЧУ'
# 	if camputer ==  bymaga[2]:
# 		text_3['text'] = 'Выиграл: ГЕНИЙ ИИ. Вы же, не кто по сравнению с ии-)'

# # mainloop это чтото типо while True бесконечность короче делает так чтобы оно работало вечно я не знаю как но без него окошко не появиться
# root.mainloop()
# #label- это окошко или пространство где можно что-то написать и там можно поместить что-то ну там фото или ищё что-то
# text_2 = Label (text = 'ГЕНИЙ ИИ'
# 			   bg = 'black'
# 			   fg = 'Green'
# 			   font = 15)

# text_2.place(x = 150, y = 40)

# text_3 = Label(text = 'Выигравший эту жизнь'
# 			   bg = 'black'
# 			   fg = 'Green'
# 			   font = 15)
# text_3.place(x = 140, y = 100)

# # Ну тож создаёт кнопочки
# cnopka_camen = Button(text = 'Камень'
# 				bg = 'black'
# 			    fg = 'Green'
# 			    font = 15,
# 				command = kamen)
# cnopka_camen.place(x = 65, y = 160)

# cnopka_nojnic = Button(text = 'Ножница'
# 				bg = 'black'
# 			    fg = 'Green'
# 			    font = 15,
# 				command = nojnic)
# cnopka_nojnic.place(x = 65, y = 160)

# cnopka_bym = Button(text = 'Бумага'
# 				    bg = 'black'
# 			        fg = 'Green'
# 			        font = 15,
# 				    command = bym)
# cnopka_bym.place(x = 65, y = 160)