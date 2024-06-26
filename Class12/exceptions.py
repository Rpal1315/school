import time
try:
    a = int(input("Enter a no:"))
    b = int(input("Enter another no:"))
    time.sleep(5)
    c = b/a
    print(c)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Can't divide by zero")
except KeyboardInterrupt:
    print("Okay")
    exit(code="1")
finally:
    print("Bye")