my_dict = {}
with open("text_6.txt", encoding="utf-8") as o:
    for line in o:
        n, stats = line.split(':')
        n_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[n] = n_sum
print(f"{my_dict}")
