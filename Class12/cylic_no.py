n = int(input("Enter a number: "))
chk = True
nLen = len(str(n))
for i in range(1,nLen+1):
    num = n*i
    strNum = str(num)
    strN = str(n)
    for j in strNum:
        if j not in strN:
            chk = False
            break

if chk:
    print("The number is cyclic")
else:
    print("The number is not cyclic")