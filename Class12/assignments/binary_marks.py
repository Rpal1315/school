# Create a binary file with roll no., name, marks in the form of a dictionary. Display those names who scored more than 85 marks
import pickle

ent_no = int(input("Enter the number of students: "))
o_list = []


f = open("marks.dat", "wb")

for i in range(0, ent_no):
    o_dict = {}
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))

    o_dict["roll"] = roll
    o_dict["name"] = name
    o_dict["marks"] = marks

    o_list.append(o_dict)


pickle.dump(o_list, f)

f.close()


f1 = open("marks.dat", "rb")

o_dict = pickle.load(f1)

for i in o_dict:
    if i["marks"] > 85:
        print(i["name"])

f1.close()
