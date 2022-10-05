from sys import stdin

input = stdin.readline

n = int(input())
test_area = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = len(test_area)

for i in range(len(test_area)):
    num = test_area[i]
    if num > 0:
        num -= b
    if num > 0:
        if num % c == 0:
            cnt += (num // c)
        else:
            cnt += (num // c) + 1
print(cnt)
