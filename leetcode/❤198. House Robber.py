
ar=[4,1,5,8,2,6,5,8,9]
l,r,ln=2,3,len(ar)

def rob(nums):
    if not nums:
        return 0

    if len(nums) < 3:
        return max(nums)

    for i in range(2, len(nums)):
        if i == 2:
            nums[i] += nums[i - 2]
        else: ###                               except the 3rd element....>> we choose strictly 1st elemnt...
            nums[i] += max(nums[i - 2], nums[i - 3])  ## every time i need to choose the previous 2 elements...
                    ### and it extends untill the end.... so we make progress,,,,,,,,,,
    print(max(nums[-2:]))
    return max(nums[-2:])

# ar=[4,1,5,8,2,6,5,8,9]
ar=[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# ❤ ❤ ❤ ❤
mm={}
def robber2(arr):## in this type of array bsed problem we cant use the dictionary. to use as memoization
    ### thats why we another list.... called sliding window or something

    if not  arr:
        return
    if len(arr) < 3:
        return max(arr)
    return max(arr[0]+robber2(arr[2:]), robber2(arr[1:]))
# ar=[1,2,3,1]
# print(rob(ar),'>>>1')
print(robber2(ar),'>>>2)')
print(ar)
print(ar[:-1])














