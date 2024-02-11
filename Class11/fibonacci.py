# 0 1 1 2 3 5
import csv
import time

counter = 0
filename = "fibonacciRunTime.csv"
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(["counter", "time_diff"])

for j in range(0, 1):
    # record start time

    start = time.perf_counter()
    till = 100
    buffer1 = 0
    buffer2 = 1
    for i in range(0, till):
        res = buffer1 + buffer2
        print(res)
        buffer1 = buffer2
        buffer2 = res
    # record end time
    end = time.perf_counter()

    # print the difference between start
    # and end time in milli. secs
    time_diff = (end - start)
    print(time_diff * (10 ** 9))

    # writing to csv file
    # with open(filename, 'a+') as csvfile:
    #     # creating a csv writer object
    #     csvwriter = csv.writer(csvfile)
    #
    #     # writing the fields
    #     csvwriter.writerow([j,time_diff])
    #
