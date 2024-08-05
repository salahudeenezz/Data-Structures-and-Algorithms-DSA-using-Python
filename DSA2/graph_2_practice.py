def dsf(graph, node):
    queue = []
    node_checked = []
    queue.append(node)
    node_checked.append(node)
    while queue:
        pop_the_node = queue.pop(-1)
        print(pop_the_node)
        for neighbours in graph[pop_the_node]:
            if neighbours not in node_checked:
                queue.append(neighbours)
                node_checked.append(neighbours)
def bsf(graph, node):
    queue = []
    node_checked = []
    queue.append(node)
    node_checked.append(node)
    while queue:
        pop_the_node = queue.pop(0)
        print(pop_the_node)
        for neighbours in graph[pop_the_node]:
            if neighbours not in node_checked:
                queue.append(neighbours)
                node_checked.append(neighbours)



graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 6],
    5: [3, 6],
    6: [4, 5]
}

dsf(graph, 1)
bsf(graph, 1)