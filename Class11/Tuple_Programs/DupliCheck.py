def DupliCheck(tup1:tuple):
    count = 0
    for i in range(0,len(tup1)):
        v = tup1[i]
        for j in range(i+1, len(tup1)):
            if v == tup1[j]:
                count = count+1
    return count
print(DupliCheck((26,15,7,7,17,26)))