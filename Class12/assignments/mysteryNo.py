# Find out if a no. is a mystery no. or not
def reverse_no(num: int) -> int:
    num_str = str(num)
    num_str = num_str[::-1]
    num = int(num_str)
    return num


def mystery_no(num: int) -> None:
    """
    Mystery No. = A no. which can be expressed as the sum of a number and its reverse.

    Args:
        num: The no. to be checked

    Returns:
        object: None
    """
    for i in range(1, num // 2 + 1):
        irev = reverse_no(i)
        if i + irev == num:
            print(f"Mystery Number. The number pair is ({i},{irev})")
            break
    else:
        print("Not a Mystery Number")





def rev(x) -> str:
    if len(x) > 1:
        return x[-1] + rev(x[:len(x) - 1])
    else:
        return x

if __name__ == '__main__':
    mystery_no(129)
    mystery_no(121)
