l1 = eval(input("Enter the list of nos.: "))

# Variable Declaration
chk2 = chk1 = l1[0]
leng = len(l1)

# Loop for Checking
for i in range(0,leng):
    if chk1 < l1[i]:
        chk1 = l1[i]

for i in range(0,leng):
    if chk2 < l1[i] < chk1:
        chk2 = l1[i]

print(chk2)