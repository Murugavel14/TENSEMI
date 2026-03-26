#Python Level 4 | Problem 58
class Node: #node class for one student
    def _init_(self,ide,name,math,sci): #constructor for to automatically calls the current object when object created
        self.ide=ide #store the datas into the object
        self.name=name
        self.math=math
        self.sci=sci 
        self.next=None
class LinkedList: #this class for to manage the all student details
    def _init_(self):
        self.head=None #initially the head node is none
  
    def insert(self,ide,name,math,sci): #insert the sudent list as a new node
        new_node=Node(ide,name,math,sci) #create a new node
        if self.head is None:
            self.head=new_node 
        else:
            temp=self.head #the first node is stored in the temp. variablex
            while temp.next is not None: #run until the last node
                temp=temp.next
            temp.next=new_node
    def insert_after(self,given_id,ide,name,math,sci): #function for to insert after that target id
        temp=self.head #initially the head value is stored in the temp. variable
        while temp is not None:
            if temp.ide==given_id:
                new_node=Node(ide,name,math,sci)
                
                new_node.next=temp.next
                temp.next=new_node
                print("Inserted successfully")
                return 
            temp=temp.next
        print("id not found")
    def insert_before(self,given_id,ide,name,math,sci):#before insert function
        new_node=Node(ide,name,math,sci) #create the new node
        if self.head is None:
            print("List is empty")
            return 
        if self.head.ide==given_id:
            new_node.next=self.head 
            self.head=new_node 
            return 
        prev=None 
        temp=self.head
        while temp is not None:
            if temp.ide==given_id:
                prev.next=new_node 
                new_node.next=temp 
                return 
            prev=temp
            temp=temp.next 
        print("id not found")
        
    def delete(self,given_id):
        if self.head is None:
            print("list is empty") 
            return 
        if self.head.ide==given_id:
            self.head=self.head.next 
            print("node deleted")
            return 
        prev=None 
        temp=self.head 
        while temp is not None:
            if temp.ide==given_id:
                prev.next=temp.next 
                print("node deleted")
                return 
            prev=temp
            temp=temp.next
        print("Id not found")
            
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp is not None:
            print("ID:",temp.ide)
            print("Name:",temp.name)
            print("Maths:",temp.math)
            print("Science:",temp.sci)
            temp=temp.next 
Ll=LinkedList()
Ll.insert(1,"subash",23,43)
Ll.insert(2,"suthan",87,56)
Ll.insert(3,"raj",98,90)
Ll.insert(4,"ram",97,24)
Ll.insert(5,"karim",78,13)
Ll.display()
Ll.insert_after(3,6,"kumar",54,98)
Ll.display()
Ll.insert_before(5,7,"navin",85,98)
Ll.display() 
Ll.delete(3)
Ll.display()