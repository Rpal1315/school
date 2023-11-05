# Input 2 lists and check for common elements
l1 = eval(input("Enter list 1: "))
l2 = eval(input("Enter list 2: "))

for i in l1:
    if i in l2:
        print("Overlapped")
        break
else:
    print("Separated")