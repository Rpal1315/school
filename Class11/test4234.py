num = int(input("Enter a no: "))
count = 0
nos = []
for i in range(2,num):
    prime = True
    for j in range(2,i):
        count += 1
        if i % j == 0:
            prime = False
            break

    if prime:
        nos.append(i)


print(nos,count)