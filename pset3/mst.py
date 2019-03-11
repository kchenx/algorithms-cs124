# Kruskal's algorithm to find MST
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
            self.name[yname] = xname
        elif self.rank[xname] < self.rank[yname]:
            self.name[xname] = yname
        else:
            self.name[xname] = yname
            if self.rank[xname] == self.rank[yname]:
                self.rank[yname] += 1

    def find(self, x):
        if self.name[x] != x:
            self.name[x] = self.find(self.name[x])
        return self.name[x]



N, M, K = map(int, raw_input().split())
origlen = 0

# set up minimum spanning tree
uf = UnionFind()
# mst = []
edges = []
vertices = set()
newlen = 0

# add current black edges in graph and possible white edges
for i in xrange(M + K):
    edge = map(int, raw_input().split())
    vertices.add(edge[0])
    vertices.add(edge[1])
    edges.append(edge)
    if i < M:
        origlen += edge[2]

# make MST with Kruskal's algorithm
for vertex in vertices:
    uf.makeset(vertex)

# sort edges by weight
edges.sort(key=lambda x: x[2])

for i in xrange(M + K):
    edge = edges[i]
    if uf.find(edge[0]) != uf.find(edge[1]):
        # mst.append(edge)
        uf.union(edge[0], edge[1])
        newlen += edge[2]
        if newlen > origlen:
            break

print origlen - newlen if newlen < origlen else 0
