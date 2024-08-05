class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL: 
    def __init__(self):
        self.head = None
    
    def insert_beginning(self, data):
        beginning_node = Node(data)
        beginning_node.next = self.head
        self.head = beginning_node
    
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

link.insert_beginning(5)
link.insert_beginning(0)

link.display()