class Node: #node class, this class for one student
    def __init__(self,ide,mat,sci):#self is current object. constructor (runs automatically when object is created).id,mat,sci are input values
        self.ide=ide #storing student details into the object   
        self.mat=mat
        self.sci=sci
        self.next=None #Every node has a pointer called next.initially None,it is not connected to anything yet.
class LinkedList: #class it manage entire list, this class for manage all students
    def __init__(self): #constructor
        self.head=None #head stores adress of first node, initially head is empty so None
    def insert(ide,mat,sci): #add new student to the list
        new_node=(ide,mat,sci) #new Node, it create one student list in one objectx
        if self.head is None:
            self.head=new_node #make new node as a first node now that address is stored in the self.head
        else:
            temp=self.head
            while temp.next is not None: #move until last node
                temp=temp.next
            temp.next=new_node #connect last node to new node
                
    def display(self): # used to print all student details
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head #start from first node
        while temp is not None: #traverse untill end of the list
            print("ID:",temp.ide) #print student details
            print("Maths mark:",temp.mat)
            print("Science mark:",temp.sci)
            temp=temp.next #move to next node
llist=LinkedList() #linked list object, automatically calls __init()__(self)
#llist.insert(ide,mat,sci)
#llist.display()
while True:#infinite loop to take input
    ide=int(input("id:"))
    if(ide==-1):
        #print("Enter valid id")
        break
    name=input("Name:")
    math=int(input("Maths:"))
    sci=int(input("Science:"))
    llist.insert(ide,name,math,sci) #for to add student
llist.display() #after stop print all student details
