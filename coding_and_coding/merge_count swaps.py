def merge(a, l, m, h):
    c = []
    i = l
    j = m + 1  # after the point of middle...........
    s = 0  ## the counter.....
    print(a, 'for the >>>> ', l, m, h, '|||||||| ')
    while i <= m and j <= h:
        if a[i] > a[j]:
            # there is an inversion
            s += (m - i + 1)  ##                      m-i+1
            ###  this shit works as like shifting the position of the minimal elem of array on the bigger elem.
            ###  pos seeming the small elem is in the median and adding 1 to get the proper shift....
            ## and as one shifs other small is on the next to median as we imagine the first one....

            c.append(a[j])
            print(a, '>>> ', c, a[i], ' f ', a[j], '>>>', m, i, j, s)
            # print(s, m, i, m - i + 1,' >>>',c)    #/>>>>>>>>>>>>>>>
            j += 1
        else:
            ##print(s, m, i, m - i + 1, ' >else>>', c)
            print(a[i], ' el ', a[j])
            c.append(a[i])
            i += 1

    # Adding remaining numbers
    while i <= m:
        c.append(a[i])
        i += 1
    while j <= h:
        c.append(a[j])
        j += 1
    print(c, s)
    a[l: h + 1] = c

    return s


def count(a, l, h):
    if l >= h:  ## means there only one number now
        return 0
    # print(l, h)
    m = l + (h - l) // 2
    s = 0

    s += count(a, l, m)
    s += count(a, m + 1, h)

    s += merge(a, l, m, h)
    print('>>>>', s)
    return s


def count_inversions(a):
    return count(a, 0, len(a) - 1)


ar = list(map(int, input().split()))
print(count_inversions(ar))

print(ar)
