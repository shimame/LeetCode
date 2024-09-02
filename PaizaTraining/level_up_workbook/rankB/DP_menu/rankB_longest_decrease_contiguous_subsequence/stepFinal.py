n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[n] = 1
for i in range(n-1, 0, -1):
    if a[i] >= a[i+1]:
        dp[i] = dp[i+1] + 1
    else:
        dp[i] = 1
print(max(dp))