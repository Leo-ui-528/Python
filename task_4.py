# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 2) for _ in range(SIZE)]
print(array)

counter = {}
frequency = 1
num = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

    if counter[item] > frequency:
        frequency = counter[item]
        num = item

if num is not None:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')

