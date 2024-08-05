class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackSinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
        else:
            nb.next = self.head
            self.head = nb
    
    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("None")
    
    def display(self):
        start = self.head
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.next
    
    def peek(self):
        peek = self.head.data
        return peek
    
    def linear_search(self, target):
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.data == target:
                    return f"{target} is found in the Stack."
                else:
                    current = current.next

            return f"{target} is not found in the Stack."
        else:
            return None

link = StackSinglyLinkedList()
link.push(10)
link.push(8)
link.push(6)
link.push(4)
link.push(2)
link.pop()
link.pop()
link.display()

store_peek = link.peek()
print(f"\n{store_peek}")
store = link.linear_search(8)
print(store)