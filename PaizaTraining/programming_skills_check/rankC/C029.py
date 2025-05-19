m, n = map(int, input().split())
days = [list(map(int, input().split())) for _ in range(m)]
dp = [int(days[i][1]) for i in range(m-n+1)]

for j in range(1, n):
    dp[0] += days[j][1]

for k in range(1, m-n+1):
    dp[k] = dp[k-1] - days[k-1][1] + days[k+n-1][1]

averages = [l / n for l in dp]
min_average_posi = averages.index(min(averages))

print(days[min_average_posi][0], days[min_average_posi + n - 1][0])