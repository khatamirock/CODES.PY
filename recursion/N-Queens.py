from typing import List

# mat=[[0 for x in range(4)] for x  in range(4)]
mat = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(mat)

for i, row in enumerate(mat):

    for j, col in enumerate(row):
        print(col, '({},{}) >'.format(i, j), end='')

    print()

col = set()
negD = set()  # determined by r-c....
posD = set()  # determined by r+c....
res = []
n = 5
board = [['.'] * n for _ in range(n)]
print(board)


def backTrc(r):
    if r == n:
        copy = [''.join(row) for row in board]
        res.append(copy) ## at the final state we're appending a variant of the result..... and then unfold
                            ### everything to the original form................
        return

    for c in range(n):
        if c in col or (c + r) in posD or (r - c) in negD:
            continue

        col.add(c)
        negD.add(r - c)
        posD.add(c + r)
        board[r][c] = '*'

        backTrc(r + 1)  ## only one simple case here....

        col.remove(c)
        negD.remove(r - c)
        posD.remove(c + r)
        board[r][c] = '.'

    return res


retr = (backTrc(0))
for x in retr:
    print(x)

# print(board)
