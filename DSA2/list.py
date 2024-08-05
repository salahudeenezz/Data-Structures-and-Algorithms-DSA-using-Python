class List:
    def __init__(self):
        self.names = ["jake"]
    
    def append(self, element): 
        if self.names:
            self.names.append(element)
        else:
            self.names.append(element)
    
    def insert(self, index, element):
        if self.names:
            self.names.insert(index, element)
        else:
            print(None)
    
    def update(self, index, element):
        self.names[index] = element

    def delete(self, index):
        if self.names:
            del self.names[index]
        else:
            print(False)
    
    def delete_two(self, index):
        if self.names:
            self.names.pop(index)
        else:
            print(None)
    
    def delete_three(self, element):
        if self.names:
            self.names.remove(element)
        else:
            print(None)

    def display(self):
        if self.names:
            print(self.names)
        else:
            print("None")
    
    def travesal(self):
        if self.names:
            for name in self.names:
                print(name)
        else:
            print("None")
    
    def linear_search(self, element):
        if self.names:
            for i in range(len(self.names)):
                if self.names[i] == element:
                    return f"{element} is found at index {i}"
                else:
                    continue

            return f"{element} was not found in the list." 
        else:
            print("Empty List")


list = List()
list.append("salahudeen")
list.append("ayubi")
list.append("ezzaldiin")
list.insert(0, "speed")
list.insert(2, "kai")
list.append("cenat")
list.delete(0)
list.delete(2)
list.delete(-1)
list.update(0, "jane")
list.display()

store = list.linear_search('ezzaldiin')
print(store)