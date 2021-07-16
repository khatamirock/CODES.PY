

############## stairWay to heavennnnnnnnnnnn

def stairs(n):

    if n<=1:
        return 1

    return stairs(n-1)+stairs(n-2)






''' pronlem the same ideology as the starWay problem '''
#########   Domino arrangements

def arrange(n):
    if n<=1:
        return 1

    return arrange(n-1)+arrange(n-2)


n=5
print( 'stairs>> : ' ,stairs(n)   ,  '| Dominos way :  ',arrange(n)  )



#...................


