N, X = [int(x) for x in input().split()]
w = [int(input()) for _ in range(N)]
ans = 0
for i in range(2 ** N):
    sum = 0
    for j in range(N):
        if (i >> j) & 1:
            sum += w[j]
    if (sum <= X) and (ans < sum):
        ans = sum
print(ans)