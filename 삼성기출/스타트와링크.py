from sys import stdin
from itertools import combinations

input = stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
all_mem = list(range(0, n))
coms = list(combinations(list(range(0, n)), n // 2))
answer = 1e9

for k in range(len(coms)):
    team1, team2 = 0, 0
    team1_com = list(combinations(coms[k], 2))
    for i, j in team1_com:
        team1 += board[i][j] + board[j][i]
    rest = []
    for m in all_mem:
        if m not in coms[k]:
            rest.append(m)
    team2_com = list(combinations(rest, 2))
    for i, j in team2_com:
        team2 += board[i][j] + board[j][i]
    score_diff = abs(team1 - team2)
    if score_diff <= answer:
        answer = score_diff

print(answer)
