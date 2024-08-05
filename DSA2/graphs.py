class HashMaps:
    def __init__(self):
        self.graph = {}
    
    def insertion(self, node : str, list : list[str]):
        self.graph[node] = list
    
    def deletion(self, node : str):
        del self.graph[node]
    
    def bfs(self, graph_dict, start_node):
        self.queue = [start_node]
        self.visited_node = [start_node]
        while self.queue:
            pop_node = self.queue.pop(0)
            print(pop_node)
            for continue_node in graph_dict[pop_node]:
                if continue_node not in self.visited_node:
                    self.queue.append(continue_node)
                    self.visited_node.append(continue_node)
    
    
    def dfs(self, graph_dict, start_node):
        self.stack = [start_node]
        self.visited = [start_node]
        while self.stack:
            popped_node = self.stack.pop(-1)
            print(popped_node)
            for checking_neighbours in graph_dict[popped_node]:
                if checking_neighbours not in self.visited:
                    self.stack.append(checking_neighbours)
                    self.visited.append(checking_neighbours)


    def search(self, target_node : str):
        if target_node in self.graph:
            return f"\n{self.graph[target_node]} is found in the graph."
        else:
            return f"\n{target_node} is not found in the graph."

    def display(self):
        print(self.graph)


link = HashMaps()
link.insertion("A", ["B"])
link.insertion("B", ["C"])
link.insertion("C", ["D"])
link.insertion("D", ["E"])
link.insertion("E", ["F"])
link.insertion("F", [])

link.dfs(link.graph, "A")

