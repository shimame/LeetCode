N, M = [int(x) for x in input().split()]
g = [["0" for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = [int(n) - 1 for n in input().split()]
    g[a][b] = str(1)
    g[b][a] = str(1)

for i in range(N):
    print("".join(g[i]))