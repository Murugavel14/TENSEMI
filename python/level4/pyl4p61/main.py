# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class
class Queue:

    def __init__(self):
        self.top = None   # front of queue


    # Add operation (insert at top)
    def add(self, data):

        newnode = Node(data)

        if self.top is None:
            self.top = newnode
            return

        temp = self.top

        while temp.next:
            temp = temp.next

        temp.next = newnode

        print(data, "added to queue")


    def remove(self):
        if self.top is None:
            print("Queue empty")
            return

        temp = self.top
        self.top = self.top.next

        print("Removed:", temp.data)


    # Display queue
    def display(self):

        if self.top is None:
            print("Queue is empty")
            return

        temp = self.top

        print("Queue (Top → Bottom):")

        while temp:
            print(temp.data)
            temp = temp.next


# Main menu
def main():

    q = Queue()

    while True:

        print("\n1. Add")
        print("2. Remove")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = int(input("Enter value: "))
            q.add(value)

        elif choice == 2:

            q.remove()

        elif choice == 3:

            q.display()

        elif choice == 4:

            print("Exiting program")
            break

        else:

            print("Invalid choice")


main()