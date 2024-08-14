
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