# Convert a given infix expression to postfix expression

infix = input("Enter Infix Expression: ")
stack = []
precedence = [ "^",'*', '/', '+', '-' ]

for i in infix:
    if i.isalnum():
        print(i, end='')
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        while stack and stack[-1] != '(' and precedence.index(i) <= precedence.index(stack[-1]):
            print(stack.pop(), end='')
        stack.append(i)

while stack:
    print(stack.pop(), end='')
