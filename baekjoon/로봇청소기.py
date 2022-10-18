from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def rotate(cur_dir):
    next_dir = cur_dir - 1
    if next_dir == -1:
        next_dir = 3
    return next_dir

que = deque([[r, c, d]])
while que:
    x, y, cur_dir = que.popleft()
    maps[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0:
                que.append([nx, ny, cur_dir])
                maps[nx][ny] = 2
