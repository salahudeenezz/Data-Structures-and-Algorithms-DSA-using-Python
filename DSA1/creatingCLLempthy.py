class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_beginning(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
            self.tail = nb
            self.tail.next = self.head
        else:
            nb.next = self.head
            self.head = nb
            self.tail.next = self.head
    
    def insert_ending(self, data):
        ne = Node(data)
        self.tail.next = ne
        self.tail = ne
        self.tail.next = self.head
    
    def insert_at_postion_from_head(self, pos, data):
        np = Node(data)
        start = self.head
        for i in range(pos-1):
            start = start.next
        np.next = start.next
        start.next = np
    
    def insert_at_position_from_tail(self, pos, data):
        np2 = Node(data)
        start = self.tail
        for i in range(pos):
            start = start.next
        np2.next = start.next
        start.next = np2
        
    def display(self):
        start = self.head
        print(start.data, '->', end=' ')
        while start.next != self.head:
            start = start.next
            print(start.data, '->', end=' ')
        print(start.next.data)
       
     def search(self, element):
        start = self.head
        while True:
            if start.data == element:
                return start
            start = start.next
            if start == self.head:
                break
        return None
    
    def search2(self, element):
        start = self.tail
        while True:
            if start.data == element:
                return start
            start = start.next
            if start == self.tail:
                break
        return None


link = CLL()
link.insert_beginning(10)
link.insert_beginning(30)
link.insert_beginning(0)
link.insert_ending(5)
link.insert_ending(6)
link.insert_at_postion_from_head(2, 4)
link.insert_at_position_from_tail(2, 1)
link.display()
store = link.search(40)
print("\n")
if store is not None:
    print(f"{store.data} is found in the CLL.")
else:
    print(store)

store2 = link.search2(30)
print("\n")
if store2 is not None:
    print(f"{store2.data} is found in the CLL.")
else:
    print(store2)