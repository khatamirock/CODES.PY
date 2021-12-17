

mem={}
def stairs(n):
    if n==0:
        return 1
    if n<0:
        return 0
    if n in mem:
        return mem[n]
    mem[n]=stairs(n-1)+stairs(n-2)
    ## so the lession here is we have to look for the CHOICES we've been given
    #   and the choice is two in here///////////////////
    ## then we need to go forward with the choice...........
    return mem[n]
    # sum+=stairs(n-1,sum)+stairs(n-2,sum) # this was the first solution
    # return sum


print(stairs(5))













