import random

a = 0
i = 0
tst = random.randint(10, 50)
print(tst)

while i <= 50:
    i = i + 3
    a = a + 1
    if i == tst:
        print(a)
        break
