numbers = [1, 2, 3] # O(n)
print(numbers[0])  # O(1) 
print(numbers[1])  # O(1) 
print(numbers[2])  # O(1) 
print('\n')

numbers[0] = 2  # O(1)
numbers[1] = 1  # O(1)
numbers[2] = 5  # O(1)

print(numbers)  # O(n)
print('\n')

for number in numbers: # O(n)
    print(number) # O(n)
print('\n')

names = ['kwaku', 'bonsu']
names.append('ama bonsu') # O(1)
print(names) # O(n)
print('\n')

digits = [1, 2, 3, 4, 5]  # O(n) 

digits.insert(5, 6)  # O(1)
digits.insert(2, 7)  # O(n)
digits.insert(0, 10) # O(n)
print(digits) # O(n)
print('\n')

countries = ['ghana', 'nigeria', 'togo', 'kenya']
del countries[3]  # O(1)
countries.remove('togo')  # O(1)
store_country = countries.pop(1)  # O(1)
print(countries) # O(n)
print(f"{store_country.title()} is out") # O(1)
print('\n')

drill_rappers = ('kay flock', 'dthang')
print(drill_rappers[0])  # O(1)
drill_rappers[1] = 'dd osama'  # O(1)
print(drill_rappers)  # O(n)
for drill_rapper in drill_rappers: # O(n) #travesal
    print(drill_rapper) # O(n)
 
 
numbers = [1, 2, 3, 4, 5]

index = 0

for number in numbers:
    if number == 1:
        print(f"It is found index {index}")
    
    index += 1
  
numbers = [1, 2, 3, 4, 5]
index = 0
for number in numbers:
    if number == 3:
        print(f"{number} is stored at index {index}")
    else:
        index += 1

numbers = [1, 2, 3, 4, 5]
index = 0 
element = eval(input("Enter a number to check if it's in the list or not: "))

for number in numbers:
    if number == element:
        print(f"{element} is found at index {index}")
    else:
        index += 1   

numbers = [1, 2, 3, 4, 5]
store = numbers[2]
print(store)

numbers = [1, 2, 3, 4, 5]
store = numbers.index(3)
print(store)

numbers = [1, 2, 3, 4, 5]

if 5 in numbers:
    print("yes")
else:
    print("nope")