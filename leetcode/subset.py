from typing import List

ar = []

tmp = []


def fnc(arr, ar, tm, i):
    if i >= len(arr):
        return
    ar.append(tm[:])   ### the error is in here............. if you do .append(tmp) it wont work.....
    ## cause if you dont make a different copy it will sometime become empty
    ### so eventually everyone else will also be empy....
    for x in range(i,len(arr)):
    ### again if you dont add index in range(i,len(arr))>>> it will cause duplicate.....
        if arr[x] not in tm:
            tm.append(arr[x])## add korbo......
            fnc(arr, ar, tm, x)
            tm.pop()### add korbo nah...............

    return


class Solution:
    def solution(self, nums, ans, cur, index):
        if (index > len(nums)):
            return
        ans.append(cur[:])
        for i in range(index, len(nums)):
            if (nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums, ans, cur, i)
                cur.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # accepts nums as list and returns List of list(int's)
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans


inn = [1, 2]
a=[]

fnc(inn,a,[],0)
sl = Solution()

# ar = sl.subsets(inn)

sl.solution(inn, ar, [], 0)











import itertools
from typing import List
from itertools import product

data = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        return

cc=Solution2()
def dd(digits):
    return ["".join(x) for x in product(*[data[d] for d in digits])]

print(dd('345'))
dgt='24'
d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
# for x in product(*[data[d] for d in dgt]):
#     print(x)

print(dgt)
ls=([data[x] for x in dgt])

print(*[data[x] for x in dgt])

# print(list(product(*[data[x] for x in dgt])))

print(list(product(*[x for x in ls])))

## lessions,,,,,,,,,,,,,,,
#  print(*'123') >> 1 2 3
##  print(*['123','445','78']) >> 123 445 78 # each becomes iterables....
# list(product(*['asd','sdf','rrr']))
# list(product(['asd','sdf','rrr']))>>> though it wont work,,,,

#> so conclution is * makes the item in list
##> iterable again in function call time.... even the strings become an iterable objects.....
###> and it must be used in  function to work....
## exmpl:
        # def roll(*dice):
        # ...     for x in dice:
        # ...         print(x)
        # ...
        # roll(3,4,5,1)
                # 3
                # 4
                # 5
                # 1
## lsls=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# exmpl >> print(list(zip(*lsls)))
# >> [(1, 2, 3), (4, 5, 6), (7, 8, 9)]