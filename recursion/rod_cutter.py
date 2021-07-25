

import sys


# A utility function to get the
# maximum of two integers
def max(a, b):
    return a if (a > b) else b


def cutRod(price, n):
    if (n <= 0):
        return 0
    max_val = -sys.maxsize - 1 ### similar to the longestString_Chain..................
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val


arr =[1,5,8,9,10,17,20,4,5,6,34,5,56,7,8,5,6,3,45,2,34,24,5,45,64,7,8,78,69,45,45,34,23,41,23]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr, size))


''' almost same as stairWay problem.... (not fully)..'''
# my implement..........  FASTER>>>>>>>>>>>>>>>>>>>>
###
'''  see drive DYNAMIC PROGRAMMING-I for more visual.....
prc= [1,5,8,9,10,17,20,4,5,6,34,5,56,7,8,5,6,3,45,2,34,24,5,45,64,7,8,78,69,45,45,34,23,41,23]
remem={}
def cutter(currN):
    if currN<=0:
        return 0
    curVal=-99999
    for x in range(currN):
        if not currN-x-1 in remem:
            go=cutter(currN-x-1)
            curVal=max(curVal, prc[x]+go)
            remem[currN-x-1]=go
        else:
            curVal=max(curVal,prc[x]+remem[currN-x-1]) ### the longString version is 
                                    1(the value initailly(if mentioned.) + rec()...
    return curVal

print(cutter(len(prc)))

'''


## more Older version>>>>>>>>>>>>>>>>>>>>>>>>>>

'''

prc= [1, 5, 8, 9, 10, 17, 17, 20]

ar=[1,5,6,7,8]


def cutter(currN):
    if currN<=0:
        return 0
    curVal=0
    for x in range(currN):
        curVal=max( curVal, prc[x]+cutter(currN-x-1) )
    return curVal

print(cutter(len(prc)))





'''

