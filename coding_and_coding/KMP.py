def mx(w):
    n=len(w)
    f=[0]*n
    k=0
    for i in range(1,n):
        while w[k]!=w[i] and     k>0:
            k=f[k-1]
        if w[k]==w[i]:
            k+=1
        f[i]=k
    return f
ss='lilipolilil'
print(mx(ss))

def pwer(u):
    f=mx(u)
    print(f)
    n=len(u)
    if n%(n-f[-1])==0:
        return n//(n-f[-1])
    return 1

s='blablabla'
print(pwer(s))

print('>>>>',len(s)//(s+s).find(s,1))
print(len(s),(s).find(s,1))