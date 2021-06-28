from collections import Counter
import math
def nCr(n, r):
    return (fact(n) / (fact(r)
                       * fact(n - r)))


# Returns factorial of n
def fact(n):
    res = 1

    for i in range(2, n + 1):
        res = res * i

    return res
# [1,1,1,3,3,3,7]
def countPairs(deliciousness):
    poweroftwo = [1 << i for i in range(22)]
    d = Counter(deliciousness)
    finale = 0
    for v in d:
        for pot in poweroftwo:
            tt = (pot - v)
            # if v == tt and d[v]>1:
            #     finale +=nCr(d[v], 2)

            if tt in d:## duplicate removal...## this means if v is bigger than tt its already taken.....
                if d[tt]>=2 and tt==v:
                    finale += nCr(d[v], 2)
                elif v<tt:
                    finale += d[v] * d[tt]
    # return finale % 1000000007
    print(int(finale))



## best sol 890ms
##>>>>>> the main diff is visit master this.....
## HOW TO store and remenber the visits....

def countPairs2( deliciousness) :
    pow_of_2 = set([2 ** i for i in range(0, 22)])
    MOD = 10 ** 9 + 7

    cnt = Counter(deliciousness)

    res = 0
    visit = set() ## when firstly i take 1 with 7 ,,1 id added...
    ## but when we key =7 the time when we choose 1 it should be avoided...

    for key, val in cnt.items():
        for n in pow_of_2:
            if n - key in cnt:
                if n - key == key:
                    res += val * (val - 1) // 2 ##
                else:
                    if n - key not in visit:
                        res += val * cnt[n - key]
        visit.add(key)
    return res % MOD


# countPairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]  )
countPairs2([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]  )

