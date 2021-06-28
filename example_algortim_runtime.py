def insert_cabinet(cabinet,to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter
    while(check_location >= 0):
        ''' the first step counter in a loop....'''
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1

    ''' the last step counter'''
    stepcounter += 1

    cabinet.insert(insert_location, to_insert)
    return (cabinet)


def insertion_sort(cabinet):
    newcabinet = []
    global stepcounter
    while len(cabinet) > 0:

        stepcounter += 1
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet,to_insert)
    return(newcabinet)



import random
random.seed(5000)
xs = list(range(1,10))


def check_steps(size_of_cabinet):

    cabinet = [ int(500 * random.random())
               for i in range(size_of_cabinet) ]
    print(size_of_cabinet,'>> ', cabinet)
    global stepcounter
    stepcounter = 0
    sortedcabinet = insertion_sort(cabinet)

    return (stepcounter)



random.seed(5040)
size_of_cabinet = 10
xs = list(range(1,10))
ys = [check_steps(x)
      for x in xs]
# print(ys)
import matplotlib.pyplot as plt
plt.plot(xs,ys)
plt.title('Steps Required for Insertion Sort for Random Cabinets')
plt.xlabel('Number of Files in Random Cabinet')
plt.ylabel('Steps Required to Sort Cabinet by Insertion Sort')
plt.show()