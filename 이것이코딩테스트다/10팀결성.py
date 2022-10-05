"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
n, m = map(int, input().split())

team = [i for i in range(n + 1)]

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

for _ in range(m):
    status, a, b = map(int, input().split())
    if status == 0:
        combine_team(team, a, b)

    if status == 1:
        a_parent = find_parent(team, a)
        b_parent = find_parent(team, b)
        if a_parent == b_parent:
            print("YES")
        else:
            print("NO")
