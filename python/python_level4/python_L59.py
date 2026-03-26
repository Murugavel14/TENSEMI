class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.pointer = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_to_end(self, data):
        new = node(data)
        
        if self.head is None:   #By Use not
            self.head = new
            return
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer 
            cur.pointer = new
            new.prev = cur
            
    def insert_to_start(self, data):
        new = node(data)
        
        if self.head is None:   #By Use not
            self.head = new
            return
        self.head.prev = new
        new.pointer = self.head
        self.head =  new
        
    def delete(self, data):
        if not self.head:
            print("L_List is empty")
            return
        
        if self.head.data == data:
            self.head = self.head.pointer
            if self.head:
                self.head.prev = None
            return
        
        cur = self.head
        while cur and cur.data != data:
            cur = cur.pointer
            
        if not cur:
            print(f"data {data} not found")
            return 
        print(f"data {data} found")
        
        cur.prev.pointer = cur.pointer
        cur.pointer.prev = cur.prev
        
    def display(self):
        cur = self.head
        if cur is None:         #if not cur
            print("Empty")
            return
        while cur is not None:  #if cur
            print(cur.data, end=" <=> ")
            cur = cur.pointer
        print("done")
        
def main():
    ll = linkedlist()
    for i in range(0,5):
        data1 = int(input("Enter Number: "))
        ll.insert_to_end(data1)
    ll.display()
    ll.delete(34)
    ll.insert_to_start(87)
    ll.display()
if __name__ == "__main__":
    		main()

