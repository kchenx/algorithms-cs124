# Finds whether there is an even path between nodes with union-find
# Solves CS 124 programming problem in directory

# Disjoint set data structure uses path comrpession and union by rank
# Modified for the problem, bipartitioning graphs
class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        self.connected = dict()     # keep track of connected partitions

    def makeset(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.connected[x] = 0

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        if xp == yp:
            return yp

        if self.rank[xp] > self.rank[yp]:
            xp, yp = yp, xp

        if self.rank[xp] == self.rank[yp]:
            self.rank[yp] += 1

        self.parent[xp] = yp
        return yp

    def find(self, x):
        if x not in self.parent:
            return False
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def addedge(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        if xp > yp:
            xp, yp = yp, xp

        if not self.connected[xp] and not self.connected[yp]:
            self.connected[xp] = yp
            self.connected[yp] = xp

        elif self.connected[xp] == -1 or self.connected[yp] == -1:
            newp = self.union(xp, yp)
            if self.connected[xp] > 0:
                newp = self.union(newp, self.connected[xp])
                self.connected.pop(self.connected[xp])
            if self.connected[yp] > 0:
                newp = self.union(newp, self.connected[yp])
                self.connected.pop(self.connected[yp])
            if xp in self.connected:
                self.connected.pop(xp)
            if yp in self.connected:
                self.connected.pop(yp)
            self.connected[newp] = -1

        elif self.connected[xp] and self.connected[yp]:
            if self.connected[xp] == yp:
                return
            elif xp == yp:
                newp = self.union(xp, self.connected[xp])
                newp = self.union(newp, self.connected[yp])
                self.connected.pop(self.connected[xp])
                self.connected.pop(xp)
                self.connected[newp] = -1
            else:
                xnew = self.union(xp, self.connected[yp])
                ynew = self.union(self.connected[xp], yp)
                self.connected.pop(self.connected[xp])
                self.connected.pop(self.connected[yp])
                self.connected.pop(xp)
                self.connected.pop(yp)
                self.connected[xnew] = ynew
                self.connected[ynew] = xnew

        elif self.connected[xp]:
            newp = self.union(self.connected[xp], yp)
            self.connected.pop(self.connected[xp])
            self.connected[xp] = newp
            self.connected[newp] = xp

        elif self.connected[yp]:
            newp = self.union(self.connected[yp], xp)
            self.connected.pop(self.connected[yp])
            self.connected[yp] = newp
            self.connected[newp] = yp


    def oddpath(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        if not xp or not yp:
            return 0

        if self.connected[xp] == yp or (xp == yp and self.connected[xp] == -1):
            return 1
        else:
            return 0



# get user input
N, M, K = map(int, raw_input().split())

nodes = set()
enemies = set()
res = 0

for i in xrange(M):
    p, q = map(int, raw_input().split())
    nodes.add(p)
    nodes.add(q)
    if p > q:
        p, q = q, p
    enemies.add((p, q))

# attempt to split graphs into bipartitions
uf = UnionFind()

for node in nodes:
    uf.makeset(node)

for enemy in enemies:
    uf.addedge(enemy[0], enemy[1])

for i in xrange(K):
    t, a, b = map(int, raw_input().split())
    if a > b:
        a, b = b, a
    if t == 1:
        if a not in nodes:
            nodes.add(a)
            uf.makeset(a)
        if b not in nodes:
            nodes.add(b)
            uf.makeset(b)
        uf.addedge(a, b)
    elif t == 2:
        res += uf.oddpath(a, b)

print res
