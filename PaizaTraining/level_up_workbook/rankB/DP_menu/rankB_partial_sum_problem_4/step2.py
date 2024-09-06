n, x = [int(x) for x in input().split()]
a = [int(input()) for _ in range(n)]
dp = [0] * (x+1)
dp[0] = 1
for i in a:
    for j in range(x, i-1, -1):
        dp[j] += dp[j - i]

print(dp[x] % 1000000007)