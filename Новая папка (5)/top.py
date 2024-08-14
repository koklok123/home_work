class Car: # шаблон или чертеж
    "Атрибут класса"
    # marka = 'mercedes'
    # model = 'cls'
    # color = 'black'
    def __init__(self, marka, model, color): # __init__ - конструктор
        "Атрибут объекта"
        self.marka = marka
        self.model = model 
        self.color = color
        self.bak = 0
        self.is_start = False
        self.gorod = False
        
    def info(self):
        print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
    def start(self):
        if self.bak > 0:
            self.is_start = True
            print(f'Марка машины-{self.marka}, модель-{self.model}, заведена')
        elif self.bak < 0:
            print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 
        elif self.bak > 0:
            self.gorod = True
            print(f'Марка машины-{self.marka}, модель-{self.model}, заведена, Едем в {self.gorod}')
        elif self.bak < 0:
            self.gorod = False
            print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива не едем в город') 

toyota = Car('Toyota', 'camry', 'white')
toyota.info()
toyota.start()
