from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    count = 0
    g.sort()
    g.reverse()
    s.sort()
    for child in g:
        for i, cookie in enumerate(s):
            if child <= cookie:
                count += 1
                s.pop(i)
                break
    return count


t1 = findContentChildren(g=[1, 2, 3], s=[1, 1])
print("t1", t1)

t2 = findContentChildren(g=[1, 2], s=[1, 2, 3])
print("t2", t2)
