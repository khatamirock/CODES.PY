ar = [1,2,4,6,7,10]
l, r = 0, 1
ln = len(ar)
## ❤leetcode (1838) >>>  Frequency of the Most Frequent Element Frequency of the Most Frequent Element
import random
ar.sort()
s = k = 2
upto = [0] * (ln)
for x in range(ln - 1):
    upto[x + 1] = ar[x + 1] - ar[x]

print(upto)
mx = 0

addto = 0
cn = 0
for x in range(1, ln + 1):
    addto = upto[-x]
    cn = 0
    p = x

    while p <= ln - 1 and addto <= k:
        cn += 1
        k -= addto
        p += 1
        addto += upto[-p]
    k = s
    mx = max(mx, cn + 1)

    print(ar[-x], upto[-x], addto)
print(mx)
