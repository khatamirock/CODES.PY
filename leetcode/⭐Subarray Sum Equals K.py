
def subarraySum( ar, k) :
    #### the cumulative sum perinter....
    sum = [0] * (len(ar) + 1)
    for x in range(1, len(ar) + 1):
        sum[x] = sum[x - 1] + ar[x - 1]
    ####     prev-elem + current-elm
    print(sum)
#######################
    hashmap = {}  # index:frequency

    # start the hashmap with 0 size or we already have a hashmap of size 0, 1time or we already have subarraySum of size 0 , 1time
    hashmap[0] = 1
    sum_ = 0
    result = 0
    for i in range(len(ar)):
        sum_ += ar[i]  # calculate the cummulative sum

        # if the subarray is found
        if (sum_ - k) in hashmap:
            result += hashmap[sum_ - k]

        # if no subarray is found so keep on updating the hashmap with the frequency
        if sum_ in hashmap:
            hashmap[sum_] = hashmap[sum_] + 1  # we already have val in hashmap so update the frequency
        else:
            hashmap[sum_] = 1  # first time we are seeing the value.
    return result



ar=[1]
print(subarraySum(ar,0))



