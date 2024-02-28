# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
import random

matrix = [[random.randint(-10,10) for i in range(3)] for i in range(3)]
print(f'Изначальная матрица: {matrix}')

n = input('Какой столбец нужно изменить? (от 1 до 3) - ')
while type(n) == str:
    try:
        n = int(n)
        if 1 > n or n > 3:
            n = input('Вы ввели недопустимое значение.\nВведите число еще раз (от 1 до 3): ')
    except:
        n = input('Вы ввели недопустимое значение.\nВведите число еще раз (от 1 до 3): ')
    
def change(n):
    n += 3
    yield n

matrix[n-1] = [next(change(matrix[n-1][i])) for i in range(3)]

    
print(f'Измененная матрица: {matrix}')