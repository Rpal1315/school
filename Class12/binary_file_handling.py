import pickle

f1 = open("emp.dat", "wb")
ans = 'y'

while ans == 'y':
    emp_id = int(input("Enter employee id: "))
    emp_name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    pickle.dump([emp_id, emp_name, salary], f1)
        
    ans = input("Do you want to continue?(y/n)")


f1.close()


f2 = open("emp.dat", "rb")
f3 = open("emp1.dat", "wb")
while True:
    try:
        data = pickle.load(f2)
        if 20000 <= data[2] <= 30000 and str(data[1].lower()).count("a") > 1:
            pickle.dump([data[0],data[2]], f3)
    except EOFError:
        f2.close()
        f3.close()
        break  

# Displaying the contents of emp1.dat
