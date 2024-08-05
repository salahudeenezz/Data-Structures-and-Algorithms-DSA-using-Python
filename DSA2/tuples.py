class Tuple:
    def __init__(self):
        self.tuples = (1, 2, 3, 4, 5)
    
    def display(self):
        print(self.tuples)
    
    def display_two(self, index):
        print(self.tuples[index])
    
    def travesal(self):
        for tuple in self.tuples:
            print(tuple)

link = Tuple()
link.display()
link.display_two(2)
