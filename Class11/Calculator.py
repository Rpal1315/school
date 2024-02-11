try:
    num1 = int(input("Enter the 1st no: "))
    num2 = int(input("Enter the 2nd no: "))

except ValueError:
    print("Invalid Data Type was entered. Enter a no.")
    exit(1)

choice = input("Enter the operator(+,-,*,/)")

if choice == "+":
    res = num1 + num2
elif choice == "-":
    res = num1 - num2
elif choice == "*":
    res = num1 * num2
elif choice == "/":
    try:
        res = num1 / num2
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
        exit(1)

print(res)
