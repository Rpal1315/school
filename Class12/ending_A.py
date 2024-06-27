def ending_A(names):
    for name in names:
        name = name.upper()
        if name[-1] == "A":
            print(name)


names = ["Maria", "John", "Jessica", "Roberta"]

ending_A(names)
