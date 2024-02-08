def SecondLargestNoV2(l1: tuple) -> tuple:
    """
    This function takes a tuple as input and returns a tuple containing the two largest numbers from the input tuple.

    Parameters:
    l1 (tuple): The input tuple from which the two largest numbers are to be found.

    Returns:
    tuple: A tuple containing the two largest numbers from the input tuple.
    """

    # Variable Declaration
    chk1 = chk2 = 0
    leng = len(l1)

    # Loop for Checking
    for i in range(0, leng):
        if chk2 < l1[i]:
            chk2 = l1[i]
        if chk1 < l1[i]:
            chk2 = chk1
            chk1 = l1[i]

        print(chk1, chk2)

    return chk1, chk2


print(SecondLargestNoV2((26, 10, 7, 3, 15, 8)))
