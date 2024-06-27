inp = input("Enter a paragraph: ")

f = open(r"C:\Users\Ritankar's PC\Desktop\a1.txt", 'w')
f.write(inp)
f.close()

f1 = open(r"C:\Users\Ritankar's PC\Desktop\a1.txt", 'r')
f2 = open(r"C:\Users\Ritankar's PC\Desktop\a2.txt", 'w')
out = f1.read()
out_list = out.split()
for i in out_list:
    print(i)
    if i[0] in ['A', 'E', 'I', 'O', 'U']:
        f2.write(i+" ")

f1.close()

