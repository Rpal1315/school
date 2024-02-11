# Remove duplicates from a list

l1 = eval(input("Enter the list: "))
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)