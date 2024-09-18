

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# a function what swaps elements at even places


def swap_elements(lst):
    for i in range(0, len(lst), 3):
        if i % 2 == 0:
            lst[i], lst[i + 2] = lst[i + 2], lst[i]

    return lst


# calling the function
print(swap_elements(a))





