r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))
lst = []
for i in range(r):
    row = []
    for j in range(c):
        elem = input(f"Element ({i},{j}): ")
        row.append(elem)
    lst.append(row)

print(lst)