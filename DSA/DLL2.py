class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node_beginning = Node(data)
        start = self.head
        start.prev = node_beginning
        node_beginning.next = start
        self.head = node_beginning

    def insert_end(self, data):
        node_end = Node(data)
        start = self.head
        while start.next:
            start = start.next

        start.next = node_end
        node_end.prev = node_two

    def insert_position(self, pos, data):
        node_position = Node(data)
        start = self.head
        for i in range(pos-1):
            start = start.next
        node_position.prev = start
        node_position.next = start.next
        start.next.prev = node_position
        start.next = node_position

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next


node_one = Node(1)
link = DoubleLinkedList()
link.head = node_one
node_two = Node(2)
node_two.prev = node_one
node_one.next = node_two

link.insert_start(0)

link.insert_end(3)

link.insert_position(2, 4)

link.display()
