class node:
    def __init__(self, data):
        self.data    = data
        self.pointer = None

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = new

    def delete(self, data):
        if(self.head is not None):
            if(self.head.data == data):
                self.head = self.head.pointer
            else:
                cur = self.head
                while ((cur.pointer is not None) and (cur.pointer.data != data)):
                    cur = cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
        else:
            Print("Node is empty")

    def display(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data)
            cur = cur.pointer
        print("Done")
def main():
    ll = linkedlist()
    for i in range(0,5):
        data1 = int(input("Enter Number: "))
        ll.insert(data1)
    ll.display()
    dele = int(input("Enter remove: "))
    ll.delete(dele)
    ll.display()
if __name__ == "__main__":
    main()
