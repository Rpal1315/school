def ArmstrongNo():
    """
    Takes user input, calculates the length of the input number, and checks if it is an Armstrong number.
    """
<<<<<<< HEAD:Class11/assignment/ArmstrongNo.py
    inp = int(input("Enter a no: "))
=======
    inp = int(input("Enter a no:"))
>>>>>>> 6a6ff3d58dba019a3152c73435a7c9a591d48248:assignment/ArmstrongNo.py
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
