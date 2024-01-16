def DictMerge(d1,d2):
    d = d1.copy()
    d.update(d2)
    return d

def DictSum(dct:dict):
    """
    Calculates the sum of all values in a given dictionary.

    Parameters:
    - dct (dict): The dictionary to calculate the sum from.

    Returns:
    - The sum of all values in the dictionary.
    """