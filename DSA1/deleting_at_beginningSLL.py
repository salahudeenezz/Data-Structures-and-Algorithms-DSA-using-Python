class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL: 
    def __init__(self):
        self.head = None
    
    def delete_beginning(self):
        self.head = self.head.nex
    
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
node_3 = Node(30)
node_2.next = node_3

link.delete_beginning()

link.display()