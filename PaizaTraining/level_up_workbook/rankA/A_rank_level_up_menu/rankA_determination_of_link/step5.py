N = int(input())
g = [[0] * N for _ in range(N)]
for _ in range(N-1):
    a, b = [int(x) - 1 for x in input().split()]
    g[a][b] = 1
    g[b][a] = 1

index = 0
for _ in range(N):
    print(index+1)
    if 1 in g[index]:
        next = g[index].index(1)
        g[next][index] = 0
        index = next    