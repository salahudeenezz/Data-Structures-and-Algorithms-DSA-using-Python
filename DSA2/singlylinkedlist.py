class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
        else:
            nb.next = self.head
            self.head = nb
    
    def insert_at_ending(self, data):
        ne = Node(data)
        if self.head is not None:
            start = self.head
            while start.next is not None:
                start = start.next
            start.next = ne
        else:
            print("Head is empty.")
    
    def insert_at_position(self, pos, data):
        np = Node(data)
        if self.head is not None:
            prev = self.head
            start = self.head.next
            for i in range(pos-1):
                prev = prev.next
                start = start.next
            np.next = start
            prev.next = np
        else:
            print("Head is empty")
    
    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Head is empty")
    
    def delete_at_the_end(self):
        if self.head is not None:
            prev = self.head
            start = self.head.next
            while start.next is not None:
                prev = prev.next
                start = start.next
            prev.next = None
        else:
            print("head is empty")
    
    def delete_at_the_position(self, pos):
        if self.head is not None:
            prev = self.head
            start = self.head.next
            for i in range(pos-1):
                prev = prev.next
                start = start.next
            prev.next = start.next
            start.next = None
        else:
            print("Head is empty")

    def display(self):
        start = self.head
        while start is not None:
            print(start.data, "->", end=' ')
            start = start.next
        print('None')
    
    def linear_search(self, element):
        if self.head is not None:
            begin_here = self.head
            while begin_here is not None:
                if begin_here.data == element:
                    return f"{element} is found in the Linked List."
                else:
                    begin_here = begin_here.next

            return f"{element} is not found in the Linked List."  
        else:
            return None
        
link = SinglyLinkedList()

link.insert_at_beginning(10)
link.insert_at_beginning(5)
link.insert_at_ending(20)
link.insert_at_ending(30)
link.insert_at_position(2, 15)
link.insert_at_position(5, 25)
link.delete_at_beginning()
link.delete_at_the_end()
link.insert_at_beginning(5)
link.insert_at_ending(40)
link.delete_at_the_position(3)
link.display()

store = link.linear_search(30)
print(store)