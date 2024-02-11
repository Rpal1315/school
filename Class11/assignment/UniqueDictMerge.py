dict1 = eval(input("Enter the 1st dictionary"))
dict2 = eval(input("Enter the 2nd dictionary"))
out = {}
for i in dict1:
    if i not in out:
        out[i] = dict1[i]

for j in dict2:
    if j not in out:
        out[j] = dict2[j]

print(out)
