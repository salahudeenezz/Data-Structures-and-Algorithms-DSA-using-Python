class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def display_ending(self, data):
        ne = Node(data)
        start = self.head
        while start.next:
            start = start.next
        start.next = ne

    def displaying_position(self, pos, data):
        nd = Node(data)
        start = self.head
        for i in range(pos - 1):
            start = start.next
        nd.next = start.next
        start.next = nd

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next


link = SingleLinkedList()
node1 = Node(10)
link.head = node1
node2 = Node(20)
node1.next = node2

link.display_beginning(1)
link.display_ending(90)
link.displaying_position(2, 5)

link.display()

