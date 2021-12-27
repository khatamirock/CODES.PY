# A naive recursive implementation of 0-1 Knapsack Problem

# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0 :
		return 0

	# If weight of the nth item is more than Knapsack of capacity
	# W, then this item cannot be included in the optimal solution
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
				knapSack(W, wt, val, n-1))

# end of function knapSack

# To test above function
xx=list(map(int,input('Weight').split()))

print(xx)
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(n,end='poster boii>>>>>>>>>>>>>iboii>>>>>>>>>>>>>boii>>>>>>>>>>>>>boii>>>>>>>>>>>>>boii>>>>>>>>>>>>>boii>>>>>>>>>>>>>boii>>>>>>>>>>>>>\n\n')

print (knapSack(W, wt, val, n))

n = 3


#####################
# knapsack with memoization..................................


mem = [[0] * 3 for i in range(55)]
# orders can be changes range(55) or range(3) and [0]*3 or [0]*55.... that means we need only to sotre data....
# nothing much

def knapscak(W, wt, val, n):
	# remember the changalbe values cause that is the only thing that needs to be
	# stored...................in this case thats.... n and W......................
	if n == 0 or W == 0:
		return 0
	if mem[W][n - 1] != 0:
		## here also we can use mem[W][n-1] or mem[n-1][W]

		return mem[n - 1][W]

	# If weight of the nth item is more than Knapsack of capacity
	# W, then this item cannot be included in the optimal solution
	if wt[n - 1] > W:
		return knapscak(W, wt, val, n - 1)
	else:
		mx = max(val[n - 1] + knapscak(W - wt[n - 1], wt, val, n - 1), knapscak(W, wt, val, n - 1))
		# mem[n][W] = mx
		return mx


val = [60, 100, 120]
wt = [10, 20, 30]
n = 5

print(mem)
print(knapscak(50, wt, val, len(val)))
