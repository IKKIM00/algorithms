from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
visited[r][c] = True
cnt = 0
answer = 1
"""
    0
3       1
    2
"""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

status = True
while status:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            if visited[nx][ny] is False:
                visited[nx][ny] = True
                answer += 1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:
        if board[r - dx[d]][c - dy[d]] == 1:
            print(answer)
            break
        else:
            r, c = r - dx[d], c - dy[d]