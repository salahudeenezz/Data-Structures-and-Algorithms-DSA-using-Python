class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL: 
    def __init__(self):
        self.head = None
    
    def display(self):
        start = self.head
        print(start.data, '->', end=' ')
        while start.next:
            print(start.next.data,f"-> {None}", end=' ')
            start = start.next


node_1 = Node(10)
link = SLL()
link.head = node_1
node_2 = Node(20)
node_1.next = node_2

link.display()