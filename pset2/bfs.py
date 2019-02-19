from collections import defaultdict

def bfs_iteration(graph, depth, visited, node):
    """
    Performs one level of depth of BFS and returns the nodes in the next level
    of BFS
    """
    nextlevel = set()
    done = 0
    q = depth
    if not q:
        q = [node]
    while q:
        vertex = q.pop(0)
        if vertex not in visited:
            if visited[vertex] > 0:
                done = visited[vertex]
                break
            else:
                visited[vertex] = node
            nextlevel |= graph[vertex]
    return done, nextlevel, visited


# get input from user
N, M, K = map(int, raw_input().split())

city = defaultdict(set)

visited = {}
visited = defaultdict(lambda:0,visited)

# convert input into graph
for i in xrange(M):
    a, b = map(int, raw_input().split())
    city[a].add(b)
    city[b].add(a)

vacant = map(int, raw_input().split())

# conduct BFS on each vacancy, one level of depth at a time
while True:
    flag = 0
    depths = defaultdict(set)
    for node in vacant:
        done, nextlevel, visited = bfs_iteration(city, depths[node], visited, node)
        depths[node] = nextlevel
        print (done, nextlevel, visited)
        if done > 0:
            if node > done:
                node, done = done, node
            results.append((node, done))
            flag = 1

    if flag > 0:
        sort = sorted(data, key=lambda tup: (tup[1],tup[2]))
        print(sort[0][0] + ' ' + sort[0][1])
        break

