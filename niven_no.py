# Check if a no. is a niven no. or not

n = int(input("Enter a no.: "))
s = 0
temp = n

while temp > 0:
    r = temp % 10
    s = s + r
    temp = temp // 10

if n % s == 0:
    print("The number is a niven no.")
else:
    print("The number is not a niven no.")