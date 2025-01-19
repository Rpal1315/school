# Stack Implementation
def push(stack, item):
    stack.append(item)
    top = len(stack) - 1

def pop(stack):
    if stack == []:
        print("Stack Underflow")
        top = None
    else:
        item = stack.pop()
        if len(stack) == 0:
            top = None
        else:
            top = len(stack) - 1
            print("Deleted element")

def display(stack):
    if stack == []:
        print("Stack Empty")
    else:
        top = len(stack) - 1
        for i in range(top, -1, -1):
            print(stack[i])

stack = []
top = None


while True:
    print("----------------------")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    print("----------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the element: ")
        push(stack, item)

    elif choice == 2:
        pop(stack)

    elif choice == 3:
        print("----------------------")
        display(stack)
        print("----------------------")

    elif choice == 4:
        break