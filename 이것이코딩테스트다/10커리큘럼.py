"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from collections import deque
import copy
n = int(input())

indegree = [0] * (n + 1)
times = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()