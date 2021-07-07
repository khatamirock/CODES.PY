import random
import time
import matplotlib.pyplot as plt
random.seed(5040)


def create(n):
  fin_ar = [random.randint(1, 10000) for y in range(n)]
  print(fin_ar)
  with open(str(n) + 'k.txt', 'w') as f:
    print('generating file for ', str(n // 1000), 'k\n')
    for a in fin_ar:
      f.write(str(a) + '\n')
  return fin_ar

def bubbleSort(final_arr):
  aa = time.perf_counter()
  arr = final_arr
  n = len(arr)
  cn = 0
  for i in range(n):
    cn += 1
    for j in range(0, n - i - 1):
      cn += 1
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  bb = time.perf_counter()
  return (bb - aa)


def Csort(final_arr):
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


### dont run....................


###########################################################
##   main section..........

xs = list(range(1000, 11000,1500))
[create(x) for x in xs ] ## generates .txt file
## xs contains the list of number of elements in each txt file....

ys1=[]
ys2=[]
for x in xs:
  f=open(str(x)+'k.txt','r')
  ls=[]
  ## reads from the .txt file and created  list..>>>
  ## needs time for operation....
  for x in f:
    ls.append(int(x))
  # print(ls)
  ys1.append(Csort(ls))
  ys2.append(bubbleSort(ls))

## platting...................
plt.figure(1)
plt.plot(xs, ys1,color='black')
plt.xlabel('Number of element')
plt.ylabel('time(s) for sorting')

plt.figure(2)
plt.plot(xs, ys2,color='red')
plt.xlabel('Number of element')
plt.ylabel('time(s) for sorting')


plt.show()