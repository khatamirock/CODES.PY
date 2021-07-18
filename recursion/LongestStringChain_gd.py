
words = ["a","b","ba","bca","bda","bdca"]


st=set(words)
d={}

def ret(w):
    if w not in st: return 0
    elif w in d:
        return d[w]
    else:
        mx=0
        ln=len(w)
        for x in range(ln):
            mx=max(mx,ret(w[:x]+w[x+1:])+1)
        d[w]=mx
    return mx





for wr in words:
    # if len(wr)!=1:
        ret(wr)

print( max(d.values()))