# Python3 implementation of the approach


def dpt():
    return (input().split())



sa=[]

for x in range(4):
    sa.append (list(map(int,dpt())))
print(sa)



class Graph:
    adj = []

    def __init__(self, v, e):

        self.v = v
        self.e = e
        self.adj=sa
        # Graph.adj = [[0 for i in range(v)]
        #              for j in range(v)]


    def addEdge(self, start, e):

        self.adj[start][e] = 1
        self.adj[e][start] = 1

    def BFS(self, start):

        visited = [False] * self.v
        q = [start]

        visited[start] = True

        while q:
            vis = q[0]

            # Print current node
            print(vis, end=' ')
            q.pop(0)

            # For every adjacent vertex to
            # the current vertex
            for i in range(self.v):
                if (self.adj[vis][i] == 1 and  (not visited[i])):
                    # Push the adjacent node
                    # in the queue
                    q.append(i)

                    # set
                    visited[i] = True


# Driver code
v, e = 4, 4

# Create the graph
# G = Graph(v, e)
# G.addEdge(0, 1)
# G.addEdge(0, 2)
# G.addEdge(1, 3)
#
#
# G.adj=[y for y in [x for x in range()]]


# Perform BFS
st=int(input('enter starting vertice'))

for i,x in enumerate(sa[st-1]):
    if x==1:
        print(i+1)







# This code is contributed by ng24_7
