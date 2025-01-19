import csv


def Min_Fee():
    f = open("Professionals.csv", "r")
    reader = csv.reader(f)
    next(reader)
    vmin = 10000000
    for i in reader:
        if int(i[3]) < vmin:
            vmin = int(i[3])
            rec = i
    print("Lowest Fee Course: ", rec)
    print("Lowest Fee: ", vmin)


Min_Fee()
    