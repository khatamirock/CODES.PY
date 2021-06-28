s2='manoermanbar'
s1='ram'
import collections
def check0(s1,s2):
    m, n = len(s1), len(s2)
    ############very good example of finding lost array without any order in a huge string.....
    if m > n:
        print(-1)
        exit()
        # return False
    counter1 = collections.Counter(s1)
    counter2 = collections.Counter()
    sub_len, left = 0, 0
    for right, ch in enumerate(s2):
        counter2[ch] += 1
        sub_len += 1
        while counter2[ch] > counter1[ch]:
            counter2[s2[left]] -= 1
            sub_len -= 1
            left += 1
        if sub_len == m:
            print(1111)
            break
            # return True

############# another implementation........>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def checkInclusion(self, s1: str, s2: str) -> bool:

    need = collections.Counter(s1)
    window = {}

    left, right, valid = 0, 0, 0

    while right < len(s2):

        cr = s2[right]
        right += 1

        if cr in need:
            window[cr] = window.get(cr, 0) + 1
            if window[cr] == need[cr]:
                valid += 1

        while (right - left) == len(s1):

            if valid == len(need):
                return True

            cl = s2[left]
            left += 1

            if cl in window:
                if window[cl] == need[cl]:
                    valid -= 1
                window[cl] -= 1
    return False

def checkInclusion2(s1, s2):
    target = collections.Counter(s1)
    windw = collections.Counter()
    left = right = 0
    N = len(s2)
    M = len(s1)

    while right < N:
        curr = s2[right]
        windw[curr] += 1

        while windw and right - left + 1 > M:
            todel = s2[left]
            windw[todel] -= 1
            if windw[todel] <= 0:
                del windw[todel]

            left += 1
        print(windw)
        if windw == target:
            return True
        right += 1

    return False

checkInclusion2(s1,s2)