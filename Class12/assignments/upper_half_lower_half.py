#Write a program to print the sum of upper & lower half of a matrix which correspond to the left diagonal(square matrix only)


rows = int(input("Enter the no. of rows: "))
cols = int(input("Enter the no. of columns: "))

mat = []
for i in range(rows):
    row = []
    for j in range(cols):
        elem = int(input(f"Element ({i},{j}): "))
        row.append(elem)
    mat.append(row)

sum_upper = 0
for i in range(rows):
    for j in range(cols):
        if i < j:
            sum_upper += mat[i][j]

print("The sum of upper half of the matrix is:", sum_upper)

sum_lower = 0

for i in range(rows):
    for j in range(cols):
        if i > j:
            sum_lower += mat[i][j]

print("The sum of lower half of the matrix is:", sum_lower)
