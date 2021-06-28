input()

arr=list(map(int,input().split()))

minn=min(arr)

cnt=0

for x in arr:
    if minn==x:
        cnt+=1
    if minn & x!=minn:
        print(0)
        exit()

# *************  the property of and is that when we and two elements we left out with the min element or the less....
######################### so while and we have to find the min elements that stays in both sides....
#************************ >>>>>>>>>>
fct=1# this part is the nCr part .....
mod=10**9+7### what is done here is ,..... taking the (cnt.C.2)*2! and multiplying the rest (n-2)! elm with that,,,,,
########    means im taking 2 elem from the cnt item and rearanging them among themselves in 2! ways...
########### the other (n-2) elem can rearange in (n-2)! ways.....
for x in range(1,len(arr)-1):
    fct=(fct*x)%mod
ans=(cnt*(cnt-1))%mod
ans=(ans*fct)%mod
print(ans)
