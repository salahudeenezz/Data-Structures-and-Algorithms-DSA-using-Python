class Node:
    def __init__(self, data : int):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_position(self, data, pos):
        node_position = Node(data)
        prev = self.tail
        start = self.tail.prev
        for i in range(pos-1):
            prev = prev.prev
            start = start.prev
        prev.prev = node_position
        start.next = node_position
        node_position.prev = start
        node_position.next = prev

    def display(self):
        start = self.head
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.next
    
    def display1(self):
        start = self.tail
        print('\n')
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.prev
            

n1 = Node(10)
link = DLL()
link.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
link.tail = n2
n3 = Node(30)
n2.next = n3
n3.prev = n2
link.tail = n3
n4 = Node(40)
n3.next = n4
n4.prev = n3
link.tail = n4
link.insert_at_position(25, 2)

link.display()
link.display1()