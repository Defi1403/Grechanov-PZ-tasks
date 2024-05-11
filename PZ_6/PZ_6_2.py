# Дан список размера N. Найти минимальный из его локальных максимумов (локальный максимум - это элемент, который больше любого из своих соседей).

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

local_max = 21

for i in range(len(list) - 2):
    if list[i] < list[i + 1] > list[i + 2]:
        if local_max > list[i + 1]:
            local_max = list[i+1]

if local_max == 21:
    print('Локальные максимумы не найдены')
else:
    print('Минимальный из локальных максимумов:', local_max)
