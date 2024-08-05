class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def delete_beginning(self):
        self.head = self.head.next
        self.tail.next = self.head
    
    def delete_ending(self):
        start = self.head
        while start.next != self.tail:
            start = start.next
        self.tail = start
        self.tail.next = self.head

    def delete_position_from_beginning(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            prev = prev.next
            start = start.next
        prev.next = start.next
        start.next = None
    
    def delete_position_from_end(self, pos):
        prev = self.tail
        start = self.tail.next
        for i in range(pos):
            prev = prev.next
            start = start.next
        prev.next = start.next
        start.next = None
    


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

n3 = Node(30)
link.tail.next = n3
link.tail = n3
link.tail.next = link.head

n4 = Node(40)
link.tail.next = n4
link.tail = n4
link.tail.next = link.head

n5 = Node(50)
link.tail.next = n5
link.tail = n5
link.tail.next = link.head

n6 = Node(60)
link.tail.next = n6
link.tail = n6
link.tail.next = link.head

link.delete_beginning()
link.delete_ending()
link.delete_position_from_beginning(2)
link.delete_position_from_end(1)

link.display()
        