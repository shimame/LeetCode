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
    y1, x1, y2, x2 = [int(x) - 1 for x in input().split()]
    if y1 == x1 == 0:
        answer = sums[y2][x2]
    elif y1 == 0:
        answer = sums[y2][x2] - sums[y2][x1 - 1]
    elif x1 == 0:
        answer = sums[y2][x2] - sums[y1 - 1][x2]
    else:
        answer = sums[y2][x2] - sums[y2][x1 - 1] - sums[y1 - 1][x2] + sums[y1 - 1][x1 - 1]
    ans.append(answer)

for i in ans:
    print(i)