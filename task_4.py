# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10

list_1 = [random.randint(0, 10) for _ in range(SIZE)]

max_index = 0
for i in list_1:
    if list_1.count(max_index) < list_1.count(i):
        max_index = list_1.index(i)

print(f'Число {i} в массиве {list_1}, встречается чаще всего')
