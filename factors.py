n = int(input("Enter the number"))
f = []
for i in range(1,n+1):
    if n%i == 0:
        f.append(i)

print(f)