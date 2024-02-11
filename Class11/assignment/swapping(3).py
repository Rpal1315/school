def swap_3():
    """
    Swaps the values of two integers entered by the user and prints the swapped values.
    
    Parameters:
    None
    
    Returns:
    None
    """
    # Prompt user to input two integers
    a = int(input("Enter a no. "))
    b = int(input("Enter a number "))

    # Swap the values of a and b using tuple unpacking
    a, b = b, a

    # Print the swapped values of a and b
    print("The numbers are:", a, b)


swap_3()
