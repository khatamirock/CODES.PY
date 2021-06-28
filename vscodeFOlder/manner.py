import random


def maker(x):
    ar = [int(10 * random.random()) for y in range(x)]
    print(ar)
    dc = {x: 0 for x in range(1, x)}
    cn = 0
    cn += x
    for x in ar:
        cn += 1
        if x in dc:
            dc[x] += 1
        else:
            dc[x] = 1
    # print(ar)
    # print(dc)
    arr = []
    for x in dc:
        cn += 1
        # arr.append()
        if dc[x] != 0:
            for _ in range(dc[x]):
                cn += 1
                arr.append(x)
    # print(arr)
    return cn


def cSt(x):
    myList = [int(11* random.random()) for y in range(x)]
    # print(myList)
    maxValue = 0
    cn=0
    for i in range(len(myList)):
        cn+=1
        if myList[i] > maxValue:
            maxValue = myList[i]
            ''' finding the max....'''

    buckets = [0] * (maxValue + 1) # empty array...

    for i in myList:
        buckets[i] += 1 #empty arr+=1
        cn+=1# counter...

    i = 0
    for j in range(maxValue + 1):
        cn+=1
        for a in range(buckets[j]):
             cn+=1
             myList[i] = j
             i += 1

    return cn



import matplotlib.pyplot as plt


random.seed(5040)
size_of_cabinet = 10
xs = list(range(20, 90))

ys = [maker(x) for x in xs]


plt1=plt.figure(1)
plt.plot(xs, ys,color='red')
plt.title('Step Count-MY..')
plt.xlabel('Number of element')
plt.ylabel('Steps for sorting')



ys2=[cSt(x) for x in xs]


plt.plot(xs, ys2,color='black')
plt.title('Step Count-WEB..')
plt.xlabel('Number of element')
plt.ylabel('Steps for sorting')

plt.legend(['my code','webCode'])

plt.show()



