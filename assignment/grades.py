def grades():
    # prompt the user for roll number and name, and marks obtained in physics, chemistry and computer
    roll = int(input("Enter the roll no. "))
    name = input("Enter the name of student ")
    phy = float(input("Enter the marks obtained in physics "))
    chem = float(input("Enter the marks obtained in chemistry "))
    comp = float(input("Enter the marks obtained in computer "))

    # calculate the average marks
    avg = (phy + chem + comp) / 3

    # determine the grade based on the average marks
    if avg > 85:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >=45:
        grade = "C"
    else:
        grade = "D"

    # print the name, roll number and grade of the student
    print(name,"with roll no.",roll,"has got grade",grade)

grades()

