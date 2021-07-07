###############
# The Algorithm (In English):

# 1) Pick any node.
# 2) If it is unvisited, mark it as visited and recur on all its
#    adjacent nodes.
# 3) Repeat until all the nodes are visited, or the node to be
#    searched is found.


# The graph below (declared as a Python dictionary)
# is from the linked website and is used for the sake of
# testing the algorithm. Obviously, you will have your own
# graph to iterate through.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes.


##################
# The Algorithm (In Code)

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code to test in python yourself.
# Note that when calling this, you need to
# call the starting node. In this case it is 'A'.
dfs(visited, graph, 'A')

# NOTE: There are a few ways to do DFS, depending on what your
# variables are and/or what you want returned. This specific
# example is the most fleshed-out, yet still understandable,
# explanation I could find.