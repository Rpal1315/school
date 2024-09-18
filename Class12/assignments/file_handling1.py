"""
File Handling Script

This script reads a paragraph from the user, splits it into sentences, and writes each sentence to a file.
It then reads the file and prints out any lines that contain digits.

Usage:
    python file_handling1.py
"""
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
