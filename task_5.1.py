def sum_num():
    s = 0
    while True:
        numbers = input("Введите числа через пробел").split()
        for num in numbers:
            if num =='q':
                return s
            else:
                 try:
                    s += int(num)
                 except ValueError:
                        print("Для выхода из программы нажмите, - 'q'.")
        print(f"sum of numbers = {s}")
        

print(sum_num())



