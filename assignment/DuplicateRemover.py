# Remove duplicate elements from a list
l1 = eval(input("Enter the list: "))
leng = len(l1)
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l1)
print(l2)
