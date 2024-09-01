n, a, b = [int(x) for x in input().split()]
dp = [0] * (n+1)
dp[0], dp[1] = 0, a
for i in range(2, n+1):
    dp[i] = min(dp[i-1] + a, dp[i-2] + b)
print(dp[n])