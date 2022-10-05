from sys import stdin
from collections import deque

input = stdin.readline
gears = []
for _ in range(4):
    gears.append(list(map(int, input().strip())))

k = int(input())
directions = []
for _ in range(k):
    directions.append(list(map(int, input().split())))


def move_gear(gear, direct):
    if direct == 1:
        return gear[1:] + [gear[0]]
    else:
        return [gear[-1]] + gear[:-1]

def check_right(g_idx, d):
    global gears
    if g_idx > 3 or gears[g_idx][2] == gears[g_idx + 1][6]:
        return
    if gears[g_idx][2] != gears[g_idx + 1][6]:
        check_right(g_idx + 1, d * -1)
        gears[g_idx] = move_gear(gears[g_idx], d)

def check_left(g_idx, d):
    global gears
    if g_idx < 0 or gears[g_idx][6] == gears[g_idx - 1][2]:
        return
    if gears[g_idx][6] != gears[g_idx - 1][2]:
        check_left(g_idx - 1, d * -1)
        gears[g_idx] = move_gear(gears[g_idx], d * -1)

check_list = deque()
for idx, d in directions:
    # check_list.append([idx - 1, d])
    print(idx - 1)
    check_right(idx - 1, d)
    check_left(idx - 1, d)
    gears[idx - 1] = move_gear(gears[idx - 1], d)
answer = 0
for i in range(len(gears)):
    answer += gears[i][0]
print(answer)