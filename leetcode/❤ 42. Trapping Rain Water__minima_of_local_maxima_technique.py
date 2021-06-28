from typing import List

ar= [0,1,0,2,1,0,1,3,2,1,2,1]
# ar=[0,1,2,0,3,1,1,1,4]
# ar=[4,2,0,3,2,5]

ln=len(ar)
last=ar[0]
first=ar[1]
cnt={}
po=1
ans=0
while po<ln-1:
    # print(ar[:po],ar[po:])

    lm=max(ar[:po])
    lm=max(ar[po],lm)

    rm=max(ar[po:])

    mm=min(lm,rm)
    ans+=(mm-ar[po]) # this means the water in the current platform....
    ###########
    po += 1

print(ans)


'   ..>>>> property of minima of local maxima....   '





' ### fast sol... [ extended.. two pointer  >>>>>>>>>>>> ] ....'
class Solution:
    def trap(self, ar: List[int]) -> int:
        if not ar:
            return 0
        left, right = 1, len(ar) - 2
        left_max, right_max = ar[0], ar[-1]
        ans = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, ar[left])
                ans += left_max - ar[left]
                left += 1
            else:
                right_max = max(right_max, ar[right])
                ans += right_max - ar[right]
                right -= 1

        return ans

