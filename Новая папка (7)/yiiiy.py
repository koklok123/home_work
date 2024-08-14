# plus = lambda x, y: x + y
# multiplication = lambda x, y: x * y 
# minus = lambda x, y: x - y
# dele = lambda x, y: x / y 


# class Computer:
#     def __init__(self, cpu, memory):
#         self.choice = input("Введите 1-(Введите 1 чтобы зайти в раздел арифметика): ").strip().lower()
#         print(f"Ваш выбор: {self.choice}")
#         self.__cpu = cpu
#         self.__memory = memory

#     def make_computations(self):
#         if self.choice == '1':
#             operation = input("Выберите операцию (1-сложение, 2-вычитание, 3-умножение, 4-деление): ").strip().lower()
#             x = float(input("Введите первое число: "))
#             y = float(input("Введите второе число: "))

#             if operation == '1':
#                 print(f"Результат: {plus(x, y)}")
#             elif operation == '2':
#                 print(f"Результат: {minus(x, y)}")
#             elif operation == '4':
#                 print(f"Результат: {dele(x, y)}")
#             elif operation == '3':
#                 print(f"Результат: {multiplication(x, y)}")
#             else:
#                 print("Неизвестная операция")

#     def get_cpu(self):
#         return self.__cpu

#     def get_memory(self):
#         return self.__memory

# kok = Computer('2', '23')
# kok.make_computations()

# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().__init__(cpu, memory)
#         self.__memory_card = memory_card
        
#     def get_memory_card(self):
#         return self.__memory_card
    
#     def info(self):
#         pass
        
    
# full = Laptop('12', '14', '16')
# print(full.get_cpu()) 
# print(full.get_memory()) 
# print(full.get_memory_card()) 



















class Game:
    def __init__(self, name, gender):
        self.choise = input("Введите имя вашего персонажа: ")
        self.name = name
        self.hp = 100
        self.life = 1
        self.height = 180
        self.gender_1 = input("Выберите пол вашего персонажа 1-Женский 2-Мужской: ")
        self.gender = gender
        self.age = 20
        self.strength = 20
        self.dau = input("Пожалуйста выберите место появления: \n 1-Лагерь военных (безопасное место), \n 2-Окраины города (средняя сложность), \n 3-Центр города (непроходимый геймплей): ")

    def start(self)
        
        print(f"NickName-{self.choise}, Здоровье-{self.hp}, Кол-во жизней-{self.life}, Рост вашего персонажа-{self.height}, Пол вашего персонажа-{gender_text}, Возраст-{self.age}, Сила-{self.strength}")
        print(f"Место спавна: {place_text}. Выберите действие:")

        if self.dau == "1":
            action = input("1-Эвакуироваться и уехать\n2-Отказаться эвакуироваться\nВведите номер действия: ")
            if action == "1":
                print("Вы эвакуировались и уехали.")
            elif action == "2":
                print("Вы решили остаться.")
            else:
                print("Неверный выбор действия.")
        elif self.dau == "2":
            action = input("1-Исследовать\n2-Вернуться в лагерь\nВведите номер действия: ")
            if action == "1":
                print("Вы начали исследовать окрестности.")
            elif action == "2":
                print("Вы вернулись в лагерь.")
            else:
                print("Неверный выбор действия.")
        elif self.dau == "3":
            action = input("1-Исследовать центр\n2-Спрятаться\nВведите номер действия: ")
            if action == "1":
                print("Вы начали исследовать центр города.")
            elif action == "2":
                print("Вы спрятались в центре города.")
            else:
                print("Неверный выбор действия.")
        else:
            print("Неверный выбор места появления.")

    def info(self):
        gender_text = "Женский" if self.gender_1 == "1" else "Мужской" if self.gender_1 == "2" else "Не указан"
        place_text = {
            "1": "Лагерь военных",
            "2": "Окраины города",
            "3": "Центр города"
        }.get(self.dau, "Не указано")

        print(f"Информация о персонаже:\nИмя: {self.choise}\nПол: {gender_text}\nМесто появления: {place_text}")

# Создание экземпляра класса и запуск игры
kok = Game('Name', 'gender')
kok.start()
kok.info()
