from collections import Counter
## why are you using counter broooooo....

def all_substrs(s):
    return [[s[j:j + i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]


def countem(ll):
    c = Counter()
    s = 0
    print(ll)
    for lst in ll:
        for e in lst:
            print(e)
            q = ''.join(sorted(e))

            c[q] += 1
    print(c)
    ## this functin is responsible for finding the paies ..... its maybe like the combination rule.....
    ## i dont know....
    print(e)
    ## it works as chossing  any 2 item 'e' number of items of the current sorted word
    ## works only if it greater than 2 cause we have to make a pair so lesser than 2 isnt allowed....
    for e in c:
        s += int(c[e] * (c[e] - 1) / 2) #4c2 +3C2+2C2....
    return s


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(countem(all_substrs(s)))