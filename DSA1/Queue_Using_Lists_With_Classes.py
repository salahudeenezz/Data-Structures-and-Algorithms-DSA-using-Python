class Queue:
    def __init__(self):
        self.numbers = list()
    
    def enqueue(self, element):
        if self.numbers is None:
            self.numbers.append(element)
        else:
            self.numbers.append(element)
    
    def dequeue(self):
        if self.numbers is not None:
            self.numbers.pop(0)
        else:
            print("The stack list is empty.")
    
    def display(self):
        print(self.numbers)
    
    def peek(self):
        if self.numbers is not None:
            peek = self.numbers[0]
            return peek
        else:
           return "The queue list is empty."
        def search(self, element):
        return (element in self.numbers)
    
    def search_2(self, element):
        if element in self.numbers:
            return f"{element} is found in the queue."
        else: 
            return f"{element} is not found in the queue"
    
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

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.display()

print(queue.peek())

store_element = queue.search(10)
print(store_element)

store_result = queue.search_2(10)
print(store_result)

store_result2 = queue.search_3(10)
print(store_result2)

store_result_3 = queue.search_4(10)
print(store_result_3)
