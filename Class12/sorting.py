samp = [14,13,12,16,14,17,10]
def bubble_sort(a:list)-> list:
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def insertion_sort(a:list) -> list:
    b = [a[0]]
    for i in range(1,len(a)):
        for j in range(len(b)):
            if a[i]<b[j]:
                b.insert(j-1,a[i])
    return b

print(insertion_sort(samp))

