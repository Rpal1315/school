# Find if a no. and its reverse are both prime or not

n = int(input("Enter a no.: "))
n1 = n
s = 0
f1 = 0
f2 = 0

while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

for i in range(2,n):
    if n % i == 0:
        f1 = 1

for i in range(2,s):
    if s % i == 0:
        f2 = 1

if f1 == 0 and f2 == 0:
    print("The number is a reverse prime")
else:
    print("The number is not a reverse prime")
