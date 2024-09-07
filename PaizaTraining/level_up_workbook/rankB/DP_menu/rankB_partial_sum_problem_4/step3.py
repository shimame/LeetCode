n, x = [int(x) for x in input().split()]
a = [int(input()) for _ in range(n)]
steps = [n+1] * (x+1)
steps[0] = 0
for i in a:
    for j in range(x, i-1, -1):
        if steps[j-i] != n + 1:
            steps[j] = min(steps[j],steps[j-i] + 1)
if steps[x] == n + 1:
    print(-1)
else:
    print(steps[x])