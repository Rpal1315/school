# Sum of alternate elements of matrix
rows = int(input("Enter the no. of rows: "))
cols = int(input("Enter the no. of columns: "))

mat = []
for i in range(rows):
    row = []
    for j in range(cols):
        elem = int(input(f"Element ({i},{j}): "))
        row.append(elem)
    mat.append(row)

sum = 0
for i in range(rows):
    for j in range(cols):
        if (i+j) % 2 == 0:
            sum += mat[i][j]

print("The sum of alternate elements of the matrix is:", sum)