# Count the no. of nos. in a list
lst = eval(input("Enter the list: "))
count = 0
for i in lst:
    if i is int:
        count += 1
print(count)