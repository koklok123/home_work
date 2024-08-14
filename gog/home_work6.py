# def is_even(number):
	
value = float(int(input("Введите число: ")))
# print(isinstance(value,float int))
# print("Первое float второе int (значения)")
if value == 123:
	print(value.is_integer())
else: 
	value == 123.0
print(isinstance(value, int))

# #value = float(input("Введите число: "))

print(value.is_integer())

#функция фактория переменная n 

def factorial(n):
#если n равен 0 или n равен 1 возвращает 1
    if n == 0 or n == 1:
        return 1
    #если вернуть n *-одно факториал N-1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) 
print(factorial(0))  
print(factorial(1))  
print(factorial(6))  
#функция 
def my_set(my_set):
    return sorted(my_set)


list_set = {21, 32, 1, 2, 3, 6, 5, 4}
sorted_elements = my_set(list_set)
print(sorted_elements)  
#в принципе второй вариант
my_list = {2,34,54,34,2, 43,23,12,1}
print(my_list)




def are(set1, set2):
    return set1 == set2

# Пример использования:
my_set1 = {1, 2, 3}
my_set2 = {3, 5, 1}
result = are(my_set1, my_set2)
print(f"Множества равны? True-да, False-нет:  {result}") 



spis = [1,2,3,4,5,6,7,8,9,10]
newspis = spis [::-2]
print(newspis)
      
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

s = "1,2,3,4,5,6,7,8,9"
reversed_s = reverse_string(s)
print(reversed_s)



my_listit = len([1, 2, 3, 45, 6, 4, 32, 6, 7, 32])
print(my_listit)
print(f"вот столько аргументов {my_listit}")
