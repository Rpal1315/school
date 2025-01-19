R = {"OM":76,"JAI":45,"BOB":89,"ALI":65,"ANU":90,"TOM":82}

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

stack = []

for i in R:
    push(stack,i)

while stack != []:
    print(pop(stack))