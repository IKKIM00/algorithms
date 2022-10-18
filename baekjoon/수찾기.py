import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

def binary(answer):
    start = 0
    end = len(n_list) - 1
    mid = (start + end) // 2
    while start <= end:
        # print(start, end, mid)
        if answer == n_list[mid]:
            return 1
        elif answer < n_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return 0

for i in m_list:
    print(binary(i))
