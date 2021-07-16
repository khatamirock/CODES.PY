import random
import time

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

################  website solve....
def Csort(final_arr):

  myList = final_arr

  # print(myList)
  maxValue = 0  ## decrease the couonting... dramatically
  cn = 0
  for i in range(len(myList)):
    cn += 1
    if myList[i] > maxValue:
      maxValue = myList[i]
      ''' finding the max....'''
  # print(maxValue)
  buckets = [0] * (maxValue + 1) # empty array...[0,0,0,0,x,0,0,0,0,y,0,0,0,0,n,0,0,0,0,0,y,0,0,0,z,,,,,]

  for i in myList:
    buckets[i] += 1  # empty arr+=1
    # cn += 1  # counter...
  ''' end.....'''
  i = 0
  for j in range(maxValue + 1):

    for a in range(buckets[j]):
      cn += 1
      myList[i] = j
      i += 1

arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
Csort(arr)

print(arr)
