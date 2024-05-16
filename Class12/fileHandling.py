file1 = open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'r')
out = file1.readlines()
# out = out[2]
# print(out)
file1.close()

file2 = open(r"C:\Users\Ritankar's PC\Desktop\test.txt", 'w')
file2.writelines(['Ritankar Pal\n','XII\n','S4\n','16'])
file2.close()

