## WAP to find the factorial of a no.
n = int(input("Enter a no.: ",))
f = 1

for i in range(1,n+1):
    f = f * i
print("The factorial of",n,"is",f)
