from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, idx, score):
    global answer
    if answer >= score + max_val * (3 - idx):
        return
    if idx == 3:
        answer = max(answer, score)
        return
    else:
        for k in range(4):
            ni = x + dx[k]
            nj = y + dy[k]
            # print(ni, nj)
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                if idx == 1:
                    visited[ni][nj] = 1
                    dfs(x, y, idx + 1, score + board[ni][nj])
                    visited[ni][nj] = 0
                visited[ni][nj] = 1
                dfs(ni, nj, idx + 1, score + board[ni][nj])
                visited[ni][nj] = 0


answer = 0
max_val = max(map(max, board))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0
print(answer)
