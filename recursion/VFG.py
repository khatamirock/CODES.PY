import random
rule = {
    "E": ["NP VP", "Interj NP VP"],
    "NP": ["Det N", "Det N that VP", "Det Adj N", "Det N PP"],
    "PP": ["Prep NP"],
    "Prep": ["in", "on", "over", "against"],
    "VP": ["Vtrans NP", "Vintr"],
    "Interj": ["oh,", "MY!!", "wow,", "damn,"],
    "Det": ["this", "that", "the"],
    "N": ["amoeba", "dichotomy", "seagull", "trombone", "corsage", "restaurant", "suburb"],
    "Adj": ["bald", "smug", "important", "tame", "overstaffed", "luxurious", "blue"],
    "Vtrans": ["computes", "examines", "foregrounds", "prefers", "interprets", "spins"],
    "Vintr": ["coughs", "walks", "whines", "slobbers", "vocalizes", "sneezes"]
}
# rule = {
#     'E': [
#         'the F T' # one only...
#     ],
#     'F': ['dog','cat' ,'man' ,'batman' # chosing from 4 item...
#           ],
#     'T': ['woof','meow', 'fisss', 'howl', 'btmn']
# }

arr = []


def xpn(start):
    if start in rule:
        chc = random.choice(rule[start])
        # print(chc)
        for x in chc.split():  ## == for x in chc: (rule down)
            xpn(x)
    else:
        arr.append(start)
    return (arr)


#
for x in range(5):
    print(xpn('E'))
    arr=[]

print(arr)
