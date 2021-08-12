
words = ["bdca","a","b","bca","ba","bda",]


st=set(words)
d={}

def ret(w):
    if w not in st: return 0
    elif w in d:
        return d[w]
    else:
        mx=0
        ln=len(w)   ### similar to the RodCutter.................
        for x in range(ln):
            mx=max(mx,  ret(w[:x]+w[x+1:]) + 1  )
        d[w]=mx
    return mx
w='bdca'
# for x=0,1,2,3,len()
''' >> w[:x]+w[x+1:]=dca for w==0### ''' # >>> and for dca ca,da,dc will occour
''' >> w[:x]+w[x+1:]=bca for w==1### '''
''' >> w[:x]+w[x+1:]=bda for w==2### '''
''' >> w[:x]+w[x+1:]=bdc for w==3### '''
for wr in words:
        # if len(wr)!=1:
            ret(wr)
print(max(d.values()))


