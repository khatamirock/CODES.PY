# Python3 implementation of the approach


def dpt():
    return (input().split())


v = int(input('Enter number of vertices: '))

sa = []
print('Enter graph daata in matrix Form:')
for x in range(v):
    sa.append(list(map(int, dpt())))
print(sa)

st = int(input('enter starting vertice: '))

print('\nThe node which are reachable are:')
visited = []
ans = [0]

def visq(st):
  qu = {st - 1}
  visited.append(st)
  while qu:

      en = qu.pop()
      for i, x in enumerate(sa[en]):
          if x == 1 and i + 1 not in visited:
              print(i + 1, end=' ')
              visited.append(i + 1)
              # ans.append(i+1)
              qu.add(i)

visq(st)

print(sorted(visited))


# This code is contributed by ng24_7
