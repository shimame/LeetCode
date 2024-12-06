N, M = [int(x) for x in input().split()]
g = [[0] * N for _ in range(N)] # 隣接行列
h = [[] for _ in range(N)] # 隣接リスト

for _ in range(M):
    a, b, k = [int(n) - 1 for n in input().split()]
    g[a][b] = k + 1
    h[a].append((b, k + 1))

for i in range(N):
    print("".join(map(str, g[i])))

for j in range(N):
    h[j].sort()
    for l, r in h[j]:
        print(f"{l}({r})", end="")
    print()