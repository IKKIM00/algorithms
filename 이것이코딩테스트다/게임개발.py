"""
입력값 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

# N, M을 공백을 기준으로 입력 받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해서 맵을 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 위치 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 입력받은 현재 좌표를 방문한 처리

# 전체 맵에 대한 정보 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1: direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전했는데 정면에 가보지 않은 칸이 있을 경우에는 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:   # 회전했는데 정면에 모두 가본 땅이거나 바다인 경우
        turn_time += 1
    # 네방향 모두 갈 수 없을 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:  # 만약 뒤가 땅이면 이동
            x = nx
            y = ny
        else:   # 뒤가 바다로 받혀있는 경우
            break
        turn_time = 0

print(count)