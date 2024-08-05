class Sets:
    def __init__(self):
        self.sets = set()
    
    def append(self, element):
        self.sets.add(element)
    
    def remove(self, element):
        self.sets.remove(element)
    
    def display(self):
        print(self.sets)
    
    def display_two(self, index):
        lists = list(self.sets)
        print(lists[index])

    def travesal(self):
        a = list(self.sets)
        for set in a:
            print(set)

link = Sets()
link.append(1)
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.remove(3)
link.update(0, 6)
link.display()
link.travesal()
