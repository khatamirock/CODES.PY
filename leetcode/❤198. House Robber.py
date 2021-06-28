
ar=[4,1,5,8,2,6,7,8]
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

rob(ar)
# ❤ ❤ ❤ ❤
