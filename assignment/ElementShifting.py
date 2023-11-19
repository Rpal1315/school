# Shift the element n places to left
n = int(input("Enter the value of n: "))
l = eval(input("Enter the list: "))

for i in range(n):
    l.append(l[0])
    l.pop(0)
print(l)