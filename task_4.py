from random import randint

my_list = [randint(-5, 5) for _ in range(30)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")
