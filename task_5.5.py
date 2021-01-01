from random import randint

with open("text.txt", 'w', encoding="utf-8") as my_f:
    my_l = [randint(1,100) for _ in range(100)]
    my_f.write(" ".join(map(str, my_l)))

print(f"Sum of elements - {sum(my_l)}")