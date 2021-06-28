




if __name__=="__main__":

    dicnr={}
    arr=[5,3,5,4,5,4,2,6,2,5,]
    print('mannerMan')
    for x in range(len(arr)):
        if(arr[x] in dicnr):
            #dicnr[arr[x]].append([]);
            dicnr[arr[x]].append(list(arr[0:3]))
        else:
            dicnr[arr[x]]=[]
            dicnr[arr[x]].append(list(arr[0:3]))


    print(dicnr[5])
    for x, y in dicnr.items():
        print(len(y),end='...')
        print(x,y)


