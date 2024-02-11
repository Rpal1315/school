def main():
    """
    This function takes input for the number of students, their roll numbers, and marks, and then finds and prints the student with the highest marks.
    """
    d = {}
    n = int(input("Enter the no. of students: "))
    out = {}

    for i in range(0, n):
        r = int(input("Enter roll no.: "))
        m = int(input("Enter marks: "))
        d[r] = m

    h = 0
    for i in d:
        if d[i] > h:
            h = d[i]
            m = i
    out[m] = h
    print(out)


main()
