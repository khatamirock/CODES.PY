lst3=[(0, 'a', 1,),(0, 'b' ,2 ),(1 ,'a' ,1),(1 ,'a', 2),(2 ,'b', 1),(2 ,'b', 3)
     ]
def trsn_stts(lst):
    dt={}
    for x in lst:
        #print(x[0])
        if( str(x[0]) in dt):

            ds= dt[ str(x[0])]
            #print(self.dt)
            if(str(x[1]) not in ds):
                #dt[x[0]]={x[1],x[2]}
                ds[x[1]]={ str(x[2])}
                ### cretates a whole new appointment......
            else:
                dt[ str(x[0]) ][ x[1]  ].add( str(x[2]) )  ## adding makes
                #######  {1,3} to {1,3,(someting) }..........

        else:
            dt[ str(x[0]) ]={x[1]:{str(x[2])}}
    return dt



#### rgex to detect all BD n

import re
text = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""

entries = re.split("\n+", text)
xx=[re.split(':?',text,3) for entry in entries]

trsn_stts(lst3)
