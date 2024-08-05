class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def delete_beginning(self):
        start = self.head
        self.head = start.next
        start.next.prev = None
        start.next = None

    def delete_ending(self):
        prev = self.head
        start = self.head.next
        while start.next:
            start = start.next
            prev = prev.next
        start.prev = None
        prev.next = None

    def delete_position(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            start = start.next
            prev = prev.next
        prev.next = start.next
        start.prev = None
        start.next = None

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next


node_one = Node(0)
link = DoubleLinkedList()
link.head = node_one
node_two = Node(1)
node_two.prev = node_one
node_one.next = node_two
node_three = Node(2)
node_three.prev = node_two
node_two.next = node_three
node_four = Node(3)
node_four.prev = node_three
node_three.next = node_four

link.delete_beginning()

link.delete_ending()

link.delete_position(1)

link.display()
'''start = self.head
self.head = start.next
start.next = None
self.head.prev = None'''