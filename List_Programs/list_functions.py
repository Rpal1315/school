def list_reversal():
    str = "Hello0"
    l1 = list(str)
    for i in range(0, (len(l1))//2):
        l1[i], l1[-(i+1)] = l1[-(i+1)], l1[i]

    print(l1)


# noinspection PyUnusedLocal
def list_compare():
    l1 = [1, 2, 5, 9]
    l2 = [1, 2, 6, 7]
    l3 = [1, 2, 5, 9]
    print(l1 > l2)
    print(l2 > l1)


def list_copy():
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
    b = list(a)  # METHOD 1
    b = a.copy()
    b.append(5)
    print(a)
    print(b)


def list_index():
    a = ["harish", "raman", "zoya"]
    print(a.index("zoya"))


def list_join():
    """
    Joins two lists and returns the combined list.

    Returns:
        list: The combined list.
    """
    # Define the first list
    l1 = [1, 3, 5]

    # Define the second list
    l2 = [2, 4, 6]

    # Combine the two lists
    l3 = l1 + l2

    # Return the combined list
    return l3


def list_sort():
    """
    Sorts a list of items.

    Returns:
        list: The sorted list.
    """
    # Join the list items into a string
    items = list_join()

    # Sort the items
    items.sort()

    return items


var = list_sort()
print(var)