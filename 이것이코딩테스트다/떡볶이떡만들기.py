"""
4 6
19 15 10 17
"""
N, M = map(int, input().split())
ddok_length = list(map(int, input().split()))

start, end = 0, max(ddok_length)
answer = 0
while start < end:
    mid = (start + end) // 2
    cut_length = 0
    for ddok in ddok_length:
        if ddok > mid: cut_length += ddok - mid
    if cut_length < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)



