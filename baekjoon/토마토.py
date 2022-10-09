import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

que = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                que.append((i, j, k))
while que:
    q, x, y = que.popleft()
    for z in range(6):
        nh = q + dh[z]
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m:
            if arr[nh][nx][ny] == 0:
                que.append((nh, nx, ny))
                arr[nh][nx][ny] = arr[q][x][y] + 1
# print(arr)
result = -2
flag = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                flag = 0
                break
            result = max(result, arr[i][j][k])

if flag == 0:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)