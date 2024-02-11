n = int(input("Enter a no.: "))
s1 = 0
s2 = 0

# Odd Sum
for i in range(1, n + 1, 2):
    s1 = s1 + i

# Even Sum
for i in range(2, n + 1, 2):
    s2 = s2 + i

print("Odd Sum:", s1)
print("Even Sum:", s2)
