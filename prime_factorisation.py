from prime import prime

f=[]
n = int(input("Enter a no."))
q = n

while q != 1:
    for i in range(1,n+1):
        if q % i == 0 and prime(i):
            f.append(i)
            q = q / i
            break


print(f)        