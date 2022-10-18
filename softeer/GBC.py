import sys
input = sys.stdin.readline

n, k = map(int, input().split())

rule = []
cur_meter = 0
for _ in range(n):
    a, b = map(int, input().split())
    cur_meter += a
    rule.append([cur_meter, b])

estimated = []
cur_meter = 0
for _ in range(k):
    a, b = map(int, input().split())
    cur_meter += a
    estimated.append([cur_meter, b])

mx = 0
for m, s in estimated:
    while rule and rule[0][0] < m:  # 현재 미터 보다 작을 경우
        if s > rule[0][1]:
            mx = max(mx, s - rule[0][1])
        rule.pop(0)
    if rule and m <= rule[0][0]:    # 현재 미터가 다음 미터보다는 큰 경우
        if s > rule[0][1]:
            mx = max(mx, s - rule[0][1])
    if rule and rule[0][0] == m:    # 같은 경우
        rule.pop(0)
print(mx)