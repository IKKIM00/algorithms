import sys

input = sys.stdin.readline

n, m = map(int, input().split())
meeting_rooms = {}
for _ in range(n):
    meeting_rooms[str(input()).rstrip()] = []
meeting_rooms = {k: v for k, v in sorted(meeting_rooms.items())}
for _ in range(m):
    r, s, t = map(str, input().split())
    meeting_rooms[r].append((int(s), int(t)))

available = {}
for r, times in meeting_rooms.items():
    available[r] = []
    meeting_rooms[r].sort(key=lambda x: x[0])
    start = 9
    for t in times:
        if t[0] > start:
            available[r].append(f'{start:02}-{t[0]:02}')
            start = t[1]
        elif t[0] == start:
            start = t[1]
    if start < 18:
        available[r].append(f'{start:02}-18')

for idx, (car, times) in enumerate(available.items()):
    print(f'Room {car}:')
    if not times:
        print("Not available")
    else:
        print(f"{len(times)} available:")
        for t in times:
            print(t)
    if idx < n - 1:
        print('-' * 5)

