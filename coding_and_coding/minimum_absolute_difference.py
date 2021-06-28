

def printJobScheduling(arr, t):
    # length of array
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit
    xx=sorted(arr,key=lambda x:x[2],reverse=True)

    print(arr)
    print(xx)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)
    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):

        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
#### the t-1 and the arr[i][1] - 1 means for the arr 0 index matchinng
        ### for that we minus 1 and for every elemet it can be placed from that palce upto 0....
        ## so we need to find the minumum between the limit and the postional value....

        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            ## for every larger value we want to place it from the last of its original pos
            ## if theeres already another val we place it before....
            ## and continue this...
            sa=t-1
            el=arr[i]
            sr=arr[i][1]-1
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # print the sequence
    print(job)


# Driver COde
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

print("Following is maximum profit sequence of jobs")

# Function Call
printJobScheduling(arr, 3)

# This code is contributed
# by Anubhav Raj Singh
