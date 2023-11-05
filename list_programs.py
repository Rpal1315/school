def list_freq(l1: list):
    for i in l1:
        count = 0
        for j in l1:
            if i == j:
                count += 1
                l1.remove(i)
        print(i, ":", count)

    print(i, ":", count)


def list_freq_1(l1: list):
    while l1:
        count = l1.count(l1[0])
        val = l1[0]
        l1 = [x for x in l1 if x != val]
        print(val, ":", count)
    print(l1)


list_freq_1([2, 5, 2, 3, 3, 3])
