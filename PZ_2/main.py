# Вариант 19. Дано трёхзначное число. В нём зачеркнули первую справа цифру и приписали её слева. Вывести полученное число.

orig_num = int(input('Введите положительное трёхзначное число: '))
if orig_num < 0:
    num = orig_num * (-1)
    num = str(num)
else:
    num = orig_num
if len(str(num)) != 3: # Обработка исключений
    print('Ваше число нетрёхзначное')
else:
    num = int(num) # Обработка числа
    fig1 = num // 100
    fig2 = num // 10
    fig2 = fig2 % 10
    fig3 = num % 100
    fig3 = fig3 % 10
if orig_num < 0:
    print('Ваше изменённое число: -', fig3, fig1, fig2, sep='')
else:
    print('Ваше изменённое число: ', fig3, fig1, fig2, sep='')