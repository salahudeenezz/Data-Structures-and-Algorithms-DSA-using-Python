class Queue:
    def __init__(self):
        self.queue : list[int] = []
    
    def enqueue(self, element : int):
        if self.queue:
            self.queue.append(element)
        else:
            self.queue.append(element)
    
    def dequeue(self, index):
        if self.queue:
            self.queue.pop(index)
        else:
            print("The queue is empty.")
    
    def display(self):
        if self.queue:
            print(self.queue)
        else:
            print("The queue is empthy.")

    def peek_front(self, index):
        if self.queue:
            peek = self.queue[index]
            return peek
        else:
            print("The queue is empty.")

    def linear_search(self, element):
        if self.queue:
            for i in range(len(self.queue)):

                if self.queue[i] == element:
                    return f"{element} is found at index {i}"
                else:
                    continue

            return f"{element} was not found in the Queue."
        else:
            print("Empty Queue")

link = Queue()
link.enqueue(0)
link.enqueue(1)
link.enqueue(2)
link.dequeue(0)
link.display()

store_peek = link.peek_front(0)
print(store_peek)

store = link.linear_search(2)
print(store)