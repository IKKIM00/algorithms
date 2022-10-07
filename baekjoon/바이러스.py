n = int(input())
m = int(input())
network = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

answer = 0
visited = [False] * (n + 1)
def dfs(visited, i, network):
    visited[i] = True
    global answer
    answer += 1
    for j in network[i]:
        if not visited[j]:
            dfs(visited, j, network)
dfs(visited, 1, network)
print(answer - 1)
