class Stack:
    def __init__(self):
        self.numbers = list()
    
    def push(self, element):
        if self.numbers is None:
            self.numbers.append(element)
        else:
            self.numbers.append(element)
    
    def pop(self):
        if self.numbers is not None:
            self.numbers.pop()
        else:
            print("The stack list is empty.")
    
    def display(self):
        print(self.numbers)
    
     
    def peek(self):
        if self.numbers is not None:
            peek = self.numbers[-1]
            return peek
        else:
           return "The stack list is empty."


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.pop()
stack.pop()
stack.pop()

stack.display()

print(stack.peek())