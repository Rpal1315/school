# Find out is a no. is a special palindrome or not
num = int(input("Enter a no.:"))
numStr = str(num)
counter = 0
chkID = (len(numStr) // 2)
for i in range(0, len(numStr)):
    for j in range(i + 1, len(numStr)):
        if numStr[i] == numStr[j]:
            counter += 1

if counter == chkID:
    print("Special Palindrome")
else:
    print("Not a Special Palindrome")
