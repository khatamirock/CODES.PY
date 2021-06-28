
from collections import Counter


def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i * r in dictPairs:
            count += dictPairs[i * r]
        if i * r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]

        dict[i] = dict.get(i, 0) + 1

    return count

def printNcR(n, r):

    p = 1
    k = 1

    if (n - r < r):
        r = n - r

    if (r != 0):
        while (r):
            p *= n

            m = math.gcd(p, k)

            p //= m
            k //= m
            n -= 1
            r -= 1
    else:
        p = 1
    return p


import math


def fct(a):
    return math.factorial(a)

n,mlt=map(int,input().split())
arr=list(map(int,input().split()))

# cnter=Counter(arr)
# tot=0
#
# ar=sorted([x for x in cnter])
#
#
# for x in range(len(ar)-2):
#     i,j,k=ar[x],ar[x]*mlt,ar[x]*mlt*mlt
#     #print(i,j,k)
#     #print(cnter[i],cnter[j],cnter[k],end=' >>> ')
#     if(cnter[i]==0 or cnter[j]==0 or cnter[k]==0):continue
#     tot+=int((printNcR(cnter[i],1)+printNcR(cnter[j],1)+printNcR(cnter[k],1))/2)


print(countTriplets(arr ,mlt))
