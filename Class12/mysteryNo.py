# Find out if a no. is a mystery no. or not
def reverseNo(num: int) -> int:
    numStr = str(num)
    numStr = numStr[::-1]
    num = int(numStr)
    return num


def mysteryNo(num: int) -> None:
    """
    Mystery No. = A no. which can be expressed as the sum of a number and its reverse.

    Args:
        num: The no. to be checked

    Returns:
        object: None
    """
    for i in range(1, num // 2 + 1):
        iRev = reverseNo(i)
        if i + iRev == num:
            print(f"Mystery Number. The number pair is ({i},{iRev})")
            break
    else:
        print("Not a Mystery Number")


mysteryNo(129)
mysteryNo(121)
