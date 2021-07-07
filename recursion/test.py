
dep=6
a=['0{}1','2']
sa='0{}1'
p=0
import  random
random.seed(438)

for x in range(10):
    print(random.choice(a))
def al(a,d):
    if d<dep:
        print(a.format('0a1'))
        al(a.format('0{}1'),d+1)
    else:
        print((a.format('')))

# al('0{}1',0)

# for two parameters or you can say
def aa(x,d):
    print(x)

    if d<dep:
        a('0a1',d)

    a('2',d)

    pass






# for x in range(6):
#     sa =sa.format('0{}1')
#     print(sa.format('0a1'))
# # print(a[p].format(a[1]),'>>>>>')
