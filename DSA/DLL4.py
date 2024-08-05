class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def search(self, element):
        start = self.head
        while start:
            if start.data == element:
                return f"{element} is found in the double linked list."
            start = start.next
        return f"{element} is not found in the double linked list"

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
link.display()

store = link.search(3)
print(f"\n{store}", end='')
