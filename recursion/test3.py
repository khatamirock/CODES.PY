
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



