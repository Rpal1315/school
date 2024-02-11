def swap_2():
    """
    Swaps the values of two integers, a and b, entered by the user.

    Parameters:
    None

    Returns:
    None
    """
    a = int(input("Enter a no. "))
    b = int(input("Enter a number "))

    a, b = b, a

    print("The numbers are:", a, b)


swap_2()
