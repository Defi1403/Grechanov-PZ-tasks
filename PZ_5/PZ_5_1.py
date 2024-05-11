#  Найти сумму чисел ряда 1,2,3,4... от числа n до числа m. Суммирование оформить функцией
#  с параметрами. Значение n и m программа должна запрашивать

def amount(num1, num2):
    sum = 0
    while num1 < num2:
        sum += num1
        num1 += 1
    return sum

def check(a):
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("Вы ввели неправильное значение")
            a = input("Введите число еще раз: ")
    return a

n = input("Введите первое число: ")
n = check(n)
m = input("Введите второе число: ")
m = check(m)
print(f"Сумма чисел ряда от {n} до {m} равна {amount(n, m)}")
