class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circularlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
            self.tail = nb
        else:
            nb.next = self.head
            self.head = nb
    
    def insert_at_ending(self, data):
        ne = Node(data)
        if self.tail is not None:
            self.tail.next = ne
            self.tail = ne
            self.tail.next = self.head
        else:
            print(None)

    def insert_at_position_from_head(self, pos, data):
        np = Node(data)
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            prev = prev.next
            start = start.next
        np.next = start
        prev.next = np

    def insert_at_position_from_tail(self, pos, data):
        np2 = Node(data)
        prev = self.tail
        start = self.tail.next
        for i in range(pos):
            prev = prev.next
            start = start.next
        np2.next = start
        prev.next = np2
    
    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            return -1

    def delete_at_the_end(self):
        if self.head is not None:
            prev = self.head
            start = self.head.next
            while start.next != self.head:
                prev = prev.next
                start = start.next
            self.tail = prev
            self.tail.next = self.head
    
    def delete_position_from_head(self, pos):
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            prev = prev.next
            start = start.next
        prev.next = start.next
        start.next = None

    def delete_position_from_tail(self, pos):
        prev = self.tail
        start = self.tail.next
        for i in range(pos):
            prev = prev.next
            start = start.next
        prev.next = start.next
        start.next = None

    def display(self):
        start = self.head
        print(start.data, '->', end=' ')
        while start.next != self.head:
            start = start.next
            print(start.data, '->', end=' ')
        print(start.next.data)
        print("\n")
    
    def linear_search(self, element):
        start = self.head
        while True:
            if start.data == element:
                return f"{element} is found in the Circular Linked List."
            else:
                start = start.next
            if start == self.head:
                break
        return f"{element} is not found in the Circular Linked List."
    
    def linear_search_two(self, element):
        prev = self.tail
        while True:
            if prev.data == element:
                return f"{element} is found in the Circular Linked List."
            else:
                prev = prev.next
            if prev == self.tail:
                break
        return f"{element} is not found in the Circular Linked List."

link = Circularlinkedlist()
link.insert_at_beginning(20)
link.insert_at_beginning(5)
link.insert_at_beginning(10)
link.insert_at_beginning(15)
link.insert_at_ending(30)
link.insert_at_ending(40)
link.insert_at_ending(50)
link.insert_at_ending(60)
link.insert_at_position_from_head(5, 35)
link.insert_at_position_from_head(5, 34)
link.delete_at_beginning()
link.delete_at_the_end()
link.delete_at_the_end()
link.delete_position_from_head(2)
link.delete_position_from_tail(2)
link.display()

store = link.linear_search(10)
print(store)

cut = link.linear_search_two(34)

print(cut)
