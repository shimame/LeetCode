N, K = [int(x) for x in input().split()]
A = [1, 0, -1]
if N == K:
    print(0)
else:
    if (K - N) % 3 == 0:
        step = 0
    if (K - N) % 3 == 1:
        step = 1
    if (K - N) % 3 == 2:
        step = 2
    print(A[(N-1 + step) % 3])