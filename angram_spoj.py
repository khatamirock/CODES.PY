
def angram(S,n):
    d=[]
    ss = ''.join(sorted(S[0]))
    for x in S:

        if(len(x)==len(ss)):

            #print(x)
           # print(len(x) )
            s= ''.join(sorted(x))
            if(ss==s):
                #print('paic')
                d.append(x)
               # S.remove(x)

    return d

def anagrams(S): # S is a set of strings
  d = {}
  for word in S:
    s = ''.join(sorted(word))


    if s in d: ## if thats in the dictionary then append else you have to crete one... CAREFUl
        d[s].append(word)
    else:
        d[s] = [word] # add a new signature and its first word # -- extract anagrams,
                  # adding as list.....
  #print(d)
  return [d[s] for s in d if len(d[s]) > 1] ## returning the list of the each dictionaries.....
     ## d[s] the value for each key s in d it returns d[s] the values it contains if its grater than 1....

def predictive_text(dic): #  total_weight[p] = total weight of words having prefix
    total_weight = {}
    for word, weight in dic.items():
        print(word)
        print(weight)


if __name__=='__main__':
    str = 'below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel'

    ar_str=str.split(' ')
    #print(ar_str[2])
#     for x in range(len(ar_str)):
# #        ls=angram(ar_str,x)
#         for x in range(len(ls)):
#             #print(ls[x],end='..')
#             ar_str.remove(ls[x])
#
#         print(ls)
    print('\n')

    ss=anagrams(ar_str)
    print(ss)
    ict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
    predictive_text(ict)