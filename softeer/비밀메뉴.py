import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
sec = ''.join(map(str, input().split()))
but = ''.join(map(str, input().split()))
if sec in but:
    print('secret')
else:
    print('normal')