
from collections import Counter,defaultdict
def freqQuery(queries): ##THIS IS THE OPTIMAL FUNCTION FOR THE PROPER USAGE....
    ###   THIS USES THE DICTIONARY REVALSAL(not totally) BUT GOOD
    ### {4: 2, 5: 2, 3: 0, 1:1} BECOMES....
    #  {0: {3}, 2: {4, 5}, 1:{1}}
    c = Counter()
    d = defaultdict(set)## this is so useful and important....
    ####     it creates a set inside the dictionary.... without any effort.... {0: {}, 1:{} }  ....
    for x,y in queries:
        v = c[y]
        print(d)
        print(c)
        print(x,y,v)
        if x==1:
            d[v].discard(y)  ## removign the y element from the [v] key... and adding that to another key (the next step actually +1 )...
            ## without removing it will have 2 copies in different keys without actual existance....
            d[v+1].add(y)
            c[y] = v+1
        elif x==3:
            yield 1 if d[y] else 0
        elif v:
            d[v].discard(y)
            d[v-1].add(y)
            c[y] = v-1

cmd=[]
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    cmd.append((x,y))
dct={}
scn=Counter() ## taking a counter.....
for x in cmd:
    #print(x[0],x[1]) 33 every command contains x[0] ,x[1] pair...
    if x[0]==1:

       scn[x[1]]+=1
       dct[scn[x[1]]]=x[1]### hudai...
    elif x[0]==2 and scn[x[1]]>0: ## making sure its not 0
        scn[x[1]]-=1
        #dct[scn[x[1]]] = x[1]
    elif(x[0]==3):
       # print(scn)
        cn=0
        N=0
        for xx in scn:## xx in every counter....
           #print(scn[xx],'>>',x[1])
           N+=1

           if(scn[xx]==x[1]):
               print(1)
               cn=1
               break
           if (N > len(scn) / 4+170):## breaking after sufficienet amount of searching if search goes to far...
               # ## case demans for that reason....
               break
        if(cn==0):
           print(0)
