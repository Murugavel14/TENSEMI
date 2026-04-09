# Node class for Doubly Linked List
class Node:

    def __init__(self, student_id, maths_mark, science_mark):
        self.student_id = student_id
        self.maths_mark = maths_mark
        self.science_mark = science_mark

        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    # create sample list
    def create_sample(self):

        data = [
            (101,80,75),
            (102,85,90),
            (103,70,65),
            (104,88,92),
            (105,60,72)
        ]

        for d in data:
            self.insert_end(d[0],d[1],d[2])


    # insert at end
    def insert_end(self, student_id, maths, science):

        new_node = Node(student_id, maths, science)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    # insert after ID
    def insert_after(self, target_id, student_id, maths, science):

        temp = self.head

        while temp:

            if temp.student_id == target_id: #after 103 we going to update 

                new_node = Node(student_id, maths, science) # (newnode)

                new_node.next = temp.next   #103 next is 104 so newnode next is (104 == temp next)
                new_node.prev = temp        # 

                if temp.next: 
                    temp.next.prev = new_node

                temp.next = new_node

                print("Inserted after", target_id)
                return

            temp = temp.next

        print("ID not found")


    # insert before ID
    def insert_before(self, target_id, student_id, maths, science):

        temp = self.head

        while temp:

            if temp.student_id == target_id:

                new_node = Node(student_id, maths, science)

                new_node.next = temp
                new_node.prev = temp.prev

                if temp.prev:
                    temp.prev.next = new_node
                else:
                    self.head = new_node

                temp.prev = new_node

                print("Inserted before", target_id)
                return

            temp = temp.next

        print("ID not found")


    # delete node
    def delete(self, target_id):

        temp = self.head

        while temp:

            if temp.student_id == target_id:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print("Deleted ID", target_id)
                return

            temp = temp.next

        print("ID not found")


    # display list
    def display(self):

        temp = self.head

        if temp is None:
            print("List Empty")
            return

        print("\nStudent Records")
        print("ID\tMaths\tScience")

        while temp:
            print(temp.student_id,"\t",temp.maths_mark,"\t",temp.science_mark)
            temp = temp.next



def main():

    dll = DoublyLinkedList()

    dll.create_sample()

    while True:

        print("\n1. Insert Entry")
        print("2. Delete Entry")
        print("3. Display List")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            sid = int(input("Enter new student ID: "))
            maths = int(input("Enter maths mark: "))
            science = int(input("Enter science mark: "))

            pos = input("Insert before or after (b/a): ")

            target = int(input("Enter target ID: "))

            if pos == 'a':
                dll.insert_after(target,sid,maths,science)

            else:
                dll.insert_before(target,sid,maths,science)


        elif choice == 2:

            target = int(input("Enter ID to delete: "))
            dll.delete(target)


        elif choice == 3:

            dll.display()


        elif choice == 4:

            print("Program Ended")
            break


main()