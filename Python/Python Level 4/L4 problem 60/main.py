class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None


    # Push operation
    def push(self, data):

        newnode = Node(data)

        newnode.next = self.top
        self.top = newnode

        print(data, "pushed into stack")


    # Pop operation
    def pop(self):

        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        self.top = self.top.next

        print("Popped Data:", temp.data)


    # Display stack
    def display(self):

        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top

        print("Stack (Top → Bottom):")

        while temp:
            print(temp.data)
            temp = temp.next


def main():

    stack = Stack()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = int(input("Enter value: "))
            stack.push(value)

        elif choice == 2:

            stack.pop()

        elif choice == 3:

            stack.display()

        elif choice == 4:

            print("Exiting program")
            break

        else:

            print("Invalid choice")


main()