# 못풀었음
"""
5
3 2 1 1 9
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)