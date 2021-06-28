1.
##  >> import bisect ## SEE: fraudal activiry...
## its a module that inserts an element into a right position in a sorted array and its very oprimized...
# >> bisect.insort(arr,elm)....  ## this is inserting the
    ### required d'th element into temp array at proper position
##>>>>>>>>>>>>>>>>>
2.
d = defaultdict(set) ## SEE: frequency queries _problem..
d[v].discard(y)  ## removign the y element from the [v] key...  good operation....
##>>>>>>>>>>>>>>>>>>>>>>>>>
3.
## you cant make operations on list as iterating
# else you will get the list index error......
# careful >...>>>> see  STRING MAKING ANAGRAM on -- HackerRank.....
##>>>>>>>>>>>>>>>>>>>>>>>>>

3.

##  for x,y in groupby(s):
    ## it works by making the group of the side by side same element..
    ##  if s='aaabbab'
    ## then y=['aaa','bb','a','b']
    # and x=['a','b','a','b']
############ remember you have to make a list of those or you
#  wont be able to see the inside of these containers,,,,,,,,,,,

##>>>>>>>>>>>>>>>>>>>>>>>>>
4.
dc={1: 1, 2: 2, 4: 1}
sm=sum(1 for x in dc if x==1)
## prints 2.... makes the sum increment by 1 if the x is 1 ....
5.
#   reverse strting with fastest computation is:
#   >>>>>>>>>>   s[::-1]

6.
# if the matter is all about division and mod and  these stuffs:
#         take a peak into the LCM and GCD ......

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
7.
# problem reagrading factorial (n!) you can try the>>>  log2(n!)    technique,,,,,
#     this helps for faster calculation.....
8.
#  COMMON CHILD >>>  longest common substrning is done in that,,.... good solutions.....

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
9.
# >>  from itertools import product ### see subset problem example....

## lessions,,,,,,,,,,,,,,,
#  print(*'123') >> 1 2 3
##  print(*['123','445','78']) >> 123 445 78 # each one becomes iterables....
# list(product(*['asd','sdf','rrr']))
# list(product(['asd','sdf','rrr']))>>> though it wont work,,,,cause theres only 3 iterbl,,,

10.
 # >>>>  m[x]=m.get(x,0)+1
# >>> it helps when theres no value firstly and make it zero then increase by one...:

11.
# say you have 5 2 6 arry and u need to add another number say 3:
# so how many sub array partitions are there now???
# ans=(right-left+1)
# cause it will form a whole array from 5-3
# another with 2-3
# anohter with 6-3
#     and other with the single elemnt itself........
#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>\

12.

so for array summ and add ,,,to make it in dynamic programming .... you have to think of making.. the
    ...   sum array .. on every iteation.... thing of adding the previous element or substracting them ...
        see the 198.House Robber >>> problem [Leetcode]....
    also the Goodlane electricity problem [hackerRank]//
#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>\
13.

# the good example for greedy is in leetcode>mostProfit || problem.....
# with many array handling.............

#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>\
14.

aar=[[1],[1,2,3],[2,3,4],[1,5],[3,4]]
x=max(aar,key=len)
#
# returns the first max lenght of array according to lenght()
#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>#>>>>>>>>>>>>>>>>>>>>>>>>>\






