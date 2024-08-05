class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_beginning(self):
        self.head = self.head.next
        self.tail.next = self.head

    def delete_ending(self):
        prev = self.head
        start = self.head.next
        while start.next != self.tail:
            prev = prev.next
            start = start.next
        self.tail = start
        self.tail.next = self.head

    def delete_position(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
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
link = CircularLinkedList()
link.head = n1
link.tail = n1
link.tail.next = link.head

n2 = Node(20)
link.tail.next = n2
link.tail = n2
link.tail.next = link.head

n3 = Node(25)
link.tail.next = n3
link.tail = n3
link.tail.next = link.head

n4 = Node(30)
link.tail.next = n4
link.tail = n4
link.tail.next = link.head

link.delete_beginning()
link.delete_ending()
link.delete_position(2)


link.display()