class Stack:

    def __init__(self):
        self.stack = list()
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return False
    
    def display(self):
        print(self.stack)



stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)

stack.pop()

stack.pop()

stack.push(5)

store = stack.peek()

stack.display()

print(f"\n{store} is peeked.")