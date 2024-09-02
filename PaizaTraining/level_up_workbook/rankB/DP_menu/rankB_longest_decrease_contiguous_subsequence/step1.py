n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    if a[i-1] <= a[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1
print(max(dp))