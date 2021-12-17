



from collections import defaultdict
import sys
import time
maxInt=99999999999999

import random
wgtOption=[1,2,3,4,6,7,8,10]

zONe=[0,0,1,0,1,0,0]
def matrixGEN(u):
  adj2=[]
  for x in range(u):
    ap=[]
    for y in range(u):
      inc=random.choice( zONe)
      if inc==1:
        ap.append(random.choice(wgtOption))
      else:
        ap.append(0)
    adj2.append(ap)
  return adj2
    

def mrxCONV(matrix):
    adj = []
    for i,row in enumerate(matrix):
        for j,col in enumerate(row):
            if col!=0:
                adj.append( [i,j,col] )
    return adj


## this is actually a variant of BFS |||||||||||| implemented by that.............
def byUnsrtArr(a,tm):
    s=time.perf_counter()
    edges=defaultdict(list)

    for x,y,z in a:
        edges[x].append((y,z))

    k=a[0][0]


    unsortedList=[(0,0)]
    visited=set()
    t=0
    while unsortedList:
        w1,n1=unsortedList.pop()
        if n1 in visited:
            continue
        visited.add(n1)
        t=max(t,w1)

        for n2,w2 in edges[n1]:
            if n2 not in visited:
                # heapq.heappush(unsortedList,(w1+w2,n2))
                unsortedList.append((w1+w2,n2))

        unsortedList.sort(reverse=True,key=lambda x:x[0])
        ### sorting cause the list is unsorted .. needs constant sorting
        ### also in worst case the complexity is O(log.n)
        ## gonna be much more faster after the 1st sort.. if
    # print(len(visited))

    ss = time.perf_counter()
    ss-=s
    return  (ss+tm)*1000



################################ part 3 and 4 above
class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    
    
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right



        if smallest != idx:

            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest


            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)



    def extractMin(self):


        if self.isEmpty() == True:
            return


        root = self.array[0]


        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode


        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1


        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:

            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            
            i = (i - 1) // 2



    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(dist, n):
    print("Vertex\tDistance from source")
    for i in range(n):
        print("%d\t\t%d" % (i, dist[i]))
    print(max(dist))

maxint=999999999


class Graph2():
    t1=time.perf_counter()
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    def minDistance(self, dist, sptSet):
        min = maxint
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def dijkstra(self, src):

        dist = [maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        # self.printSolution(dist)
    tm2=time.perf_counter()


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)


    def addEdge(self, src, dest, weight):
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
    def dijkstra(self, src):

        V = self.V
        dist = []
        minHeap = Heap()

        for v in range(V):
            dist.append(maxInt)
            minHeap.array.append(minHeap.
                                 newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        minHeap.size = V;

        while not minHeap.isEmpty():
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
            for pCrawl in self.graph[u]:
                v = pCrawl[0]
                if minHeap.isInMinHeap(v) and dist[u] != maxInt and pCrawl[1] + dist[u] < dist[v]:
                    dist[v] = pCrawl[1] + dist[u]
                    minHeap.decreaseKey(v, dist[v])
        # printArr(dist, V)




l,u=0,random.randint(1,100)
wgtOption=[1,2,3,4,6,7,8,10]

tm1=time.perf_counter()## timer for the extra time taken to generate the matrix....
matrix=matrixGEN(u)
tm2=time.perf_counter()-tm1

try:
# print(matrix)
    graph = Graph(u)
    # print('\nALGOROTHM with Adjacency List')
    cnt=0
    ############################################
    t_ad=time.perf_counter()
    for i,row in enumerate(matrix):
        for j,col in enumerate(row):
            if col!=0:
                cnt+=1
                graph.addEdge(i,j,col)

    print('the vertex is {} And the Edge Count is {}'.format(u,cnt))

    graph.dijkstra(0)
    t_ad2=time.perf_counter()

    ############  >>> ''' the matrix graph IMPL'''
    print('\nALGOROTHM with Adjacency Matrix took : {:.3f} ms'.format((t_ad2-t_ad)*1000))
    #######################################
    t_mat=time.perf_counter()
    g = Graph2(u)
    g.graph = matrix

    g.dijkstra(0)
    t_mat2=time.perf_counter()
    print('ALGOROTHM with Adjacency Matrix took : {:.3f} ms\n\n'.format((t_mat2-t_mat)*1000))

    ##################################################
    arr=mrxCONV(matrix)
    print('for unsorted array Adjacency list : {:.3f}'.format(byUnsrtArr(  arr ,0)),'ms')

    ###################################


    print('for unsorted array MATRX : {:.3f}'.format(byUnsrtArr(arr,tm2)),' ms')

except:
    print('please run again \n UNEXPECTED ERROR occoured')

