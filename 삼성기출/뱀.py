from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = "A"
l = int(input())
snake_chg_point = {}
for _ in range(l):
    k, v = map(str, input().split())
    snake_chg_point[int(k)] = v

cur_direct = "W"
head = (0, 0)
snake = deque()
snake.append((0, 0))
time = 0

# 방향: [왼쪽, 오른쪽]
chg_direct = {"W": ["N", "S"],
              "E": ["S", "N"],
              "S": ["W", "E"],
              "N": ["E", "W"]}

def next_move(loc, direct):
    if direct == "W":
        return (loc[0], loc[1] + 1)
    elif direct == "E":
        return (loc[0], loc[1] - 1)
    elif direct == "N":
        return (loc[0] - 1, loc[1])
    else:
        return (loc[0] + 1, loc[1])

while True:
    time += 1
    next_head = next_move(head, cur_direct)
    if next_head[0] >= n or next_head[1] >= n or next_head[0] < 0 or next_head[1] < 0:
        break

    if board[next_head[0]][next_head[1]] == "A":
        board[next_head[0]][next_head[1]] = 1
        snake.append(next_head)
        head = next_head
        if time in snake_chg_point:
            turn = snake_chg_point[time]
            if turn == "L":
                cur_direct = chg_direct[cur_direct][0]
            else:
                cur_direct = chg_direct[cur_direct][1]
    elif board[next_head[0]][next_head[1]] == 0:
        board[next_head[0]][next_head[1]] = 1
        snake.append(next_head)
        past_x, past_y = snake.popleft()
        board[past_x][past_y] = 0
        head = next_head
        if time in snake_chg_point:
            turn = snake_chg_point[time]
            if turn == "L":
                cur_direct = chg_direct[cur_direct][0]
            else:
                cur_direct = chg_direct[cur_direct][1]
    else:
        break
print(time)