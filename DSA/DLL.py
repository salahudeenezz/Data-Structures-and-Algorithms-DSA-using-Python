class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

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

link.display()
