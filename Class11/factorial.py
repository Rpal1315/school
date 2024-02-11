# WAP to find the factorial of a no.
from big_o import big_o


def V1():
    n = int(input("Enter a no.: ", ))
    f = 1

    for i in range(1, n + 1):
        f = f * i
    print("The factorial of", n, "is", f)


def V2(n: int):
    while n > 0:
        if n > 1:
            return V2(n - 1) * n
        else:
            return 1


import big_o

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(V2, positive_int_generator, n_repeats=100)
print(best)
