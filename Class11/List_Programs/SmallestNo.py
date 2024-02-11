# Find the smallest no. in a list
lst = eval(input("Enter the list: "))
k = lst[0]
for i in lst:
    if i < k:
        k=i

print(k)