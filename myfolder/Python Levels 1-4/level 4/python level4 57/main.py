# Node class represents one student record in the linked list
class Node:

    # constructor that runs when a new node is created
    def __init__(self, student_id, maths_mark, science_mark):

        self.student_id = student_id      # store student ID
        self.maths_mark = maths_mark      # store maths mark
        self.science_mark = science_mark  # store science mark
        self.next = None                  # pointer to the next node (initially empty)



# LinkedList class manages the entire list
class LinkedList:

    # constructor that runs when LinkedList object is created
    def __init__(self):
        self.head = None   # head pointer that points to the first node



    # function to create 5 sample entries
    def create_sample(self):

        # sample data stored as tuples (id, maths, science)
        data = [
            (101, 80, 75),
            (102, 85, 90),
            (103, 70, 65),
            (104, 88, 92),
            (105, 60, 72)
        ]

        # loop through each tuple and insert it into the linked list
        for d in data:
            self.insert_end(d[0], d[1], d[2])



    # function to insert a node at the end of the list
    def insert_end(self, student_id, maths_mark, science_mark):

        new_node = Node(student_id, maths_mark, science_mark)  
        # create a new node with given student data

        if self.head is None:     # if list is empty
            self.head = new_node  # make the new node the head
            return

        temp = self.head          # start from the first node

        while temp.next:          # move until the last node
            temp = temp.next

        temp.next = new_node      # attach the new node at the end



    # function to insert a node AFTER a given ID
    def insert_after(self, target_id, student_id, maths_mark, science_mark):

        temp = self.head   # start from first node

        while temp:        # traverse the list

            if temp.student_id == target_id:   # check if current node has target ID

                new_node = Node(student_id, maths_mark, science_mark)  
                # create new node

                new_node.next = temp.next      # connect new node to next node
               temp.next = new_node           # connect current node to new node

                print("Inserted after ID", target_id)
                return

            temp = temp.next   # move to next node

        print("Target ID not found")   # if ID not present



    # function to insert BEFORE a given ID
    def insert_before(self, target_id, student_id, maths_mark, science_mark):

        if self.head is None:  # if list is empty
            return

        # if the target node is the first node
        if self.head.student_id == target_id:

            new_node = Node(student_id, maths_mark, science_mark)
            new_node.next = self.head  # point new node to current head
            self.head = new_node       # make new node the head
            return


        prev = None          # previous node pointer
        temp = self.head     # start from head

        # traverse until target ID is found
        while temp and temp.student_id != target_id:
            prev = temp
            temp = temp.next

        if temp is None:     # if ID not found
            print("Target ID not found")
            return

        new_node = Node(student_id, maths_mark, science_mark)  

        prev.next = new_node   # previous node points to new node
        new_node.next = temp   # new node points to target node



    # function to display all student records
    def display(self):

        temp = self.head   # start traversal from head

        if temp is None:   # check if list is empty
            print("List is empty")
            return

        print("\nStudent Records")
        print("ID\tMaths\tScience")

        while temp:   # traverse until the end of the list

            print(temp.student_id, "\t", temp.maths_mark, "\t", temp.science_mark)
            # print student information

            temp = temp.next   # move to next node



# main function where program execution starts
def main():

    ll = LinkedList()    # create linked list object

    ll.create_sample()   # create 5 sample nodes


    # infinite loop to display menu repeatedly
    while True:

        print("\n===== MENU =====")
        print("1. Insert Entry")
        print("2. Display List")
        print("3. Exit")

        choice = input("Enter your choice: ")   # take menu input


        if choice == '1':   # if user chooses insert

            student_id = int(input("Enter new Student ID: "))
            maths = int(input("Enter Maths mark: "))
            science = int(input("Enter Science mark: "))

            pos = input("Insert Before or After target ID (b/a): ")
            target = int(input("Enter target ID: "))

            if pos.lower() == 'a':   # insert after
                ll.insert_after(target, student_id, maths, science)

            elif pos.lower() == 'b':  # insert before
                ll.insert_before(target, student_id, maths, science)

            else:
                print("Invalid option")


        elif choice == '2':   # display linked list
            ll.display()


        elif choice == '3':   # exit program
            print("Program terminated.")
            break


        else:
            print("Invalid choice")


# ensures the program runs only when executed directly
if __name__ == "__main__":
    main()