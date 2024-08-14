# for i in range(100000000000000000000000000000000000, 0, -1):
# 	print(f"{i}Привет суслик как ты там")






class Car:
	
	def __init__(self, model, year, color, city):
		
		self.model = model
		self.year = year
		self.color = color
		self.city = city
		self.baal = True

	def drive(self):
		if self.baal == True:
            		print(f"модель-{self.model}, лет-{self.year}, Цвет-{self.color}, В какой город едем-{self.city}")
		elif self.baal == False:
			print(f"модель-{self.model}, лет-{self.year}, Цвет-{self.color}, К намшему величайшему сожеление поездку в Амстерда отменяем")
				
			
pop = Car('тесла', '13', 'белая', 'В АМСТЕРДАМ НАХУЙ')
pop.drive()