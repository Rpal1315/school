def main():
    # Write a program to find the highest marks in dict. containing the roll no. as key and marks as value
    d = {}
    n = int(input("Enter the no. of students: "))

    for i in range(0,n):
        r = int(input("Enter roll no.: "))
        m = int(input("Enter marks: "))
        d[r]=m

    h = 0
    for i in d:
        if d[i] > h:
            h = d[i]

    print(h)

def v1_1():

    d = {}
    n = int(input("Enter the no. of students: "))

    for i in range(0, n):
        r = int(input("Enter roll no.: "))
        m = int(input("Enter marks: "))
        d[r] = m

    h = 0
    for i in d:
        if d[i] > h:
            h = d[i]
            p = i

    print(f"{p}:{h}")

def v2():
    d = {}
    n = int(input("Enter the no. of students: "))

    for i in range(0, n):
        d1 = {}
        r = int(input("Enter roll no.: "))
        n = input("Enter name: ")
        m = int(input("Enter marks: "))
        d1['name'] = n
        d1['marks'] = m
        d[r] = d1

    h = 0
    for i in d:
        if d[i]['marks'] > h:
            h = d[i]['marks']
            p = i

    print(d[i])

v2()