stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

stack.pop()
stack.pop()
stack.pop()

print(stack)

peek = stack[0]
print(f"Peek: {peek}")





stack = [1, 2, 3, 4, 5]

stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.insert(1, 2)
stack.insert(2, 3)
stack.insert(3, 4)
stack.insert(4, 5)

del stack[4]
del stack[3]
del stack[2]
del stack[1]

stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

stack.remove(5)
stack.remove(4)
stack.remove(3)
stack.remove(2)


print(stack)