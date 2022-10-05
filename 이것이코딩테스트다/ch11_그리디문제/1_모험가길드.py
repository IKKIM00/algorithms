"""
5
2 3 1 2 2
"""
from collections import Counter
n = int(input())

explore = list(map(int, input().split()))
cnt_explore = Counter(explore)
cnt_explore = {k: v for k, v in sorted(cnt_explore.items())}

answer = 0
rest = 0
for k, v in cnt_explore.items():
    answer += (v + rest) // k
    rest = v % k
print(answer)


# 정답코드
explore.sort()
count = 0
result = 0

for i in explore:
    count += 1
    if count >= i:
        result += 1
        count = 0