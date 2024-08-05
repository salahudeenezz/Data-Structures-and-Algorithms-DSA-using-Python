
def display(self):
        start = self.head
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.next

def display(self):
        start = self.tail
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.prev