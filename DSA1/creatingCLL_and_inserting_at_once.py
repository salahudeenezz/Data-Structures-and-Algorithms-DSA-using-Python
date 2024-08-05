class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
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
    
    def insert_at_ending(self, data):
        ne = Node(data)
        self.tail.next = ne
        self.tail = ne
        self.tail.next = self.head
    
    def display(self):
        start = self.head
        print(start.data, '->', end=' ')
        while start.next != self.head:
            start = start.next
            print(start.data, '->', end=' ')
        print(start.next.data)



n1 = Node(10)
link = CLL()
link.head = n1
link.tail = n1
link.tail.next = link.head

n2 = Node(20)
link.tail.next = n2
link.tail = n2
link.tail.next = link.head

link.insert_at_beginning(30)
link.insert_at_ending(40)
link.insert_at_postion_from_head(2, 1)
link.insert_at_position_from_tail(2, 0)
link.display()
        