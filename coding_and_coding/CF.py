
s='1912'
re=''
m=100

a=0
ln=0
for x in (s):

    ad=int(x)
    re=ad+m
    #print(re)
    ln+=len(str(re))

print(ln%(10**9+7))