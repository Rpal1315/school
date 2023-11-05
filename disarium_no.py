# Determine if a no. is a disarium no. or not

n = int(input("Enter a no.: "))
i = len(str(n))
s = 0
temp = n

while temp > 0:
    r = temp % 10
    s = s + r ** i
    temp = temp // 10
    i = i - 1

if n == s:
    print("The number is a disarium no.")
else:
    print("The number is not a disarium no.")
