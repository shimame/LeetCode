def calc_interval_sum(X, l, u, r, d):
    rst = X[r][d]
    if 0 < l and 0 < u:
        rst += X[l - 1][u - 1]
    if 0 < l:
        rst -= X[l - 1][d]
    if 0 < u:
        rst -= X[r][u - 1]
    return rst

H, W, N = map(int, input().split())
C = [[int(x) for x in input().split()] for _ in range(H)]
counts = [[0] * (W + 1) for _ in range(H + 1)]
ans = []
for i in range(1, H + 1):
    counts[i] = [0] + C[i - 1][:]
    for j in range(1, W + 1):
        counts[i][j] += counts[i - 1][j] + counts[i][j - 1] - counts[i - 1][j - 1]

for _ in range(N):
    y, x, b, s = map(int, input().split())

    w_B, w_S = b // 2, s // 2

    outer = calc_interval_sum(counts, y - w_B, x - w_B, y + w_B, x + w_B)
    inner = calc_interval_sum(counts, y - w_S, x - w_S, y + w_S, x + w_S)
    ans.append(outer - inner)

for i in ans:
    print(i)