import random

length = input('Задайте длину списка (от 5 до 30): ') # Предлагаем ввести длину списка с последующей проверкой

while type(length) != int:
        try:
            length = int(length)
            if length > 30 or length < 5:
                print("Вы ввели неправильное значение")
                length = input('Задайте длину списка (от 5 до 30): ')
        except ValueError:
            print("Вы ввели неправильное значение")
            length = input('Задайте длину списка (от 5 до 30): ')

list = []

for i in range(length): # Заполняем список числами
    list.append(random.randint(-20, 20))
print('Изначальный список: ', list)

local_min = []

for i in range(len(list) - 2):
    if list[i] > list[i + 1] and list[i + 1] < list[i + 2]:
        local_min.append(i)

for i in range(len(local_min)):
     list[local_min[i] + 1] **= 2
print('Список с возведенными в квадрат локальными минимумами: ', list)