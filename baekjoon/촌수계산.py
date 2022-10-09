n = int(input())
a, b = map(int, input().split())
m = int(input())
board = [[] for _ in range(n + 1)]
for i in range(m):
    p, s = map(int, input().split())
    board[p].append(s)
    board[s].append(p)
visited = [False] * (n + 1)
result = []
status = False

def dfs(start, answer):
    if start == b:
        result.append(answer)
    visited[start] = True
    answer += 1
    for v in board[start]:
        if not visited[v]:
            dfs(v, answer)

dfs(a, 0)
if not result:
    print(-1)
else:
    print(result[0])