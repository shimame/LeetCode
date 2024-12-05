N, M = [int(x) for x in input().split()]
g = [[0] * N for _ in range(N)]
h = [[] for _ in range(N)]

for _ in range(M):
    a, b = [int(n) - 1 for n in input().split()]
    g[a][b] = 1
    h[a].append(b)

for i in range(N):
    print("".join(map(str, g[i])))

for j in range(N):
    h[j].sort()
    print("".join(map(str, h[j])))