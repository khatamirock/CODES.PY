st='{{{}}}{{}}{{{{{}}}}}'
a=[4,5,6,1,3,7,2,3]

print('max broski....',max( i for i in a))
lf='{'
rt='}'

pos=0
old=0
big=old
for x in range(len(st)):
    print(pos,old)
    old=pos
    if st[pos]==lf:
        pos+=1
        while st[pos]==lf:
            pos+=1
    old=pos-old
    if(big<old):
        big=old

    print(pos)

    print(st[pos:pos],st[pos:(pos*2)])
   ## new pos....

    pos=pos*2
    if(pos>=len(st)):break
print(big)