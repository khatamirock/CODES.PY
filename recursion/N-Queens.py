# N-Queens - Backtracking - Leetcode 51 - Python
# NeetCode

from typing import List


col = set()
negD = set()  # determined by r-c....  ''' for the diagonals'''
posD = set()  # determined by r+c....
res = []
n = 4
board = [['*'] * n for _ in range(n)]


def bp():
    for x in board:
        print(x)
    print('------------------------')

solution=[]
retreat=[]

def backTrc(r):
    # bp()
    if r == n:
        copy = ['  '.join(row) for row in board]
        # print('solution >>>> ',solution)
        res.append(copy)  ## at the final state we're appending a variant of the result..... and then unfold

        ### everything to the original form................
        return

    for c in range(n):
        if c in col or (c + r) in posD or (r - c) in negD:
            # solution.append(c+1)
            # print(solution)
            # solution.pop()
            continue
        board[r][c] = 'Q'
        col.add(c)
        negD.add(r - c)
        posD.add(c + r)

        solution.append(c+1) ###solution place .....

        backTrc(r + 1)  ## only one simple case here....
        # print(retreat)
        # print(c+ 1, end='. ')
        solution.pop()

        col.remove(c)
        negD.remove(r - c)
        posD.remove(c + r)
        board[r][c] = '.'
#''' to understand backTack intuitively see,,,>>. '''# '''recursion/best_backTrack__recursion.py'''

    return res


retr = (backTrc(0))
for x in retr:
    for y in x:
        print(y)
    print(x)

# print(board)
