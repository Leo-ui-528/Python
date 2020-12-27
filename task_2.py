my_list = [int(i) for i in input("Введите числа через пробел").split()]
previous = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(previous)
