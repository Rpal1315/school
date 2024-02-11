def PowerTuple(tupin:tuple,pow:int):
    a = []
    for i in range(0,len(tupin)):
        t1 = tupin[i]
        b = []
        for j in range(1,pow+1):
            t2 = t1**j
            b.append(t2)
        b = tuple(b)
        a.append(b)
    a = tuple(a)
    return a


print(PowerTuple((2,3,5), 10))