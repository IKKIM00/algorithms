"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
n, m = map(int, input().split())

def find_parent(team, x):
    if team[x] != x:
        return find_parent(team, team[x])
    return team[x]

def combine_team(team, a, b):
    a = find_parent(team, a)
    b = find_parent(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        combine_team(parent, a, b)
        result += cost
        last = cost

print(result - last)