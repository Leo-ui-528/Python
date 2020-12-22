numbers = [int(i) for i in input("Введите числа через пробел").split()]
if numbers =='q':
    break
print(sum(numbers))
n = (sum(numbers))

numbers_2 = [int(i) for i in input("Введите числа через пробел").split()]
m = (sum(numbers_2))

print(m)

print(m + n)
