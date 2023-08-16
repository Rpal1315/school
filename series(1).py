x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

s = 1

for i in range(1,n+1):
    s = s + (x**i)/i
print(s)
