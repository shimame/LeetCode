H, W, N = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]
sums = [[0] * W for _ in range(H)]
ans = []
for h in range(H):
    for w in range(W):
        if h == 0:
            sums[h][w] = sum(A[h][:w+1])
        else:
            sums[h][w] = sums[h-1][w] + sum(A[h][:w+1])

for _ in range(N):
    y, x = map(int, input().split())
    ans.append(sums[y-1][x-1])

for i in ans:
    print(i)


"""answer
H, W, N = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]

ans = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(1, H + 1):
    ans[i] = [0] + A[i - 1][:]
    for j in range(1, W + 1):
        ans[i][j] += ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1]

for _ in range(N):
    y, x = map(int, input().split())
    print(ans[y][x])
"""