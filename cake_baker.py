



if __name__=='__main__':
    zro=[0 for _ in range(3)]

    ar1=[2,3,1]
    br2=[4,2,3]
    for x in range(1,4):

        for y  in range(1,4):
            s=(x+y)%3
          #  print(s,end=' >>>{} and {} ....'.format(ar1[s],br2[x]))
            zro[s]+=ar1[s]*br2[x-1]


        print('\n')
    print(zro)