class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def delete_beginning(self):
        start = self.head
        self.head = start.next
        start.next = None

    def delete_ending(self):
        prev = self.head
        start = self.head.next
        while start.next:
            start = start.next
            prev = prev.next
        prev.next = None

    def delete_position(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            start = start.next
            prev = prev.next
        prev.next = start.next

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next


node_one = Node(1)
link = SinglyLinkedList()
link.head = node_one
node_two = Node(2)
node_one.next = node_two
node_three = Node(3)
node_two.next = node_three
node_four = Node(4)
node_three.next = node_four
link.delete_beginning()
link.delete_ending()
link.delete_position(2)
link.display()