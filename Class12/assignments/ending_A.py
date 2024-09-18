def ending_A(names):
    """
    The function `ending_A` takes a list of names, converts each name to uppercase, and prints out the
    names that end with the letter "A".
    
    :param names: The function `ending_A` takes a list of names as input and prints out the names that
    end with the letter "A" after converting them to uppercase
    """
    for name in names:
        name = name.upper()
        if name[-1] == "A":
            print(name)



names = ["Maria", "John", "Jessica", "Roberta"]

ending_A(names)
