from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
slope = [1] + [0] * l
roads = []
board = []
for _ in range(n):
    inp = list(map(int, input().split()))
    board.append(inp)
    roads.append(inp)
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    roads.append(temp)

answer = 0
for r in roads:
    flag = 0
    check = [False] * n
    for i in range(n - 1):
        if r[i] == r[i + 1]:
            continue
        if abs(r[i] - r[i + 1]) > 1:
            flag = 1
        if r[i] > r[i + 1]:
            temp = r[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if r[j] != temp:
                        flag = 1
                    if check[j]:
                        flag = 1
                    check[j] = True
                else:
                    flag = 1
        else:
            temp = r[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if r[j] != temp:
                        flag = 1
                    if check[j]:
                        flag = 1
                    check[j] = True
                else:
                    flag = 1
    if flag == 0:
        answer += 1
print(answer)