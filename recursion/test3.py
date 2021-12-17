

import collections
import time
import random

l,u=0,150
wgtOption=[1,2,3,4,6,7,8,10]
def adjListGEN(u):
  adj2=[]
  l=0
  for x in range(u):

    chs=(random.randint(l,u))
    chs2=(random.randint(l,u))
    inc=random.choice(wgtOption)
    adj2.append([chs,chs2,inc])
  return adj2


zONe=[0,0,1,0,1]
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
    # print([chs,chs2])


def mrxCONV(matrix):
    adj = []
    for i,row in enumerate(matrix):
        for j,col in enumerate(row):
            if col!=0:
                adj.append( [i,j,col] )
    return adj


## this is actually a variant of BFS |||||||||||| implemented by that.............
def byUnsArr(a,tm):
    s=time.perf_counter()
    edges=collections.defaultdict(list)

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




tm1=time.perf_counter()
gen=matrixGEN(100)
tm2=time.perf_counter()-tm1

arr=mrxCONV(gen)

print('for MATRX',byUnsArr(arr,tm2))


print('for ADJ list',byUnsArr(  arr ,0),'\n\n\n')


