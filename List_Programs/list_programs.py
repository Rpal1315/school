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

def nested_list():
    a = [1,2,3,[5,6]]

def list_insert():
    a = [1,3]
    a.insert(1,2)
    print(a)

def list_presence():
    a = [1,2,3,4,5]
    b = [1,2,3,4,6]

    c = 5 in a
    d = 5 in b

    print(c,d)

def list_extend():
    lst1 = [1.5,2.5,3.5,5.4]
    lst2 = [1,2,3,4,5]
    lst2.extend(lst1)
    print(lst2)

def list_slice():
    l1 = ["a","e",'p','q','r','i','o','u']
    lstc = l1[2:5]
    del l1[2:5]
    print(l1)
    print(lstc)
    l2 = l1.copy()

def list_small(a):
    lst = a
    print(lst)
    while len(lst) > 2:
        lst.pop(0)
        lst.pop(-1)
        print(lst)

list_small([1,0,1,0,1,0,1])