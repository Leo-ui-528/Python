f = int(input("Введите первое число"))
s = int(input("Введите второе число"))


def my_d(first, second):
    return first / second


try:
    f / s
except ZeroDivisionError:
    print("0")

print(my_d(f, s))
