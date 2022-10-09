from collections import deque
n, k = map(int, input().split())

max_val = 100000
result = [0] * (max_val + 1)

def bfs():
    que = deque([n])
    while que:
        cur = que.popleft()
        if cur == k:
            print(result[k])
            return
        for j in [cur - 1, cur + 1, cur * 2]:
            if 0 <= j <= max_val and result[j] == 0:
                result[j] = result[cur] + 1
                que.append(j)
bfs()