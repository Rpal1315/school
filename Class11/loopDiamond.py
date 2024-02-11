# n = int(input("Enter a no.: "))
n = 5
for i in range(n + 1):
    for j in range(i, n):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")

    print()
for i in range(n - 1, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")

    print()
