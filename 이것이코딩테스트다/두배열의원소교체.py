"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]
print(sum(A))