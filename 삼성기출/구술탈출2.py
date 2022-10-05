from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = []
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 현재 R과 B의 위치를 찾고 초기화
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j
q.append((rx, ry, bx, by, 1))
visited.append((rx, ry, bx, by))


def move(x, y, dx, dy):
    count = 0
    while board[x][y] != "O" and board[x + dx][y + dy] != "#":
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfx(q, visited):
    while q:
        # print(q)
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            return -1
        for i in range(len(dx)):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if board[next_bx][next_by] != "O":
                if board[next_rx][next_ry] == "O":
                    return depth
                if next_rx == next_bx and next_ry == next_by:
                    if r_count > b_count:
                        next_rx -= dx[i]
                        next_ry -= dy[i]
                    else:
                        next_bx -= dx[i]
                        next_by -= dy[i]

                if not (next_rx, next_ry, next_bx, next_by) in visited:
                    visited.append((next_rx, next_ry, next_bx, next_by))
                    q.append((next_rx, next_ry, next_bx, next_by, depth + 1))
    return -1

print(bfx(q, visited))