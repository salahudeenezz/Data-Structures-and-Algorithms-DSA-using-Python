class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element : int):
        if self.stack:
            self.stack.append(element)
        else:
            self.stack.append(element)
        
    def pop(self, index):
        if self.stack:
            self.stack.pop(index)
        else:
            print("The stack is empty")
    
    def display(self):
        if self.stack:
            print(self.stack)
        else:
            print("The stack is empty.")
    
    def peek(self, front):
        if self.stack:
            peek = self.stack[front]
            return peek
        else:
            print("Empty")
    
    def linear_search(self, element):
        if self.stack:
            for i in range(len(self.stack)):
                if self.stack[i] == element:
                    return f"{element} is found at index {i}."
                else:
                    continue

            return f"{element} was not found in the Stack"
        else:
            print("Empty Stack.")

link = Stack()

link.push(5)
link.push(4)
link.push(3)
link.push(2)
link.push(1)

link.pop(-1)
link.pop(-1)
link.pop(-1)

link.display()

store_peek_result = link.peek(-1)
print(store_peek_result)

store = link.linear_search(4)
print(store)
