import sys
input = sys.stdin.readline

n = int(input())
time_sch = []
for _ in range(n):
    s, e = map(int, input().split())
    time_sch.append([s, e])
time_sch.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = time_sch[0][1]
for i in range(1, n):
    if time_sch[i][0] >= end:
        answer += 1
        end = time_sch[i][1]
print(answer)
