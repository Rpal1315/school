def list_reversal():
    str = "Hello0"
    l1 = list(str)
    for i in range(0,(len(l1))//2):
        l1[i],l1[-(i+1)] = l1[-(i+1)],l1[i]

    print(l1)

def list_compare():
    l1 = [1,2,5,9]
    l2 = [1,2,6,7]
    l3 = [1,2,5,9]
    print(l1 > l2)
    print(l2 > l1)

def list_copy():
    a = [1,2,3]
    b = a
    b.append(4)
    print(a)
    b = list(a) # METHOD 1
    b = a.copy()
    b.append(5)
    print(a)
    print(b)

def list_index():
    a = ["harish","raman","zoya"]
    print(a.index("zoya"))

