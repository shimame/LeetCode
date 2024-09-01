n, a, b = [int(x) for x in input().split()]
dp = [0] * (n+5)
dp[2], dp[4], dp[5] = a, 2*a, b
for i in range(6, n+5):
    if dp[i-2] == 0 and dp[i-5] == 0:
        pass
    elif dp[i-2] == 0:
        dp[i] = dp[i-5] + b
    elif dp[i-5] == 0:
        dp[i] = dp[i-2] + a
    else:
        dp[i] = min(dp[i-2] + a, dp[i-5] + b)
min = max(dp)
for j in range(n+4, 0, -1):
    if dp[j] == 0 or dp[j] > min:
        dp[j] = min
    if min > dp[j]:
        min = dp[j]
print(dp[n])

"""answer
n, a, b = map(int, input().split())
dp = [10000000] * (n + 5)
dp[0] = 0
for i in range(2, n + 5):
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + a)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + b)
print(min(dp[n:]))
"""