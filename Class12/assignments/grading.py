"""
Create a dictionary S which contains Name:[Eng,Math,Sci] as key value pairs, Display the grades according to the following criteria

Marks       Grade
>=90            A
<90 and >=60    B
<60             C
"""
def grading():
    S={}
    entry_count = int(input("Enter the number of entries: "))
    for i in range(entry_count):
        name = input("Enter the name: ")
        eng = int(input("Enter the marks in English: "))
        math = int(input("Enter the marks in Math: "))
        sci = int(input("Enter the marks in Science: "))
        S[name] = [eng, math, sci]



    for i in S:
        m = (S[i][0] + S[i][1] + S[i][2]) / 3
        if m >= 90:
            print(i, ":", "A")
        elif m >= 60:
            print(i, ":", "B")
        else:
            print(i, ":", "C")


grading()