from typing import List


class Solution2:
    def __init__(self):
        self.partitions = []  ## global clusterfucnk

    def func(self, partition, s):
        n = len(s)

        # Potentially redundant
        if n == 0:
            self.partitions.append(partition)
            return

        if n == 1:
            self.partitions.append(partition + [s])
            return

        for i in range(1, n + 1):
            # We loop from 1 to n + 1, because otherwise, the empty string
            # would always be a palindrome and the recursion wont terminate
            next_partition = s[:i]
            if next_partition == next_partition[::-1]:  # palindrome testing
                self.func(partition + [next_partition], s[i:])

    def partition(self, s: str) -> List[List[str]]:
        self.func([], s)
        return self.partitions


class Solution:
    def isPalin(self, seg):
        i = 0
        j = len(seg) - 1
        while (i < j):
            if (seg[i] != seg[j]):
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s: str):
        if (len(s) == 0 and len(self.temp) > 0):
            self.res.append(self.temp[:])
            return
        n = len(s) + 1
        for i in range(1, n):
            seg = s[0:i]
            if (self.isPalin(seg)):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s)
        return self.res


def trk(s, tm):
    if s == '':
        print('??')
        return
    for x in range(1, len(s) + 1):## for printing and traverse all the partition multilpe times...
        sf = s[:x]
        pf = s[x:]
        if sf == sf[::-1]:
            print(sf)
            trk(pf, '')


dl = Solution()
ss = 'aabas'
dl.partition(ss)

print(dl.isPalin(ss))
print(dl.partition(ss))

trk(ss, '')