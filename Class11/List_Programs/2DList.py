r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))
lst = []
for i in range(r):
    row = []
    for j in range(c):
        elem = input(f"Element ({i},{j}): ")
        row.append(elem)
    lst.append(row)

print(print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in lst])))