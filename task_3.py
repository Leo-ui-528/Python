# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10

array = [random.randint(3, 6) for _ in range(SIZE)]
print(f'Массив до изменения: {array}')

maxi = 0
mini = 10
for i in array:
    if i > maxi:
        maxi = i
    elif mini > i:
        mini = i

    # print(mini, maxi)

maxi = array.index(maxi)
mini = array.index(mini)

array[mini], array[maxi] = array[maxi], array[mini]

print(f'Массив после изменения: {array}')
