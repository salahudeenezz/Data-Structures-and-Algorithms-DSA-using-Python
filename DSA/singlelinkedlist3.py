class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next

    def search(self, element):
        start = self.head
        while start:
            if start.data == element:
                return f"{element} is found in the linked list."
            start = start.next
        return f"{element} is not found in the linked list"


node_one = Node(0)
link = SinglyLinkedList()
link.head = node_one
node_two = Node(1)
node_one.next = node_two
node_three = Node(2)
node_two.next = node_three

link.display()

store = link.search(0)
print(f"\n{store}", end='')

