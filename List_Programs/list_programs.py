def list_freq(l1: list):
    """
    Calculate the frequency of each element in the given list.

    Parameters:
    l1 (list): A list of elements.

    Returns:
    None
    """
    for i in l1:
        count = 0
        for j in l1:
            if i == j:
                count += 1
                l1.remove(i)
        print(i, ":", count)

    print(i, ":", count)


def list_freq_1(l1: list):
    """
    Generate the frequency count of each element in a given list.

    Args:
        l1 (list): The input list for which the frequency count needs to be generated.

    Returns:
        None: This function does not return any value.
    """
    while l1:
        count = l1.count(l1[0])
        val = l1[0]
        l1 = [x for x in l1 if x != val]
        print(val, ":", count)
    print(l1)


def nested_list():
    a = [1, 2, 3, [5, 6]]


def list_insert(lst: list, ins, indx):
    """
    Insert an element into a list at a specified index.

    Args:
        lst (list): The list to insert the element into.
        ins: The element to insert into the list.
        indx (int): The index at which to insert the element.

    Returns:
        list: The modified list with the element inserted at the specified index.
    """
    lst.insert(indx, ins)
    return lst


def list_presence(lst: list, chk):
    """
    Check if `chk` is present in `lst`.

    Parameters:
        - lst (list): The list to be checked.
        - chk: The element to search for in the list.

    Returns:
        - bool: True if `chk` is present in `lst`, False otherwise.
    """
    out = chk in lst

    return out


def list_extend(lst1:list,lst2:list):
    """
    Extends lst2 with the elements from lst1.

    Args:
        lst1 (list): The list to be extended onto lst2.
        lst2 (list): The list to be extended.
    """
    lst2.extend(lst1)
    print(lst2)


def list_slice():
    l1 = ["a", "e", 'p', 'q', 'r', 'i', 'o', 'u']
    lstc = l1[2:5]
    del l1[2:5]
    print(l1)
    print(lstc)
    l2 = l1.copy()


def list_small(a):
    """
    Removes the first and last elements from a list until the length of the list is less than or equal to 2.

    Parameters:
        a (list): The input list.

    Returns:
        None
    """
    lst = a
    print(lst)
    while len(lst) > 2:
        lst.pop(0)
        lst.pop(-1)
        print(lst)


def list_count(lst: list, src):
    """
    Count the number of occurrences of a given element in a list.

    Parameters:
        lst (list): The list to search for the element.
        src : The element to count in the list.

    Returns:
        int: The number of times the element appears in the list.
    """
    cnt = lst.count(src)
    return cnt


def list_rewrite(lst: list, src):
    """
    A function that takes a list and a source value as input and returns a new list containing a sorted subsequence of the original list, starting from the first occurrence of the source value and ending at the last occurrence.

    Parameters:
    - lst (list): The original list.
    - src: The source value to search for in the original list.

    Returns:
    - list: A new list containing the sorted subsequence of the original list.
    """ 
    cnt = list_count(lst, src)
    lst.sort()
    i = lst.index(src)
    l1 = lst[i:i + cnt]
    return l1
