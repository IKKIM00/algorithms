import sys
input = sys.stdin.readline

n = int(input())
wh = []
for _ in range(n):
    weight, height = map(int, input().split())
    wh.append([weight, height])

for i in range(n):
    rank = 1
    cur_w, cur_h = wh[i][0], wh[i][1]
    for j in range(n):
        if cur_w < wh[j][0] and cur_h < wh[j][1]:
            rank += 1
    print(rank)

