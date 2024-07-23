N, K = map(int, input().split())
M = 0
while N < K:
    N *= 2
    M += 1
print(M)