def puzzle(w, n):
    nw_list = []
    for i in range(0, len(w)):
        if (i + 1) % n == 0:
            nw_list.append("_")
        else:
            nw_list.append(w[i])

    nw = "".join(nw_list)
    return nw


print(puzzle("Television", 3))
