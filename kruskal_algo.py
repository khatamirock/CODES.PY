class Edge :

   def __init__(self, arg_src, arg_dst, arg_weight) :
       self.src = arg_src
       self.dst = arg_dst
       self.weight = arg_weight

class Graph :

    def __init__(self, arg_num_nodes, arg_edgelist) :
        self.num_nodes = arg_num_nodes
        self.edgelist  = arg_edgelist
        self.parent    = []
        self.rank      = []

        self.mst       = []

    def FindParent (self, node,t) :
        if t==1:
        
            if node != self.parent[node] :
                self.parent[node] = self.FindParent(self.parent[node],1) #
                #

            return self.parent[node]
        else:
            ##### without pathCompression>>>>>>>>
            if node == self.parent[node] :
               return node
            return self.FindParent(self.parent[node],2)

    def KruskalMST (self,cse) :

        
        self.edgelist.sort(key = lambda Edge:Edge.weight)

        self.parent = [None] * self.num_nodes
        self.rank   = [None] * self.num_nodes

        for n in range(self.num_nodes) :
            self.parent[n] = n 
            self.rank[n] = 0   

        for edge in self.edgelist :
            root1 = self.FindParent(edge.src,cse)
            root2 = self.FindParent(edge.dst,cse)

            
            
            if root1 != root2 :
               self.mst.append(edge)
               if self.rank[root1] < self.rank[root2] :
                  self.parent[root1] = root2
                  self.rank[root2] += 1
               else :
                  self.parent[root2] = root1
                  self.rank[root1] += 1

        cost = 0
        for edge in self.mst :
            
            
            cost += edge.weight
        print("\nCost of minimum spanning tree : " +str(cost))
import time
import random
mp={1:'with Path Compression',2:'WithOut Compression'}
def main() :


    for x in range(2):
        num_nodes = random.randint(5,100)
        l, u = 0, random.randint(num_nodes,500)

        wgtOption = [1, 2, 3, 4, 6, 7, 8, 10]
        print('Vertex {} and Edges {}'.format(num_nodes,u))
        nodes=[x for x in range(num_nodes)]
        adj=[]
        for x in range(u):
            chs = random.choice(nodes)
            chs2 = random.choice(nodes)
            inc = random.choice(wgtOption)
            adj.append(Edge(chs,chs2,inc))
            

        
        total=0
        for x in range(1,3):

            t=time.perf_counter()
            Graph(num_nodes, adj).KruskalMST(x)
            
            t2=time.perf_counter()
            t=t2-t
            print('time  {} takes {:3f} ms'.format(mp[x],t * 1000))
            total+=t
        print('total={:.2f} ms\n'.format(total*1000))


if __name__ == "__main__" :
    main()
