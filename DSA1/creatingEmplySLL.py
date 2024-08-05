class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL: 
    def __init__(self):
        self.head = None
    
    def insert_beginning(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
        else:
            nb.next = self.head
            self.head = nb
    
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
    def search(self, element):
        start = self.head
        while start is not None:
            if start.data == element:
                return start
            start = start.next
        return None


link = SLL()

link.insert_beginning(5)
link.inserting_ending(10)
link.insert_beginning(0)
link.inserting_ending(20)

link.display()

print('\n')
store_node = link.search(30)
if store_node is not None:
    print(f"{store_node.data} is found in the linked list")
else:
    print(store_node)