from collections import deque
import statistics

###############################################
def retmd(ar):## returns the median.....
    mdn = int(d / 2)
    if (d % 2 != 0):
        mdn = aa[mdn]
    else:
        mdn = (aa[mdn] + aa[mdn - 1]) / 2
    return mdn

import bisect
n, d = map(int, input().split())

#a= [2, 3, 4, 2, 3, 6, 8, 4, 5]
a= list(map(int,input().split()))

cnt=0
cn=0
aa=sorted(a[:d])

for x in range(n-d):
    dd=retmd(aa)
    if(a[x+d]>=2*dd):
        cnt+=1
    del aa[bisect.bisect_left(aa,a[x])] ###
    bisect.insort(aa,a[x+d])
    ##print(a[x],'rem  ',aa, '>>> ', a[x + d])

    ##pass
print(cnt)
