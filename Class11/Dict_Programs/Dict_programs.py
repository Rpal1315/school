def DictMerge(d1,d2):
    """
    Merge two dictionaries.

    Args:
        d1 (dict): The first dictionary to be merged.
        d2 (dict): The second dictionary to be merged.

    Returns:
        dict: The merged dictionary.

    """
    d = d1.copy()
    d.update(d2)
    return d

def DictSum(dct:dict):
    """
    Calculate the sum of all values in a dictionary.

    Args:
        dct (dict): The dictionary to calculate the sum of.

    Returns:
        int: The sum of all values in the dictionary.
    """
    out = sum(dct.values())
    return out


DictSum({"Ram": 89, "Shyam": 99, "Jadu": 77, "Idrish": 78})
