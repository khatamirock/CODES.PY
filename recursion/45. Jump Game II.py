



# nums =[1,2,3]
nums=[5,4,3,2,10,1,4]
# nums=[1,2,4,5,2,4,2,3,6,7,6,5,4,4,6,7,8,9,7,6,5,4,3,2,3,4,5,6,5,4,2,4,5,7,5]
# formulate the recursive solution |
# for min, max and counting ways...
rem={}
ln=len(nums)-1
def hlp(ind):
    if ind>ln:
        return 0
    if ind in rem:
        return rem[ind]
    mini=999999999
    for i in range(ind+1,ind+nums[ind]+1):
        l=hlp(i)
        mini=min(mini,1+l)
        rem[i]=l

    return mini


print(hlp(0))
