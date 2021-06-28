#!/bin/python3

import os
import sys
import math
from itertools import permutations

#
# Complete the beautifulPermutations function below.
#
def beautifulPermutations(arr):
    n = len(arr)
    r = n - len(set(arr))
    c = 0
    print(n, r)
    a = 1
    d = math.factorial(n) // 2 ** r
    for i in range(r + 1):
        c = (c + a * (math.factorial(n - i)) * ((-1) ** i) // (2 ** (r - i))) % 1000000007
        a = (a * (r - i) // (i + 1))
        print(a,c)
    return c % 1000000007




arr = list(map(int, input().rstrip().split()))

result = beautifulPermutations(arr)
print(result)


st=['ab','bc','cd']

asd=permutations(st,3)

print(list(asd))