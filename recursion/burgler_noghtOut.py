

ar=[3,8,10,4,1,7]
def brgl(n):

    for x in range(2,n):
        if x==2:
          ar[x]+=ar[x-2]
        else:
            ar[x]+=max(ar[x-2],ar[x-3])

    return max(ar[-2:])


print(  brgl(len(ar))  )




