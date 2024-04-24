inp = input("Enter the string: ")
inp = inp.lower()
chk = inp.split()
out = {}
for i in chk:
    if i in out:
        out[i] = out[i] + 1
    else:
        out[i] = 1

print(out)
