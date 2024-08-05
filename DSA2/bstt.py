class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)
    
    def insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)

        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)
        elif node.data == node.data:
            pass
    
    def pre_order(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)
    
    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=' ')

    
    def level_order(self, node):
        self.queue = []
        if node is not None:
            self.queue.append(node)
        while self.queue:
            temp = self.queue.pop(0)
            print(temp.data, end=' ')

            if temp.left is not None and temp.right is not None:
                self.queue.append(temp.left)
                self.queue.append(temp.right)
            else:
                pass
                
    
    def search(self, node, value):
        if node is not None:
            if value == node.data:
                return node
            elif value > node.data:
               return self.search(node.right, value)
            elif value < node.data:
                return self.search(node.left, value)
    
    def get_inorder_successor(self, node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp
        

    def delete(self, node, value):
        if node is not None:
            if value == node.data:
                if node.left is None and node.right is None:
                    return None
                elif node.left is not None and node.right is not None:
                    temp = self.get_inorder_successor(node.right)
                    node.data = temp.data
                    node.right = self.delete(node.right, temp.data)
                elif node.left is not None:
                    temp = node.left
                    node = None
                    return temp
                elif node.right is not None:
                    temp = node.right
                    node = None
                    return temp
            
            elif value > node.data:
                node.right = self.delete(node.right, value)
            elif value < node.data:
                node.left = self.delete(node.left, value)
        
        return node

        

tree = BST()
tree.insert(20)
tree.insert(15)
tree.insert(9)
tree.insert(16)
tree.insert(29)
tree.insert(22)
tree.insert(30)


tree.pre_order(tree.root)
print("\n")
tree.in_order(tree.root)
print("\n")
tree.post_order(tree.root)

print("\n")

tree.level_order(tree.root)

print("\n")
search_result = tree.search(tree.root, 20)

if search_result is not None:
    print(search_result.data)
else:
    print(None)
    

tree.delete(tree.root, 29)
tree.in_order(tree.root)