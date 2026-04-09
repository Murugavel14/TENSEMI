class node:
    def __init__(self, data):	#NODE CREATION
        self.data    = data
        self.pointer = None
class linkedlist:
    def __init__(self):		#DECLARE HEAD
        self.head = None
    def insert(self, data):		#DEFINE INSERT FUNCTION
        new = node(data)
        if self.head is None:		#HEAD -> NEW (ASSIGN)
            self.head = new
        else:
            cur = self.head		#HEAD ->  CUR NODE
            while cur.pointer is not None:    # IF CUR.POINTER IS !_NONE [LOOP]
                cur = cur.pointer		# TRUE -> THEN ASSIGN NEXT DATA POINTER
            cur.pointer = new		#CUR.POINTER IS NONE -> THEN ASSIGN NEW
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
if __name__ == "__main__":
    main()

