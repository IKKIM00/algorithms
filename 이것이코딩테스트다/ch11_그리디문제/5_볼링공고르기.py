"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""

n, m = map(int, input().split())
weights = list(map(int, input().split()))

answer = 0
for i in range(len(weights)):
    for j in range(i, len(weights)):
        if weights[i] != weights[j]:
            answer += 1
print(answer)