
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Set to keep track of visited nodes.


def dfs1(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# dfs(visited, graph, 'A')

def dfs2(nums,path,res):
     if not nums:
        res.append(path)
        return
     for i in range(len(nums)):
        dfs2(nums[:i]+nums[i+1:],path+[nums[i]],res)



num=[1,2,3,4]
def permute(nums):
    res = []
    dfs2(nums,[],res)
    return res
print(permute(num))

