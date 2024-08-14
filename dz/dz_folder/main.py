
# from canculator import plus, multiplication, minus, dele
# from palid import pal
# from step import exponentiate

# while True:
            
#             choice = input("Выберите действие (арифметика, палиндром, степень, выход): ").strip().lower()
#             print(f"Ваш выбор: {choice}")
            
#             if choice == 'выход':
#                 print("Выход из программы")
#                 break
#             elif choice == 'арифметика':
#                 operation = input("Выберите операцию (сложение, вычитание, умножение, деление): ").strip().lower()
#                 x = float(input("Введите первое число: "))
#                 y = float(input("Введите второе число: "))
                
#                 if operation == 'сложение':
#                     print(f"Результат: {plus(x, y)}")
#                 elif operation == 'вычитание':
#                     print(f"Результат: {minus(x, y)}")
#                 elif operation == 'деление':
#                     print(f"Результат: {dele(x, y)}")
#                 elif operation == 'умножение':
#                     print(f"Результат: {multiplication(x, y)}")
#                 else:
#                     print("Неизвестная операция")

#             elif choice == 'степень':
#                 base = int(input("Введите число для возведения в степень: "))
#                 exp = int(input("Введите степень: "))
#                 print(f"Результат: {exponentiate(base, exp)}")
           
#             elif choice == 'палиндром':
#                 s = input("Введите строку: ")
#                 print(f"Это палиндром: {pal(s)}")
#             else:
#                 print("Неизвестное действие")







# "Абстракция"

# class Shape:
# 	def area(self):
# 		pass
# 	def perimetor(self):
# 		pass
	

# class Square(Shape):
# 	def __init__(self, side):
# 		self.side = side 
		
# 	def area(self):
#         return self.side * 2 
	
#     def perimetor(self):
#         return 4 * self.side
	

# class Circle(Shape):
		
#     def __init__(self, radius):
#         self.radius = radius
	
#     def area(self):
#         return 3.14 * self.radius ** 2
	
#     def perimetor(self):
#         return 2 * 3.14 * self.radius
	
    
# sqeare = Square(4)
# print(f'Площадь квадрата: {sqeare.area()}')
# print(f'Периметр квадрат: {sqeare.peremetre()}')
      



# crue = Circle(3)
      
# print(f'Площадь круга: {crue.area()}')
# print(f'Периметр круга: {crue.perimetor()}')
      


class Vehicle:
    def start_engiene(self):
        pass

    def stop_engiene(self):
        pass

    def drive(self):
        pass

class Car(Vehicle):
    def start_engiene(self):
        return "Двигатель заведён"
    
    def stop_engiene(self):
        return "Двигатель авто не завендён"
    
    def drive(self):
        return "Авто едет"

class Bicycle(Vehicle):

    def start_engiene(self):
        return "У велосипеда нет движка"
    
    def stop_engiene(self):
        return "Там знак стоп"
    
    def drive(self):
        return "Велосипед не едет"
    

car = Car()
print(car.start_engiene())
print(car.stop_engiene())
print(car.drive())

bicycle = Bicycle()
print(bicycle.start_engiene())
print(bicycle.stop_engiene())
print(bicycle.drive())
  