
class Appliance:
	
    def __init__(self):
          self.yes_no = False
          
    def turn_on(self):
        self.yes_no = True
	
        
    def turn_off(self):
        self.yes_no = False

    def use(self):
        pass

    def repair(self):
        pass


		
class WashingMachine(Appliance):
        def use(self):
                return "Стиральная машина начала стирку"
        def repair(self):
                return "Ремонт стиральной машины"
        


class Microwave(Appliance):
        def use(self):
                return "Микроволновая печь разогревает еду"
        def repair(self):
                return "Ремонт микроволновой печи"
        

class Refrigerator(Appliance):
        def use(self):
                return "Холодильник охлаждает продукты"
        def repair(self):
                return "Ремонт холодильника"
        


def turn_off(self):
        if self.yes_no == False:
            print(washingmachine.repair())
            print(microwave.repair())
            print(refrigerator.repair())
            return "Ну они отключены"

washingmachine = WashingMachine()
microwave = Microwave()
refrigerator = Refrigerator()

print(washingmachine.use())
print(microwave.use())
print(refrigerator.use())
    
