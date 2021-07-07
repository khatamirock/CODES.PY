import random

def bubbleSort(x):
    arr =  [int(11 * random.random())+1 for y in range(x)]
    n = len(arr)
    cn=0
    # Traverse through all array elements
    for i in range(n):
        cn+=1
        # Last i elements are already in place
        for j in range(0, n-i-1):
            cn+=1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return cn

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
    myList = [int(11* random.random()) for _ in range(x)]
    # print(myList)
    maxValue = 0 ## decrease the couonting... dramatically
    cn=0
    for i in range(len(myList)):
        cn+=1
        if myList[i] > maxValue:
            maxValue = myList[i]
            ''' finding the max....'''
    # print(maxValue)
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
xs = list(range(5, 100))

ys = [bubbleSort(x) for x in xs]


plt1=plt.figure(1)
plt.plot(xs, ys,color='red')



ys2=[cSt(x) for x in xs]

plt.figure(2)
plt.plot(xs, ys2,color='black')

plt.title('Step Count..')
plt.xlabel('Number of element')
plt.ylabel('Steps for sorting')

plt.legend(['Bubble_Sort','Countng_Sort'])

plt.show()



'''import random
import time
import matplotlib.pyplot as plt

random.seed(5040)


def create(n):
    fin_ar = [random.randint(1, 10000) for y in range(n)]
    # print(fin_ar)
    with open(str(n) + 'k.txt', 'w') as f:
        print('generating file for ', str(n // 1000), 'k\n')
        for a in fin_ar:
            f.write(str(a) + '\n')
    return fin_ar


def bubbleSort(final_arr):
    aa = time.time()
    arr = final_arr
    n = len(arr)
    cn = 0
    # Traverse through all array elements
    for i in range(n):
        cn += 1
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            cn += 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    bb = time.time()
    return (bb - aa)


def cSt(final_arr):
    aa = time.time()
    myList = final_arr
    # [int(11* random.random()) for _ in range(x)]
    # print(myList)
    maxValue = 0  ## decrease the couonting... dramatically
    cn = 0
    for i in range(len(myList)):
        cn += 1
        if myList[i] > maxValue:
            maxValue = myList[i]
            ''' finding the max....'''
    # print(maxValue)
    buckets = [0] * (maxValue + 1)  # empty array...

    for i in myList:
        buckets[i] += 1  # empty arr+=1
        cn += 1  # counter...

    i = 0
    for j in range(maxValue + 1):
        cn += 1
        for a in range(buckets[j]):
            cn += 1
            myList[i] = j
            i += 1

    bb = time.time()

    return (bb - aa)


xs = xs = list(range(1000, 10000, 1500))
print(xs, '||| number of elemtns in each array')
ys = [cSt(create(x)) for x in xs]

plt.figure(1)
plt.plot(xs, ys, color='black')
plt.xlabel('Number of element')
plt.ylabel('time(s) for sorting')

ys2 = [bubbleSort(create(x)) for x in xs]
plt.figure(2)
plt.plot(xs, ys2, color='red')
plt.xlabel('Number of element')
plt.ylabel('time(s) for sorting')

plt.show()
'''
