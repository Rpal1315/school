def sublistV1(inp: list) -> list[list]:
    """
    Generate a list of sublists from the given input list.

    Args:
        inp (list): The input list from which sublists will be generated.

    Returns:
        list[list]: A list of sublists. Each sublist contains consecutive elements from the input list.

    Example:
        >>> sublistV1([0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5])
        [[0], [1, 1], [2, 2], [3, 3, 3], [4, 4], [5]]
    """
    out = [inp[0:1], ]
    for i in range(1, len(inp)):
        if out[-1][-1] == inp[i]:
            out[-1].append(inp[i])

        else:
            oList = list()
            oList.append(inp[i])
            out.append(oList)
    return out


# print(sublistV1([0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]))


def sublistV2(inp: list) -> list[list]:
    """
    Generate a list of sublists from the given input list.

    Args:
        inp (list): The input list from which sublists will be generated.

    Returns:
        list[list]: A list of sublists. Each sublist contains consecutive elements from the input list.

    Example:
        >>> sublistV2([5, 0, 1, 0, 2, 1, 3, 2, 3, 4, 3, 5])
        [[5, 5], [0, 0], [1, 1], [2, 2], [3, 3, 3], [4]]
    """
    out = []
    leng = len(inp)
    i = 0
    while i < leng:
        chk = inp.pop(0)
        oList = list()
        oList.append(chk)
        leng = len(inp)
        j = 0
        while j < leng:
            if inp[j] == chk:
                oList.append(inp[j])
                inp.pop(j)
            leng = len(inp)
            j += 1
        out.append(oList)
    return out


if __name__ == '__main__':
    # print(sublistV2([5, 0, 1, 0, 2, 1, 3, 2, 3, 4, 3, 5]))
    print(sublistV2([0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]))
