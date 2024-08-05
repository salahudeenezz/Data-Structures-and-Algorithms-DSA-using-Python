class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        insert_node_at_beginning = Node(data)
        if self.head is None:
            self.head = insert_node_at_beginning
            self.tail = insert_node_at_beginning
        else:
            insert_node_at_beginning.next = self.head
            self.head.prev = insert_node_at_beginning
            self.head = insert_node_at_beginning
    
    def insert_at_the_end(self, data):
        insert_node_at_the_end = Node(data)
        insert_node_at_the_end.prev = self.tail
        self.tail.next = insert_node_at_the_end
        self.tail = insert_node_at_the_end
    
    def insert_at_position_from_head(self, pos, data):
        node_position = Node(data)
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
                prev = prev.next
                start = start.next
        node_position.next = start
        start.prev = node_position
        node_position.prev = prev
        prev.next = node_position
        
    

    def insert_at_position_from_tail(self, pos, data):
        node_position_two = Node(data)
        prev = self.tail
        start = self.tail.prev
        for i in range(pos-1):
                prev = prev.prev
                start = start.prev
        node_position_two.prev = start
        start.next = node_position_two
        node_position_two.next = prev
        prev.prev = node_position_two
    
    def delete_from_beginning(self):
        if self.head is not None:
              self.head.next.prev = None
              self.head = self.head.next
        else:
             print(None)
    
    def delete_from_end(self):
        if self.tail is not None:
              self.tail.prev.next = None
              self.tail = self.tail.prev
        else:
             print(None)
    
    def delete_at_position_from_head(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            prev = prev.next
            start = start.next
        prev.next = start.next
        start.next.prev = prev
        start.next = None
        start.prev = None
    
    def delete_at_position_from_tail(self, pos):
        prev = self.tail
        start = self.tail.prev
        for i in range(pos-1):
             prev = prev.prev
             start = start.prev
        prev.prev = start.prev
        start.prev.next = prev
        start.prev = None
        start.next = None
    
    
    def display(self):
        start = self.head
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.next

        prev = self.tail
        print("\n")
        while prev is not None:
            print(prev.data, '->', end=' ')
            prev = prev.prev
        print("\n")

    def linear_search(self, element):
        if self.head is not None:
            start = self.head
            while start is not None:
                if start.data == element:
                    return f"{element} is found in the Doubly Linked List."
                else:
                    start = start.next
            return f"{element} is not found Doubly Linked List."
        else:
            return

    def linear_search_two(self, element):
        if self.tail is not None:
            prev = self.tail
            while prev is not None:
                if prev.data == element:
                    return f"{element} is found in the Doubly Linked List."
                else:
                    prev = prev.prev
            return f"{element} is not found Doubly Linked List."
        else:
            return

link = DoublyLinkedList()
link.insert_at_beginning(10)
link.insert_at_beginning(20)
link.insert_at_beginning(30)
link.insert_at_the_end(5)
link.insert_at_the_end(40)
link.insert_at_beginning(0)
link.insert_at_the_end(50)
link.insert_at_position_from_head(2, 35)
link.insert_at_position_from_tail(2, 4)
link.delete_from_beginning()
link.delete_from_end()
link.delete_at_position_from_head(2)
link.delete_at_position_from_tail(2)
link.display()


store = link.linear_search(10)
print(store)

check = link.linear_search_two(40)
print(check)