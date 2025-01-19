exp = input("Enter the expression: ")

stack = []

for i in exp:
    if i.isalnum():
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            stack.append(b + a)
        elif i == "-":
            stack.append(b - a)
        elif i == "*":
            stack.append(b * a)
        elif i == "/":
            stack.append(b / a)

print(stack.pop())

