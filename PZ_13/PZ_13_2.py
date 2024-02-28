# В матрице элементы последнего столбца заменить на -1
import random

matrix = [[random.randint(-10,10) for i in range(3)] for i in range(3)]
print(f'Изначальная матрица: {matrix}')

def change(n):
    n[-1] = -1
    yield n

new_matrix = [next(change(matrix[i])) for i in range(3)]

print(f'Измененная матрица: {new_matrix}')