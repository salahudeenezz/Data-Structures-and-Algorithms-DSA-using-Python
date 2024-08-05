class List:
    def __init__(self, notempty):
        self.numbers = notempty
    
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
        return self.slicing
    
    def display(self):
        print(self.numbers)
    
    def display2(self, index: int):
        print(self.numbers[index])
    
    def display3(self):
        for slice in self.slicing:
            print(slice)
    

list = List([1, 2, 3, 4, 5])
list.append(6)
list.insert(0, 7)
list.delete(0)
list.delete_2(4)
list.delete_3(1)
list.modify_or_change(0, 9)
list.display()
list.display2(0)

store = list.slice(0, 4)
print(store)

list.display3()