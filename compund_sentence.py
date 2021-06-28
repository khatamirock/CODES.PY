


if __name__=='__main__':
    
    str_ls=[]
    strs=''
    while 1:
        strs=input()
        if not strs:
            break
        else:
            str_ls.append(strs)
    #str_ls=['a','alien','born','less','lien','never','nevertheless','new','newborn','the','zebra',    'zebr']

    store=[]

   # print(dic)
    cnt = 0

    nstr_ls2=''
    for x in range(len(str_ls)):
        for y in range(x+1,len(str_ls)):
            nstr_ls2=str_ls[y]
            if(str_ls[y].__contains__(str_ls[x])):
               # print(str_ls[x], str_ls[y])
                nstr_ls=str(str_ls[y])
                nstr_ls=nstr_ls.replace(str_ls[x],'')
                #print(nstr_ls)
                if(str_ls.__contains__(nstr_ls)):
                    if(store.__contains__(nstr_ls2)==False):
                        store.append(nstr_ls2)
                        #str_ls.remove(nstr_ls2)



        #print('')
    for x in store:
        print(x)