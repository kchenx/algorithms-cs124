# Solves CS 124 programming problem in directory

import sys
sys.setrecursionlimit(2**30)

from collections import defaultdict

class Graph:
    """ Digraph class, `components()` modified to solve particular problem """

    def __init__(self, nvertices):
        self._nverts = nvertices
        self._out = defaultdict(set)    # edges from node
        self._in = defaultdict(set)     # edges to node
        self._counter = 0

    def addEdge(self, u, v):
        """ Add edge to graph """
        self._out[u].add(v)
        self._in[v].add(u)

    def components(self):
        """
        Returns array of strongly-connected components by Kosaraju's algorithm.
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

        # Assign to SCC
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


    def components2(self): 
        """ Wrapper function for Tarjan's algorithm """

        disc = [-1] * (self._nverts + 1)
        low = [-1] * (self._nverts + 1)
        onstack = [False] * (self._nverts + 1)
        stack = []
        sccs = []

        def scchelper(u):
            disc[u] = low[u] = self._counter
            self._counter += 1
            onstack[u] = True
            stack.append(u)

            for v in self._out[u]:
                if disc[v] == -1:
                    scchelper(v)
                    low[u] = min(low[u], low[v])
                elif onstack[v]:
                    low[u] = min(low[u], disc[v])

            w = -1
            temp = []
            if low[u] == disc[u]:
                while w != u:
                    w = stack.pop()
                    temp.append(w)
                    onstack[w] = False

                if temp != [0]:
                    sccs.append(temp)
                temp = []

        for i in xrange(self._nverts):
            if disc[i] == -1:
                scchelper(i)

        # Check if single source SCC and each SCC has at least 2 nodes
        nsources = 0
        for scc in sccs:
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

        return sccs




N, M, B = map(int, raw_input().split())

g = Graph(N)
allones = True      # if cost and quality all one
costs = [-1] * (N + 1)
qualities = [-1] * (N + 1)

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
    sccs = g.components2()

    if sccs:
        print 2 * len(sccs)
    else:
        print "Impossible"

else:
    sccs = g.components2()

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

    dp = [[[float("-inf") for k in xrange(4)] for j in xrange(B + 1)] for i in xrange(2)]

    def f(n, b, s):
        for i in xrange(n):
            for j in xrange(b + 1):
                for k in [2, 1, 0]:
                    # Base case: first node
                    if i == 0:
                        if k == 2:
                            dp[1][j][k] = 0
                        elif k == 1:
                            if j < costs[nodes[i]]:
                                dp[1][j][k] = float("-inf")
                            else:
                                dp[1][j][k] = qualities[nodes[i]]
                        elif k == 0:
                            dp[1][j][k] = float("-inf")

                    elif k == 1 and islast[i - 1]:
                        if j < costs[nodes[i]]:
                            dp[1][j][k] = float("-inf")
                        else:
                            dp[1][j][k] = dp[0][j - costs[nodes[i]]][2] + qualities[nodes[i]]

                    elif k == 0 and islast[i - 1]:
                        dp[1][j][k] = float("-inf")

                    elif k == 0 and (i == 1 or islast[i - 2]):
                        if j < costs[nodes[i]]:
                            dp[1][j][k] = float("-inf")
                        else:
                            dp[1][j][k] = dp[0][j - costs[nodes[i]]][1] + qualities[nodes[i]]

                    # Reset server count for new SCC
                    elif islast[i]:
                        if j < costs[nodes[i]]:
                            dp[1][j][k] = dp[0][j][0]
                        else:
                            dp[1][j][k] = max(dp[0][j - costs[nodes[i]]][1] + qualities[nodes[i]], dp[0][j][0])

                    elif k == 2 or j < costs[nodes[i]]:
                        dp[1][j][k] = dp[0][j][k]

                    else:
                        dp[1][j][k] = max(dp[0][j - costs[nodes[i]]][k + 1] + qualities[nodes[i]], dp[0][j][k])

                # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dp]))


            # Move entries
            for j in xrange(b + 1):
                for k in xrange(3):
                    dp[0][j][k] = dp[1][j][k]

        return dp[1][b][s]

    maxq = f(N, B, 0)

    print maxq if maxq >= 0 else "Impossible"
    