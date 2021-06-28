


############### best sol so far,,,,,,,,,,,,,,,,,,
a=[0 ,0,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1]
k,n=3,len(a)

print(a)
prv=[0]*len(a)

last=-1
for x in range(len(a)):
   if a[x]==1:
      last=x
   prv[x]=last

ans=0
print(prv)
ii=0
for i in range(len(a)):
   take=prv[min(ii+k-1,n-1)]## when the ii+k-1 is greater than the n itsef we take the n-1 ...
   if take!=-1 and take==n-1:
      ans+=1
      break
   if(take==-1 or take+k<=ii):
      print(-1)
      exit()
   ii=take+k
   ans+=1
print(ans)