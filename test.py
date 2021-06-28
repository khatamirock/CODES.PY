import sys


def main():
    a = [l for l in sys.stdin.readline().strip()]
    b = [l for l in sys.stdin.readline().strip()]

    a = [l for l in a if l in b]
    b = [l for l in b if l in a]


    print((lcs(a, b)))


def lcs(a, b):
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # row 0 and column 0 are initialized to 0 already
    print(lengths)
    print(list(enumerate(a)))
    print(list(enumerate(b)))
    ## the first palce are ignored thats why we use i+1 and j+1 making the position one step ahead,,,
    ### also the reason we used the (len(a)+1) up for lengths()......
    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = \
                    max(lengths[i + 1][j], lengths[i][j + 1])
    m=len(a)
    n=len(b)
    print(lengths)
    ### see the difference.......
    ## tha main difference is about the if i==0 or j==0 conditon.....
    ###.................
    # for i in range(m + 1):
    #     for j in range(n + 1):
    #         if i == 0 or j == 0:
    #             a[i][j] = 0
    #         elif a[i - 1] == b[j - 1]:
    #             lengths[i][j] = lengths[i - 1][j - 1] + 1
    #         else:
    #             lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    #
    #

    result = lengths[-1][-1]

    return result


if __name__ == "__main__":
    main()