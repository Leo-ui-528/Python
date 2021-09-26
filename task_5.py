# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

SIZE = 20

array = [random.randint(-10, 10) for _ in range(SIZE)]

i = 0
index = -1
while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1
print(f'В массиве{array}, элемент {array[index]}, на позиции {index} - максимальный отрицательный')
