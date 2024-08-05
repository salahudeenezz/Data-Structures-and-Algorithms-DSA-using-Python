class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL: 
    def __init__(self):
        self.head = None
    
    def inserting_ending(self, data):
        ending_node = Node(data)
        start = self.head
        while start.next:
            start = start.next
        start.next = ending_node
    
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

link.inserting_ending(30)
link.inserting_ending(40)