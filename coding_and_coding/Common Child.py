import sys


def main():
    a = [l for l in sys.stdin.readline().strip()]
    b = [l for l in sys.stdin.readline().strip()]

    a = [l for l in a if l in b]
    b = [l for l in b if l in a]

    print(a,b,(lcs(a, b)))


def lcs(a, b):
    lengths = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    # row 0 and column 0 are initialized to 0 already
    print(lengths)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = \
                    max(lengths[i + 1][j], lengths[i][j + 1])
    print(lengths)

    # read the substring out from the matrix
    result = lengths[-1][-1]
    # x, y = len(a), len(b)
    # while x != 0 and y != 0:
    #     if lengths[x][y] == lengths[x - 1][y]:
    #         x -= 1
    #     elif lengths[x][y] == lengths[x][y - 1]:
    #         y -= 1
    #     else:
    #         assert a[x - 1] == b[y - 1]
    #         result = a[x - 1] + result
    #         x -= 1
    #         y -= 1
    return result


if __name__ == "__main__":
    main()
