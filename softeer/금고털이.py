import sys
input = sys.stdin.readline

w, n = map(int, input().split())
lock = []
for _ in range(n):
    m, p = map(int, input().split())
    lock.append([p, m])
lock.sort(key=lambda x: x[0], reverse=True)

answer = 0
temp_weight = 0
for i in range(n):
    temp_weight += lock[i][1]
    answer += lock[i][1] * lock[i][0]
    if temp_weight > w:
        break
answer -= (temp_weight - w) * lock[i][0]
print(answer)