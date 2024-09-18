import pickle

inp = input("Enter a paragraph: ")
f = open("text.dat", "wb")
inp_list = inp.split(".")
pickle.dump(inp_list, f)

f.close()


f1 = open("text.dat", "rb")

o_list = pickle.load(f1)

max_len = 0
max_index = 0


for i in range(0, len(o_list)):
    for j in o_list[i].split(" "):
        if len(j) > max_len:
            max_len = len(j)
            max_index = i

print(o_list[max_index])