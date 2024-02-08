def ArmstrongNo():
    inp = int(input("Enter a no:"))
    leng = len(str(inp))
    s = 0
    for i in str(inp):
        i = int(i)
        s += i ** leng

    if s == inp:
        print("The no. is a Armstrong No.")
    else:
        print("The no. is not a Armstrong No.")


ArmstrongNo()
