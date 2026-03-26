class Node: #node class for one student
    def __init__(self,data):
        self.data=data
        self.prev=None 
        self.next=None 
class doublylinkedlist:#linkedlist structure to manage all data 
    def __init__(self):
        self.head=None #head stores first node of the list address 
    #Insert 
    def insert_entry(self):#function to insert new node
        new_id=int(input("Enter new Id:"))#user enter new id
        new_node=Node(new_id)#create new node 
        
        if self.head is None:
            self.head=new_node #If no nodes exist, the new node becomes head
            return 
        given_id=int(input("Enter existing id:"))#choose the node for insert
        position=input("insert before or after(b/a) ")#choose insertion position
        temp=self.head  
        while temp:
            if temp.data==given_id:
                if position=='b': #insert before
                    new_node.next=temp
                    new_node.prev=temp.prev 
                    if temp.prev:
                        temp.prev.next=new_node 
                    else:
                        self.head=new_node 
                    temp.prev=new_node
                    
                elif position=='a':
                    new_node.prev=temp
                    new_node.next=temp.next 
                    if temp.next:
                        temp.next.prev=new_node 
                    temp.next=new_node 
                return 
            temp=temp.next 
        print("id not found")
    #delete entry 
    def delete_entry(self):
        delete_id=int(input("Enter the ID to delete:"))#user give id
        temp=self.head #traverse
        while temp:
            if temp.data==delete_id:
                if temp.prev:
                    temp.prev.next=temp.next 
                else:
                    self.head=temp.next 
                if temp.next: 
                    temp.next.prev=temp.prev 
                print("Node deleted") 
                return 
            temp=temp.next 
        print("Id not found")
    #display list 
    def display_list(self): #for print list function
        temp=self.head  #start from head
        if temp is None:
            print("list is empty")
            return
        while temp:
            print(temp.data, end="<->")
            temp=temp.next 
        print("NULL")
def main():
    dll=doublylinkedlist()
    for i in range(5):
        value=int(input("Enter initial Id:"))
        node=Node(value) #create node
        
        if dll.head is None:
            dll.head=node 
        else:
            temp=dll.head 
            while temp.next:
                temp=temp.next
            temp.next=node 
            temp.prev=temp
            
            while True:
                print("1.Insert entry:")
                print("2.Delete entry:")
                print("3.Display List:")
                print("4.Exit")
                choice=int(input("Enter the choice:"))
                if(choice==1):
                    dll.insert_entry() 
                elif choice==2:
                    dll.delete_entry() 
                elif choice==3:
                    dll.display_list() 
                elif choice==4:
                    break 
                else:
                    print("Invalid choice")
if __name__ == "__main__":
    main()

        