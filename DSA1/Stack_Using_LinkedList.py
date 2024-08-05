class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        element = Element(data)
        if self.head is None:
            self.head = element
        else:
            element.next = self.head
            self.head = element
            
    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("The stack is empty.")

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            print("The stack is empty.")

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next
    
      
    def search(self, element):
        start = self.head
        while start is not None:
            if start.data == element:
                return start
            start = start.next
        return None

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.push(20)
stack.display()
print("\n")
print(stack.peek())


store_result = stack.search(30)
if store_result is not None:
    print(f"{store_result.data} is found in the stack linked list.")
else:
    print(store_result)