num_1 = int(input("Введите первое число"))
num_2 = int(input("Введите второе число"))
num_3 = int(input("Введите третье число"))

m = (min(num_1, num_2, num_3))


def my_func(n_1, n_2, n_3):
    return num_1 + num_2 + num_3 - m


print(my_func(num_1, num_2, num_3))
