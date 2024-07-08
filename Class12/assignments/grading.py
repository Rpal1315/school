"""
Create a dictionary S which contains Name:[Eng,Math,Sci] as key value pairs, Display the grades according to the following criteria

Marks       Grade
>=90            A
<90 and >=60    B
<60             C
"""
S: dict[str, list[int]] = {}
entry_count = int(input("Enter the number of entries: "))
for i in range(entry_count):
    name = input("Enter the name: ")
    eng = int(input("Enter the marks in English: "))
    math = int(input("Enter the marks in Math: "))
    sci = int(input("Enter the marks in Science: "))
    S[name] = [eng, math, sci]



for j in S:
    m = (S[j][0] + S[j][1] + S[j][2]) / 3
    if m >= 90:
        print(j, ":", "A")
    elif m >= 60:
        print(j, ":", "B")
    else:
        print(j, ":", "C")


