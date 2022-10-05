from sys import stdin

input = stdin.readline

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
commend = list(map(int, input().split()))
# print(commend)

dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


for i in commend:
    x += dx[i - 1]
    y += dy[i - 1]
    if x >= n or x < 0 or y < 0 or y >= m:
        x -= dx[i - 1]
        y -= dy[i - 1]
        continue
    # print(f"x: {x}, y: {y}")
    turn(i)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])