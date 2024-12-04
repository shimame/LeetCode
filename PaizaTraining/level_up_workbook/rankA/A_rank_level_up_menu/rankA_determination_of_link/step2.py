N, M = [int(x) for x in input().split()]
g = [[] for _ in range(N)]

for _ in range(M):
    a, b = [int(n) - 1 for n in input().split()]
    g[a].append(b)
    g[b].append(a)

for i in range(N):
    g[i].sort()
    print("".join(map(str, g[i])))