# Solves CS 124 programming problem in directory

from collections import defaultdict

class Graph:
    """ Digraph class for weighted graph """

    def __init__(self, nverts):
        self.nverts = nverts
        self.graph = [[0 for j in xrange(nverts)] for i in xrange(nverts)]

    def addedge(self, u, v, weight):
        """ Add weighted edge to graph """
        self.graph[u][v] = weight

    def bfs(self, s, t, parents):
        """ Returns True iff path from `s` to `t` using BFS """

        visited = [False] * self.nverts
        q = []

        q.append(s)
        visited[s] = True

        while q:
            u = q.pop(0)

            for i, val in enumerate(self.graph[u]):
                if visited[i] == False and val > 0:
                    q.append(i)
                    visited[i] = True
                    parents[i] = u

        return True if visited[t] else False

    def fordfulkerson(self, source, sink): 

        parents = [-1] * self.nverts        # Stores path
        maxflow = 0

        # Augment flow 
        while self.bfs(source, sink, parents):

            # Find min residual capacity
            flow = float("inf")
            s = sink
            while s != source:
                flow = min(flow, self.graph[parents[s]][s])
                s = parents[s]

            # Add flow vector
            maxflow += flow

            # Update residual capacities
            v = sink
            while v != source:
                u = parents[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = parents[v]

        return maxflow


# Get user input

N, M = map(int, raw_input().split())

g = Graph(2 * N + 1)

for i in xrange(M):
    a, b, c, d = map(int, raw_input().split())
    a -= 1
    b -= 1
    g.addedge(a * 2 + 1, b * 2, c * d)

lockdowns = map(int, raw_input().split())

for i, e in enumerate(lockdowns):
    g.addedge(i * 2, i * 2 + 1, e)

for i in xrange(1, 4):
    g.addedge(i * 2 + 1, 2 * N, float("inf"))

print g.fordfulkerson(0, 2 * N)

