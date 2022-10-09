from collections import deque

f, s, g, u, d = map(int, input().split())

result = [0] * (f + 1)
visited = [False] * (f + 1)
def bfs():
    que = deque([s])
    visited[s] = True
    while que:
        cur = que.popleft()
        if cur == g:
            print(result[cur])
            return
        for i in [cur + u, cur - d]:
            if 0 < i <= f and visited[i] is False:
                visited[i] = True
                result[i] = result[cur] + 1
                que.append(i)
    if result[g] == 0:
        print('use the stairs')
        return
bfs()
