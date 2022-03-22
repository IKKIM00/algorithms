"""
BFS - 너비 우선 탐색 = 가까운 노드부터 탐색하는 알고리즘
선입선출 방식인 큐 자료구조를 이용하는 것이 정석
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    while queue:    # 큐가 빌 때 까지 반복
        # 큐에서 원소를 하나씩 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:  #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, 1, visited)