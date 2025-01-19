#shift words with upper case vowels to a different text file

inp = input("Enter text: ")

f1 = open("text.txt", "w")
f1.write(inp)
f1.close()

f1 = open("text.txt", "r")
f2 = open("new_text.txt", "w")

f1_out = f1.read()
f1_out_list = f1_out.split(" ")

for i in f1_out_list:
    for j in i:
        if j in ['A', 'E', 'I', 'O', 'U']:
            f2.write(i+" ")
            break

f1.close()
f2.close()

f2 = open("new_text.txt", "r")
print(f2.read())