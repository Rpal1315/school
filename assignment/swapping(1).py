def swap_1():
    """
    Swaps the values of two numbers entered by the user.
    This function does not take any parameters and does not return anything.
    """
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a
    a = b
    b = c

    print("The numbers are:",a,b)

swap_1()