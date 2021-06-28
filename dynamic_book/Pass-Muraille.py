
st,en=map(int,input().split())
a,b=map(int,input().split())

m,n=map(int,input().split())
apl=list(map(int,input().split()))
org=list(map(int,input().split()))

apCn=0
for x in apl:

    if a+x>=st and a+x<=en:
        # print('1 apl')
        apCn+=1
orCn=0
for x in org:

    if b+ x <= en and b+x>=st:
        orCn+=1
        # print('1 org')

print(apCn)
print(orCn)

#
# sapple = sum([1 for f in apple if (f+a) >= s and (f+a) <= t])
