"""
DFS? 깊이 우선 탐색 알고리즘
- 특정한 경로를 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후 다시 돌아가서 다른 경로를 탐색하는 알고리즘
- 일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러개 있으면 낮은 번호부터 처리
"""

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)