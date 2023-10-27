# Даны три целых числа: A, B, C. Проверить истинность высказывания: "Число B находится между A и C".

a, b, c = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")

while type(a) != int:  # Проверка первого числа на тип данных int
    try:
        a = int(a)
    except ValueError:
        print("Вы ввели неправильное значение")
        a = input("Введите первое число: ")

while type(b) != int:  # Проверка второго числа на тип данных int
    try:
        b = int(b)
    except ValueError:
        print("Вы ввели неправильное значение")
        b = input("Введите второе число: ")

while type(c) != int:  # Проверка третьего числа на тип данных int
    try:
        c = int(c)
    except ValueError:
        print("Вы ввели неправильное значение")
        c = input("Введите третье число: ")

if (a > b > c) or (a < b < c):
    print("Число B находится между A и C")
else:
    print("Число B НЕ находится между A и C")