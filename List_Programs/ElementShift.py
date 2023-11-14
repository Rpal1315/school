

l1 = list(eval(input("Enter the list: ")))

# Variable Declaration
leng = len(l1)

for i in range(0,leng+1):
    t = l1[0]
    l1.insert(leng-1,t)
    l1.pop(0)

print(l1)
