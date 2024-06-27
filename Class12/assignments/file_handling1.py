# Access multiple lines from a file and print those lines which consists of a digit or a number as a word

f = open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'w')
inp = input("Enter the paragraph: ")
inp_list = inp.split(".")
for i in inp_list:
    f.write(i+"\n")
f.close()
f1= open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'r')
out = f1.readlines()

for i in out:
    for j in i:
        if j.isdigit():
            print(i)
            break
