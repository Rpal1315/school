try:
    a = int(input("Enter a no:"))
    b = int(input("Enter another no:"))
    c = b/a
except ValueError:
    print("Invalid input")
finally:
    print("Bye")