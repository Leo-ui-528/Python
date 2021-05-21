# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
import random

SIZE = 97

array = [random.randint(2, 99) for _ in range(SIZE)]
for n in range(2, 10):

    array[n] = []
    for f in range(2, 100):
        if f % n == 0:
            array[n].append(f)
    print(f'Для числа {n} кратны - {len(array[n])}')
