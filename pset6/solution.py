# Solves CS 124 programming problem in directory

import sys
sys.setrecursionlimit(2**30)

from collections import defaultdict

class Graph:
    """ Digraph class,`components()` modified to solve particular problem """

    def __init__(self, nvertices):
        self._nverts = nvertices
        self._out = defaultdict(set)    # edges from node
        self._in = defaultdict(set)     # edges to node

    def addEdge(self, u, v):
        """ Add edge to graph """
        self._out[u].add(v)
        self._in[v].add(u)

    def components(self):
        """
        Returns flattened list of strongly connected components by Kosaraju's algorithm.
        `nodes` array is nodes, and `islast` is true iff node `i` is last in its SCC.
        Returns false if there is more than a single source SCC,
        or if an SCC has fewer than two nodes, meaning it is impossible
        for the situation to meet the problem spec.
        """

        visited = [False] * (self._nverts + 1)
        L = []

        def visit(u):
            if not visited[u]:
                visited[u] = True
                for v in self._out[u]:
                    visit(v)
                L.insert(0, u)

        for u in self._out.keys():
            visit(u)

        component = defaultdict(set)
        assigned = [False] * (self._nverts + 1)

        def assign(u, root):
            if not assigned[u]:
                component[root].add(u)
                assigned[u] = True
                for v in self._in[u]:
                    assign(v, root)

        # Assign nodes to SCCs
        for u in L:
            assign(u, u)

        # Check if single source SCC and each SCC has at least 2 nodes
        nsources = 0
        for scc in component.values():
            # Ensure at least 2 nodes
            if len(scc) < 2:
                return False

            # SCC is a source iff sources of all nodes are in SCC
            issource = True
            for node in scc:
                if any([source not in scc for source in self._in[node]]):
                    issource = False
                    break
            if issource:
                nsources += 1
            if nsources > 1:
                return False

        return list(component.values())


N, M, B = map(int, raw_input().split())

g = Graph(N)
allones = True      # if cost and quality all one
costs = [0] * (N + 1)
qualities = [0] * (N + 1)

# Get user input
for i in xrange(M):
    u, v = map(int, raw_input().split())

    g.addEdge(u, v)

for i in xrange(1, N + 1):
    c, q = map(int, raw_input().split())
    costs[i] = c
    qualities[i] = q
    if c != 1 or q != 1:
        allones = False

if allones:
    sccs = g.components()

    if sccs:
        print 2 * len(sccs)
    else:
        print "Impossible"

else:
    sccs = g.components()
    
    if not sccs:
        print "Impossible"
        exit(0)

    nodes = []              # Flattened list of nodes, grouped by SCCs
    islast = [False] * N    # True iff node `i` is last in its SCC group
    i = -1
    for scc in sccs:
        for node in scc:
            i += 1
            nodes.append(node) 
        islast[i] = True

    dp = [[[float("-inf") for k in xrange(4)] for j in xrange(B + 1)] for i in xrange(N + 2)]

    def f(n, b, s):
        if dp[n][b][s] != float("-inf"):
            return dp[n][b][s]

        if n < 0 and b >= 0:
            dp[n][b][s] = 0
        elif b < 0 or s == 3:
            dp[n][b][s] = float("-inf")
        elif islast[n - 1] and s == 0:
            dp[n][b][s] = float("-inf")
        elif islast[n - 1] and s == 1:
            dp[n][b][s] = f(n - 1, b - costs[nodes[n]], 2) + qualities[nodes[n]]
        elif islast[n - 2] and s == 0:
            dp[n][b][s] = f(n - 1, b - costs[nodes[n]], 1) + qualities[nodes[n]]
        elif islast[n] and n >= 0:
            dp[n][b][s] = max(f(n - 1, b - costs[nodes[n]], 1) + qualities[nodes[n]], f(n - 1, b, 0))
        else:
            dp[n][b][s] = max(f(n - 1, b - costs[nodes[n]], s + 1) + qualities[nodes[n]], f(n - 1, b, s))

        return dp[n][b][s]

    maxq = f(N-1, B, 0)
    print maxq if maxq >= 0 else "Impossible"

