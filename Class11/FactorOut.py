num = int(input("Enter the no: "))
factor = []
count = 1
q = 0
while count <= num / 2:
    if num / count in factor:
        break
    if num % count == 0:
        factor.append(count)
        q = int(num / count)
        if q != count:
            factor.append(q)
    count += 1
factor.sort()
print(factor, count)
