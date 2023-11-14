# Find an element in a list
l1 = eval(input("Enter the list: "))
e = input("Enter the element to search for: ")

for i in range(0,len(l1)):
    if str(e) == str(l1[i]):
        print(f"{e} found at index {i}")
        break

else:
    print("Element not found")