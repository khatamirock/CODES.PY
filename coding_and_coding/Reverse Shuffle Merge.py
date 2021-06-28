import string
from collections import Counter


def check():
    global pos

    c[ch] -= 1

    for p in range(pos, -1, -1):
        if s[p] == ch:
            cc = Counter(s[0:p])
            for k in c.keys():
                if cc[k] < c[k]:
                    c[ch] += 1
                    return False
            pos = p - 1
            return True
    return False


s = 'eggegg'
c = Counter(s)
for k in c.keys():
    c[k] //= 2

pos = len(s) - 1

length = len(s) // 2
ans = ''
while len(ans) < length:
    for ch in string.ascii_lowercase:
        if c[ch] > 0 and check():
            ans += ch
            break

print(ans)