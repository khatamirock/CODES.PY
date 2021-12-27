
n=3
from collections import defaultdict
# print(mem)
mem=[[0]*3 for i in range(55)]
# orders can be changes range(55) or range(3) and [0]*3 or [0]*55.... that means we need only to sotre data....
# nothing much

def knapscak(W, wt, val, n):
    # remember the changalbe values cause that is the only thing that needs to be
    # stored...................in this case thats.... n and W......................
    if n == 0 or W == 0:
        return 0
    if mem[W][n-1] != 0:
        ## here also we can use mem[W][n-1] or mem[n-1][W]

        return mem[n-1][W]


    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        return knapscak(W, wt, val, n-1)
    else:
        mx=max(val[n-1] + knapscak(W-wt[n-1], wt, val, n-1), knapscak(W, wt, val, n-1))
        # mem[n][W] = mx
        return mx






val = [60, 100, 120]
wt = [10, 20, 30]
n = 5

print(mem)
print(knapscak(50, wt, val, len(val)))
