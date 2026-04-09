# Node class represents each student record
class Node:

    def __init__(self, student_id, maths_mark, science_mark):
        self.student_id = student_id      # store student id
        self.maths_mark = maths_mark      # store maths mark
        self.science_mark = science_mark  # store science mark
        self.next = None                  # pointer to next node


# LinkedList class manages the list
class LinkedList:

    def __init__(self):
        self.head = None      # head pointer


    # create 5 sample entries
    def create_sample(self):

        data = [
            (101, 80, 75),
            (102, 85, 90),
            (103, 70, 65),
            (104, 88, 92),
            (105, 60, 72)
        ]

        for d in data:
            self.insert_end(d[0], d[1], d[2])


    # insert node at the end
    def insert_end(self, student_id, maths_mark, science_mark):

        new_node = Node(student_id, maths_mark, science_mark)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # insert after a given id
    def insert_after(self, target_id, student_id, maths_mark, science_mark):

        temp = self.head

        while temp:

            if temp.student_id == target_id:

                new_node = Node(student_id, maths_mark, science_mark)

                new_node.next = temp.next
                temp.next = new_node

                print("Inserted after ID", target_id)
                return

            temp = temp.next

        print("ID not found")


    # insert before a given id
    def insert_before(self, target_id, student_id, maths_mark, science_mark):

        if self.head is None:
            return

        # if inserting before first node
        if self.head.student_id == target_id:

            new_node = Node(student_id, maths_mark, science_mark)

            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        temp = self.head

        while temp and temp.student_id != target_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("ID not found")
            return

        new_node = Node(student_id, maths_mark, science_mark)

        prev.next = new_node
        new_node.next = temp


    # delete node by id
    def delete(self, target_id):

        if self.head is None:
            print("List empty")
            return

        # if head node must be deleted
        if self.head.student_id == target_id:

            self.head = self.head.next
            print("Deleted ID", target_id)
            return

        prev = None
        temp = self.head

        while temp and temp.student_id != target_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("ID not found")
            return

        prev.next = temp.next
        print("Deleted ID", target_id)


    # display list
    def display(self):

        temp = self.head

        if temp is None:
            print("List Empty")
            return

        print("\nStudent Records")
        print("ID\tMaths\tScience")

        while temp:
            print(temp.student_id, "\t", temp.maths_mark, "\t", temp.science_mark)
            temp = temp.next


# main program
def main():

    ll = LinkedList()

    ll.create_sample()   # create 5 sample entries

    while True:

        print("1. Insert Entry")
        print("2. Delete Entry")
        print("3. Display List")
        print("4. Exit")

        choice = int(input("Enter choice: "))


        if choice == 1:

            student_id = int(input("Enter new Student ID: "))
            maths = int(input("Enter Maths mark: "))
            science = int(input("Enter Science mark: "))

            pos = input("Insert before or after ID (b/a): ")

            target = int(input("Enter target ID: "))

            if pos == 'a':
                ll.insert_after(target, student_id, maths, science)

            elif pos == 'b':
                ll.insert_before(target, student_id, maths, science)

            else:
                print("Invalid option")


        elif choice == 2:

            target = int(input("Enter ID to delete: "))

            ll.delete(target)


        elif choice == 3:

            ll.display()


        elif choice == 4:

            print("Program Ended")
            break


        else:

            print("Invalid choice")


main()