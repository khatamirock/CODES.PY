t9 = "22233344455566677778889999"
    # abcdefghijklmnopqrstuvwxyz mapping on the phone
def letter_to_digit(x):
    assert 'a' <= x <= 'z'
    return t9[ord(x) - ord('a')]
def code_word(word):
        return ''.join(map(letter_to_digit, word))

def predictive_text(dic):
    # total_weight[p] = total weight of words having prefix p
    total_weight = {}
    for word, weight in dic.items():
        prefix = ""

        for x in word:
            prefix += x
            if prefix in total_weight:
                total_weight[prefix] += weight
            else:
                total_weight[prefix] = weight # prop[s] = prefix to display for s
    prop = {}
    print(total_weight)
    for prefix in total_weight:

        code = code_word(prefix)
        print(prefix, end='{} >>>  '.format(code))

        if ( code not in prop or total_weight[prop[code]] < total_weight[prefix] ):
            prop[code] = prefix
    return prop

def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    return None
if __name__=="__main__":
    dic={'hell': 3,
'hello': 4,
'idea':8,
'next': 8,
'super': 3}

    dic2=  predictive_text(dic)
    print('\n\n')
    print(dic2)
    xx=propose(dic2,'4')

    print(xx)
