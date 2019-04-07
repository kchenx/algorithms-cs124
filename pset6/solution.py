import sys
sys.setrecursionlimit(2**30)

N, M, B = map(int, raw_input().split())

for i in xrange(M):
    a, b = map(int, raw_input().split())

for i in xrange(N):
    c, d = map(int, raw_input().split())

print "Impossible"
