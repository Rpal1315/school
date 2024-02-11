def space():
    """
    This function takes no parameters and does not return anything. It loops through each character in the 'intext' variable and checks if it is not a space character. If it is not, it prints the character without a new line. 
    """
    intext = "Fluffy is great"
    l = len(intext)
    for i in range (0,l):
        if intext[i] != " ":
            print(intext[i],end="")