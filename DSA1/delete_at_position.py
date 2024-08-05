class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL: 
    def __init__(self):
        self.head = None

    def delete_position(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            start = start.next
            prev = prev.next
        prev.next = prev.next.next
        start.next = None
    
    def display(self):
        start = self.head
        while start:
            print(start.data, '->' , end=' ')
            start = start.next

node_1 = Node(10)
link = SLL()
link.head = node_1
node_2 = Node(20)
node_1.next = node_2
n3 = Node(30)
node_2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
link.delete_position(2)
n4.next = n5
link.display()