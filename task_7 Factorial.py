from itertools import count
from math import factorial


def f_gen():
    for el in count(1):
        yield factorial(el)


generator = f_gen()
x = 0
for i in generator:
    if x == 20:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")