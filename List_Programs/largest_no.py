l1 = eval(input("Enter the list of nos.: "))

# Variable Declaration
chk = l1[0]
leng = len(l1)

# Loop for Checking
for i in range(0,leng):
    if chk < l1[i]:
        chk = l1[i]

print(chk)