from sys import stdin
import copy

input = stdin.readline

n, m = map(int, input().split())
board = []
virus_loc = []
answer = 0

for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_loc.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, temp_board):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp_board[nx][ny] == 0:
                temp_board[nx][ny] = 2
                dfs(nx, ny, temp_board)


def get_score(area):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                cnt += 1
    return cnt


def makeWall(start, cnt):
    global answer
    if cnt == 3:
        temp_board = copy.deepcopy(board)
        for k in range(len(virus_loc)):
            x, y = virus_loc[k]
            dfs(x, y, temp_board)
        answer = max(answer, get_score(temp_board))
        return

    for k in range(start, n * m):
        i = int(k / m)
        j = int(k % m)

        if board[i][j] == 0:
            board[i][j] = 1
            makeWall(k + 1, cnt + 1)
            board[i][j] = 0

makeWall(0, 0)
print(answer)
