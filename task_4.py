n: int = int(input("введите многозначное число: "))
m = -1
while n > 10:
    d = n % 10
    n //= 10
    if d > m:
        m = d
print(m)
