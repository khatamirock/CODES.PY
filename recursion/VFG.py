rule = {
    's': ["the", "n", "b"],
    'n':['dog','cat'],
    'b':['bark','hooff'],
    'e':None

}


print(rule['s'])
possblX=[]

def cfg(x):
    if x in rule:
        for name in rule[x]:
            cfg(name)
            possblX.append(name)
    pass

for x in rule['n']:
    print(x)

cfg('s')
print(possblX)