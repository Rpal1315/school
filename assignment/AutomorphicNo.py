# Check if a no is automorpic or not
a = int(input("Enter the no: "))
b = a ** 2
if str(b).endswith(str(a)):
    print("The no. is Automorphic")
else:
    print("The no. is not Automorphic")