class HashMaps:
    def __init__(self):
        self.hashmaps = {}
    
    def append(self, key, value):
        if self.hashmaps:
            self.hashmaps[key] = value
        else:
            self.hashmaps[key] = value
    
    def update(self, key, value):
        self.hashmaps[key] = value
    
    def delete(self, key):
        if key in self.hashmaps:
            del self.hashmaps[key]
        else:
            pass

    def display(self):
        print(self.hashmaps)
    
    def display_two(self, key):
        print(self.hashmaps[key])
    
    def travel(self):
        for key, value in self.hashmaps.items():
            print(f"{key.title()}: {value.capitalize()}")
    
    def search(self, target_key):
        if target_key in self.hashmaps:
            return f"{self.hashmaps[target_key]} is found in the HashMaps."
        else:
            return f"{target_key} is not found in the HashMaps."

link = HashMaps()
link.append("name", "salahudeen")
link.append("age", 'twenty years old')
link.append("country", "Ghana")
link.delete('name')
link.update("country", "America")
link.display()
store = link.search("age")
print(store)