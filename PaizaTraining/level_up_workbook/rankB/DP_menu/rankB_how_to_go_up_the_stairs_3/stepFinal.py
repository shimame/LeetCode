l = input().split()
n = int(l.pop(0))
l.sort()
dp = [0] * (n+1)
dp[0] = 1
a, b, c = map(int, l)

if a == 1:
    dp[1] = 1
for i in range(a, n+1):
    dp[i] = dp[i - a] + dp[i - b] + dp[i - c]
print(dp[n])