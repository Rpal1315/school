units = 300
res = 0
if units > 300:
    res = 1300 + 9 * (units - 300)
elif 300 >= units > 200:
    res = 550 + 7.5 * (units - 200)
elif 200 >= units > 100:
    res = 200 + 3.5 * (units - 100)
elif 100 >= units:
    res = 2 * units

print(res)
