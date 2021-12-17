

def perma(nums):
    # base case
    results = []
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        # remove the first element always
        n=nums.pop(0)
        prm=perma(nums) ## recursive call
        ## all the recursuve calls list are returned here and
        ## added to that
        for pr in prm:
            pr.append(n)
        results.extend(prm)
        nums.append(n)
    return results

print(perma([1,2,3,4]))







