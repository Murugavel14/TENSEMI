class node:
    def __init__(self, stud_id, math, science):  “””IN THIS FUNCTION IS REPRESENT FOR THE NODE[DATA, NEXT] “””
        self.stud_id = stud_id
        self.math    = math
        self.science = science
        self.pointer = None
class linkedlist:
    def __init__ (self):
        self.head = None
    def add(self, stud_id, math, science):
        new = node(stud_id, math, science)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = new
    def show(self):
        cur = self.head
        if cur is None:
            print("empty")
            return
        while cur is not None:
            print(f"ID: {cur.stud_id}, Maths: {cur.math}, Science:{cur.science}")
            #print("ID: {}, Maths: {}, Science: {}".format(cur.stud_id, cur.math, cur.science))
            cur = cur.pointer

def main():
    ll = linkedlist()
    while True:
        stud_id = int(input("Student ID: "))
        if stud_id == -1:
            break
        math = int(input("Math mark: "))
        science = int(input("Science mark: "))
        ll.add(stud_id, math, science)
    print("Records ------>")
    ll.show()
if __name__ == "__main__":
    main()

