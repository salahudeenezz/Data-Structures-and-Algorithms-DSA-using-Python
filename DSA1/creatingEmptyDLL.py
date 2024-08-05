class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
        else:
            nb.next = self.head 
            self.head.prev = nb
            self.head = nb

    def insert_at_ending(self, data):
        ne = Node(data)
        if self.tail is None:
            self.tail = ne
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            ne.prev = self.tail
            self.tail.next = ne
            self.tail = ne
    def insert_position_from_beginning(self, pos, data):
        node_position_1 = Node(data)
        prev = self.head
        start = self.head.next
        for i in range(pos-1):
            prev = prev.next
            start = start.next
        prev.next = node_position_1
        start.prev = node_position_1
        node_position_1.prev = prev
        node_position_1.next = start
    
    def insert_position_from_ending(self, pos, data):
        node_position_2 = Node(data)
        prev = self.tail
        start = self.tail.prev
        for i in range(pos-1):
            prev = prev.prev
            start = start.prev
        prev.prev = node_position_2
        start.next = node_position_2
        node_position_2.prev = start
        node_position_2.next = prev
        
    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next
    
    def display1(self):
        start = self.tail
        print('\n')
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.prev
    
    def search_from_head(self, element):
        start = self.head
        while start is not None:
            if start.data == element:
                return start
            start = start.next
        return None
    
    def search_from_tail(self, element):
        prev = self.tail
        while prev is not None:
            if prev.data == element:
                return prev
            prev = prev.prev
        return None
            

link = DLL()

link.insert_at_beginning(3)
link.insert_at_ending(4)
link.insert_at_ending(5)
link.insert_at_ending(6)
link.insert_position_from_beginning(2, 7)
link.insert_position_from_ending(2, 8)

link.display()
link.display1()



print("\n")
store_node = link.search_from_head(3)
if store_node is not None:
    print(f"{store_node.data} is found in the DLL.")
else:
    print(store_node)

print("\n")
store_node2 = link.search_from_tail(3)
if store_node2 is not None:
    print(f"{store_node2.data} is found in the DLL.")
else:
    print(store_node2)