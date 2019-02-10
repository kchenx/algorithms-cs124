from collections import deque
import sys

counter = 0

def merge(s, t):
    global counter

    n = len(s) + len(t)
    s.append((sys.maxint,0))
    t.append((sys.maxint,0))

    v = deque()
    scounter = 0
    for i in xrange(n):
        if s[0][0] < t[0][0]:
            for j in xrange(scounter, i):
                if v[j][1] != s[0][1]:
                    counter += 1

            v.append(s.popleft())
            scounter += 1
        else:
            v.append(t.popleft())
    return v

def mergesort(s):
    q = deque()
    while len(s) > 0:
        q.append(deque([s.popleft()]))

    while len(q) >= 2:
        u = q.popleft()
        v = q.popleft()
        q.append(merge(u, v))

    if len(q) == 0:
        return q
    else:
        return q[0]

N, M = map(int, raw_input().split())

tenacity = map(int, raw_input().split())
major = map(int, raw_input().split())
s = deque(zip(tenacity, major))

sorts = mergesort(s)

print(counter)
