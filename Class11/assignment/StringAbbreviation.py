# Abbreviate a string
inp = input("Enter the name: ")

l1 = inp.split(" ")
out = ""

for i in l1:
    a = i[0].capitalize()
    out += a

print(out)