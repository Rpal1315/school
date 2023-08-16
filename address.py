# Calculate the side on  which the house is present
add = int(input("Enter the house no.: "))

if add in range(1,100,2):
    print("East MG")
elif add in range(2,101,2):
    print("West MG")