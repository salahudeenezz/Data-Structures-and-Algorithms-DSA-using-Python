class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.front = None

    def push(self, data):
        element1 = Node(data)
        self.front = element1

    def push1(self, data):
        element2 = Node(data)
        element2.next = self.front
        self.front = element2

    def pop(self):
        popped_element = self.front
        self.front = self.front.next
        popped_element.next = None
        return popped_element.data
    
    def push2(self, data):
        element3 = Node(data)
        element3.next = self.front
        self.front = element3

    def display(self):
        start = self.front
        while start:
            print(start.data, '\n|', end='\n')
            start = start.next


link = Stack()
link.push(10)
link.push1(20)
link.push2(30)
store_pop = link.pop()
store_pop1 = link.pop()

link.display()
print(f"\n{store_pop} is popped off the list")
print(f"\n{store_pop1} is popped off the list")
