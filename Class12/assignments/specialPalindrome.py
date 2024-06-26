# Find out is a no. is a special palindrome or not
num_list = eval(input("Enter the list: "))
out_list = []
for num in num_list:
    num_str = str(num)
    counter = 0
    chkID = (len(num_str) // 2)
    for i in range(0, len(num_str)):
        for j in range(i + 1, len(num_str)):
            if num_str[i] == num_str[j]:
                counter += 1

    if counter == chkID:
        out_list.append(num)


print(out_list)