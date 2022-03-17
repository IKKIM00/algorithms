n = int(input())
routes = map(str, input().split())

start = [1, 1]
direction = ["R", "L", "U", "D"]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for route in routes:
    idx = direction.index(route)
    if (start[1] + dx[idx] > n) or (start[0] + dy[idx] > n) or (start[1] + dx[idx] == 0) or (start[0] + dy[idx] == 0):
        continue
    else:
        start[1] += dx[idx]
        start[0] += dy[idx]

print(start)

