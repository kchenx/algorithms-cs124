# Solves CS 124 programming problem in directory

class UnionFind:
    def __init__(self):
        self.name = dict()
        self.rank = dict()

    def makeset(self, x):
        self.name[x] = x
        self.rank[x] = 0

    def union(self, x, y):
        xname = self.find(x)
        yname = self.find(y)

        if xname == yname:
            return

        if self.rank[xname] > self.rank[yname]:
            xname, yname = yname, xname

        if self.rank[xname] == self.rank[yname]:
            self.rank[yname] += 1

        self.name[xname] = yname

    def find(self, x):
        if self.name[x] != x:
            self.name[x] = self.find(self.name[x])
        return self.name[x]


N, M, K = map(int, raw_input().split())

for i in xrange(M):
    p, q = map(int, raw_input().split())

for i in xrange(Q):
    t, a, b = map(int, raw_input().split())


