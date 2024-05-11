#  Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K
#  справа цифру D (D - входной параметр целого типа, лежащий в диапазоне 0-9,
#  K - параметр целого типа, являющийся одновременно входным и выходным). С помощью этой функции
#  последовательно добавить к данному числу K справа цифры D1 и D2, выводя результат каждого добавления.
def AddRightDigit(d, k):
    orig_k = k
    k = k * 10 + d
    print(f"Результат конкатенации чисел {orig_k} и {d} равен {k}")
    return k

def check_k(a):
    while type(a) != int:
        try:
            a = int(a)
            if a < 0:
                print("Вы ввели неправильное значение")
                a = input("Введите число еще раз: ")
        except ValueError:
            print("Вы ввели неправильное значение")
            a = input("Введите число еще раз: ")
    return a

def check_d(a):
    while type(a) != int:
        try:
            a = int(a)
            if a > 9 or a < 0:
                print("Вы ввели неправильное значение")
                a = input("Введите число еще раз: ")
        except ValueError:
            print("Вы ввели неправильное значение")
            a = input("Введите число еще раз: ")
    return a

first_n = input("Введите положительное целое число: ")
first_n = check_k(first_n)
n1 = input("Введите первое целое число от 0 до 9: ")
n1 = check_d(n1)
n2 = input("Введите второе целое число от 0 до 9: ")
n2 = check_d(n2)
first_n = AddRightDigit(n1, first_n)
AddRightDigit(n2, first_n)
