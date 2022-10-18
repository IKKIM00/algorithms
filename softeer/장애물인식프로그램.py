import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(str(input().rstrip())))
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == "1" and not visited[x][y]:
            temp = 1
            que = deque([[x, y]])
            while que:
                cur_x, cur_y = que.popleft()
                visited[cur_x][cur_y] = True
                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and graph[nx][ny] == "1":
                            visited[nx][ny] = True
                            temp += 1
                            que.append([nx, ny])
            answer.append(temp)
print(len(answer))
answer.sort()
for a in answer:
    print(a)
