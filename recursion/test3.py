
# i=0
# ln=len(nums)
# x=nums[0]
# def retIN(ar,id):
#     i=0
#     mx=-999
#     for x in range(len(ar)):
#         if mx<=ar[x]:
#             i=x
#             mx=ar[x]
#     return i+id
# ind=0
# iii=0
# for _ in (nums):
#     if ind==ln-1:break
#     if nums[ind]>=ln-ind-1:
#         iii+=1
#         break
#     mx=retIN(nums[ind+1:ind+nums[ind]+1 ],ind )
#
#     iii+=1
#     ind=mx+1
# print(iii)

nums =[2,3,1,1,4]
ar=[0]+[9999 for _ in range(1,len(nums))]

print(len(nums),len(ar),nums,ar)

for x in range(1,len(nums)-2):
    for y in range(x-1,nums[x-1]+2):
        ar[y]=min(ar[x-1]+1,ar[y])


print(ar)




