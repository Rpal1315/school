n = int(input("Enter a no.: "))
chk = True
for i in range(2,n):
    if n % i == 0:
        chk = False
        break

if chk:
    print("The number is prime")
else:
    print("The number is not prime")