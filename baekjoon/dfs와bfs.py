from collections import  deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)

bfs_visited = [False] * (n + 1)

def dfs(visited, i, graph):
    visited[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if not visited[j]:
            dfs(visited, j, graph)

def bfs(visited, i, graph):
    que = deque([i])
    visited[i] = True
    while que:
        cur = que.popleft()
        print(cur, end=' ')
        for j in graph[cur]:
            if not visited[j]:
                que.append(j)
                visited[j] = True

dfs(dfs_visited, v, graph)
print()
bfs(bfs_visited, v, graph)