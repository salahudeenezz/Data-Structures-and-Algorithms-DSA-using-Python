class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, element):
        start = self.head
        while True:
            if start.data == element:
                return True
            start = start.next
            if start == self.head:
                break
        return False

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


link.display()

store = link.search(10)
print(f"{store}", end='')