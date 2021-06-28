
difficulty=[7,68,20]
profit=[26,28,56]

worker=[71,20,16]
jobs = sorted(zip(difficulty, profit))

ans = i = best = 0
worker.sort()
for skill in worker:
    while i < len(jobs) and skill >= jobs[i][0]:
        best = max(best, jobs[i][1])
        i += 1
    ans += best
print(ans)
#### my impl...............>>>||
# lastPos=0
# print(profit)
# difficulty, profit = [[e[i] for e in jobs] for i in range(2)]
#
# print(profit)
# for x in worker:
#     if x in dc:
#         ad+=str(x)
#         ans+=profit[dc[x]]
#         lastPos=dc[x]+1
#
#     else:
#         mm=max(diff[:lastPos+1])
#         if mm<=x:
#             ans+=profit[dc[mm]]
#             lastPos = dc[mm]+1
# print(ad)
# print(ans)







# ❤ ❤ ❤ ❤