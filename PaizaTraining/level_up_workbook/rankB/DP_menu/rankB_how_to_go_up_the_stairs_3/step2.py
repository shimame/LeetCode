n, a, b = [int(x) for x in input().split()]
dp = [0] * (n+1)
dp[0] = 1
if a > b:
    a, b = b, a
if a == 1:
    dp[1] = 1
for i in range(a, n+1):
    dp[i] = dp[i - a] + dp[i - b]
print(dp[n])