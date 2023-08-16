# Find the Greatest Common Divisor of two numbers
a = int(input("Enter a no.: "))
b = int(input("Enter a no.: "))

if a > b:
    a, b = b, a

while b != 0:
    r = a % b
    a = b
    b = r

print("The GCD of the two nos. is",a)