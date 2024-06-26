# Access multiple lines from a file and print those lines which consists of a digit or a number as a word

f = open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'w')
inp = input("Enter the paragraph: ")
f.write(inp)
f.close()
f1= open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'r')
out = f1.read()
out_lst = out.split(".")

for i in out_lst:
    chk = i.split(" ")

    for j in chk:
        if j.isdigit():
            i = i.strip()
            print(i)

