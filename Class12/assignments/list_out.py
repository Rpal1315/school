# Write a function that displays those names which end with A
def name_check(names):
    for name in names:
        name = name.upper()
        if name[-1] == "A":
            print(name)

names = ["Maria", "John", "Jessica", "Roberta"]

name_check(names)