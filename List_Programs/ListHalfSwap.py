l = eval(input("Enter the list: "))
s = len(l)

if s % 2 == 0:
    l = l + l[:(s//2)]
    for i in range(s//2):
        l.pop(i)
    print(l)