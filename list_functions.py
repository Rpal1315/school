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
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    l3 = l1 + l2
    return l3


def list_sort():
    var = list_join()
    var.sort()
    return var


var = list_sort()
print(var)