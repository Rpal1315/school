def MaxValueCounter(lst: list) -> tuple:
    """
    This function takes a list as input and returns a tuple containing the maximum value and its count.

    Parameters:
    lst (list): The input list from which the maximum value and its count are to be found.

    Returns:
    tuple: A tuple containing the maximum value and its count.
    """
    # Variable Declaration
    chk = lst[0]
    leng = len(lst)
    count = 0

    # Loop for Checking
    for i in range(0, leng):
        if chk < lst[i]:
            chk = lst[i]
        elif chk == lst[i]:
            count = count+1
    # for j in lst:
    #     if chk == j:
    #         count = count + 1

    return chk, count


print(MaxValueCounter([ 10, 7, 26, 3, 15, 8, 26]))
