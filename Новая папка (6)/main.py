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
# toyota.info()
# toyota.start()







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