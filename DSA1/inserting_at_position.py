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
    
    def inserting_ending(self, data):
        ending_node = Node(data)
        start = self.head
        while start.next:
            start = start.next
        start.next = ending_node

    def insert_at_position(self, data, pos):
        node_position = Node(data)
        start = self.head
        for i in range(pos-1):
            start = start.next
        node_position.next = start.next
        start.next = node_position
   
    
    def display(self):
        start = self.head
        while start:
            print(start.data, '->' , end=' ')
            start = start.next


link = SLL()

link.insert_beginning(5)
link.inserting_ending(10)
link.insert_beginning(0)
link.inserting_ending(20)
link.insert_at_position(100, 2)

link.display()