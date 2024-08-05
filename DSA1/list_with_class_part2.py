class List:
    def __init__(self):
        self.numbers = []
    
    def append(self, element : int):
        self.numbers.append(element)
    
    def insert(self, index: int, element: any):
        self.numbers.insert(index, element)
    
    def delete(self, index: int):
        self.numbers.pop(index)
    
    def delete_2(self, element):
        self.numbers.remove(element)
    
    def delete_3(self, index):
        del self.numbers[index]

    def modify_or_change(self, index, element):
        self.numbers[index] = element
    
    def slice(self, start_index, end_index):
        self.slicing = self.numbers[start_index:end_index]
        return sorted(self.slicing, reverse=True)
    
    def display(self):
        self.numbers.sort()
        self.numbers.reverse()
        self.numbers.sort(reverse=False)
        print(self.numbers)
    
    def display2(self, index: int):
        print(self.numbers[index])
    
    def display3(self):
        for slice in self.slicing:
            print(slice)
    

list = List()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.append(10)
list.insert(0, 0)
list.delete(0)
list.delete_2(10)
list.delete_3(8)
list.modify_or_change(0, 0)
list.modify_or_change(0, 1)
list.display()
list.display2(0)
store = list.slice(1, 4)
print(store)
list.display3()

