n = int(input())

dp = [0] * 16
dp[0] = 2
dp[1] = 3
if n == 1:
    print(dp[1] ** 2)
else:
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 1] - 1
    # print(dp)
    print(dp[n] ** 2)