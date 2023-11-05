# Check if a no. is palindrome or not
n = int(input("Enter a no.: "))
n1 = n
s = 0

while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

if s == n1:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
