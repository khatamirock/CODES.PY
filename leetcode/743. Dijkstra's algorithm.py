## https://www.youtube.com/watch?v=EaphyqKU4PQ
## channel neetcode>>>>>>>>>>>>>>>>>
'''best............'''
import heapq
import collections
# a=[[0,1,4],[1,3,1],[3,5,4],[0,2,2],[2,4,5],[4,5,10],[2,3,6]]


a=[[1,2,5],[3,2,8]]
edges=collections.defaultdict(list)

## this is actually a variant of BFS ||||||||||||

for x,y,z in a:
    edges[x].append((y,z))

k=a[0][0]
print(k)

nHeap=[(0,k)]
visited=set()
t=0
while nHeap:
    w1,n1=heapq.heappop(nHeap)
    if n1 in visited:
        continue
    visited.add(n1)
    t=max(t,w1)

    for n2,w2 in edges[n1]:
        if n2 not in visited:
            heapq.heappush(nHeap,(w1+w2,n2))


print(len(visited))
print(t)





