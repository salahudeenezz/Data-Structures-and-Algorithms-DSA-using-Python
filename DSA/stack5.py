class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.front = None

    def push(self, data):
        element3 = Element(data)
        element3.next = self.front
        self.front = element3

    def search(self, element):
        start = self.front
        while start:
            if start.data == element:
                return f"{element} is found in the stack linked list."
            start = start.next
        return f"{element} is not found in the stack linked list"

    def display(self):
        start = self.front
        while start:
            print(start.data, '\n|', end='\n')
            start = start.next


element1 = Element(10)
link = Stack()
link.front = element1

element2 = Element(20)
element2.next = element1
link.front = element2
link.push(30)
link.push(40)

link.display()

store = link.search(70)
print(f"\n{store}", end='')

