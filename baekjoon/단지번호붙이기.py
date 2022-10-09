from collections import deque

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer_list = []
for i in range(n):
    for j in range(n):
        answer = 0
        if board[i][j] == 1:
            board[i][j] = 0
            answer += 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 1:
                            board[nx][ny] = 0
                            answer += 1
                            que.append((nx, ny))
            answer_list.append(answer)
print(len(answer_list))
answer_list.sort()
for a in answer_list:
    print(a)
