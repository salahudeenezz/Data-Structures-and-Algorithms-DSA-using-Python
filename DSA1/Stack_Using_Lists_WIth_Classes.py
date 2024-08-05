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
    
    def search(self, element):
        return (element in self.numbers)
    
    def search_2(self, element):
        if element in self.numbers:
            return f"{element} is found in the stack."
        else: 
            return f"{element} is not found in the stack"
    
    def search_3(self, element):
        index = 0
        for number in self.numbers:
            if number == element:
                return f"{number} is found at index {index}"
            else:
                index += 1
        return False
    
    def search_4(self, element):
        if element in self.numbers:
            store_index = self.numbers.index(element)
            return f"{element} is found at index {store_index}"
        else: 
            return False
    

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

store_element = stack.search(10)
print(store_element)

store_result = stack.search_2(10)
print(store_result)

store_result2 = stack.search_3(10)
print(store_result2)

store_result_3 = stack.search_4(10)
print(store_result_3)



"""
   
    def search_3(self):
        element = int(input())
        index = 0
        for number in self.numbers:
            if number == element:
                return f"{number} is found at index {index}"
            else:
                index += 1
        return False"""