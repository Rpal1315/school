m_list = {"A": range(90, 100 + 1), "B": range(75, 89 + 1), "C": range(60, 74 + 1), "D": range(45, 59 + 1),
          "E": range(33, 44 + 1),
          "F": range(0, 33)}
marks = int(input("Enter the marks:"))
for i in m_list:
    if marks in m_list[i]:
        print(f"The grade is {i}")
        break
