
k, p, n = map(int, input().split())
for _ in range(n):
    k = (k * p) % 1000000007
print(k)