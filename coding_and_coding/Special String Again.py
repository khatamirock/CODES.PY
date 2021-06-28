#
# from itertools import groupby
# ### theirs solution.........................
# from itertools import groupby
#
# def k_sum(k):
#     return (k*(k+1))//2
#
# def substrCount(n, s):
#     case_a = 0
#     case_b = 0
#
#     for x,y in groupby(s):
#         print(list(x))
#         print(list(y))
#         sm=sum(1 for i in x)
#
#         print(sm)
#         case_a += k_sum(sm)
#     for i in range(1,len(s)-1):
#         ## assume each character as center of a substring....
#         skip = 1
#         if s[i-skip] == s[i] or s[i+skip] == s[i]:
#             continue
#         match = s[i-skip]
#         while i-skip>-1 and i+skip<len(s) and s[i-skip]==match and s[i+skip]==match:
#             case_b += 1
#             skip += 1
#     print(case_a,case_b)
#     return case_a + case_b
#
# n = int(input())
# s = input()
# print(substrCount(n, s))
#
#
# from collections import Counter
# def substr(s):
#     cnt=0
#     if(len(Counter(s))==1):
#         print(int((len(s)*(len(s)+1))/2))
#         exit()
#
#         ##### error usage of 2 loooooopppppppppppppppp...........
#
#     for i in range(2,len(s)):
#        # print('for i >> ',i,end='  \n')
#
#         for j in range(len(s)-i+1):
#             sc=s[j:j + i]
#             if(len(sc)%2!=0):
#                 mdl=len(sc)//2
#                # print('1>>> ',sc)
#                 if( sc[:mdl]==sc[mdl+1:]):
#                   #  print('???')
#                     cnt+=1
#             else:
#                 if(sc == len(sc) * sc[0]):
#                    # print('???')
#                     cnt+=1
#     if(s==len(s)*s[0]):
#         cnt+=1
#     print(cnt+len(s))
from itertools import groupby

def substrCount(n, s):
    l = []
    count = 0
    cur = None
    y=groupby(s)### you can use it or let it do in the folloing loop....
    # 1st pass doing the work of groupby classs....
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count)) ## its not a counter its groupby class
    ### in hand implementation...
    ## so we cant use counter in this case...

   # print([list(y) for x , y in groupby(s)])
    print(l)
    ans = 0

    # 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2
    ########### >>>>>>> the combination making formula
    ## if its 3 then it will 1+2+3.....

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans

n=int(input())
s=input()
print(substrCount(n,s))