n, x = [int(x) for x in input().split()]
a = [int(input()) for _ in range(n)]
dp = [False] * (x+1)
dp[0] = True
for i in a:
    for j in range(x, i-1, -1):
        if dp[j - i]:
            dp[j] = True
if dp[x]:
    print("yes")
else:
    print("no")