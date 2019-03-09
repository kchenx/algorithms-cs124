# Modified BFS to find shortest path between special vertices
# Solves CS 124 programming problem in directory

from collections import defaultdict, deque

# get input from user
N, M, K = map(int, raw_input().split())

city = [set() for i in xrange(N + 1)]

# convert input into graph
for i in xrange(M):
    a, b = map(int, raw_input().split())
    city[a].add(b)
    city[b].add(a)

for i in xrange(1, N + 1):
    city[i] = sorted(city[i])

# create list of vacant nodes
vacant = map(int, raw_input().split())
vacant.sort()

# preparing for BFS
mindist = -1

visited = [0] * (N + 1)
origin = [0] * (N + 1)
distance = [0] * (N + 1)

# make deques for each vacancy to start BFS
q = []
for v in vacant:
    q.append(deque([v]))
    visited[v] = 1
    origin[v] = v

# conduct BFS on each vacancy, one level of depth at a time
while True:
    flag = 0
    for i in xrange(K):
        if not q[i]:
            continue

        node = q[i].popleft()
        flag = 1

        for adj in city[node]:
            if not visited[adj]:
                # check each new adjacent node
                visited[adj] = 1
                q[i].append(adj)
                origin[adj] = origin[node]
                distance[adj] = distance[node] + 1
            else:
                if origin[adj] == origin[node]:
                    continue
                # calculate total distance between nodes
                dist = distance[adj] + distance[node] + 1
                # tie breaking
                if mindist == -1 or dist < mindist:
                    mindist = dist
                    result = sorted([origin[node], origin[adj]])
                elif dist == mindist:
                    temp = sorted([result, [origin[node], origin[adj]]])
                    result = temp[0]

    if not flag:
        print result[0], result[1]
        break
