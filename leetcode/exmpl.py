#return kth permutation of n numbers

def kthPermutation(n, k):
    nums = [i for i in range(1, n+1)]
    res = []
    k -= 1
    while nums:
        i = k % len(nums)
        res.append(nums[i])
        nums.pop(i)
        k //= len(nums)
    return res
def kthPermutation2(n, k):
    nums = [i for i in range(1, n+1)]
    res = []
    k -= 1
    while nums:
        i = k % len(nums)
        res.append(nums[i])
        nums.pop(i)
        k //= len(nums)
    return res
print(kthPermutation2(3,3))
