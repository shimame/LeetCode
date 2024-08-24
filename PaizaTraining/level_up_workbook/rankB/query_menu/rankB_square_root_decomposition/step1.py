N, K = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
sums = [0] * N
sums[0] = A[0]
Q = [int(input()) for _ in range(K)]
for i in range(1, N):
    sums[i] = sums[i - 1] + A[i]
for q in Q:
    print(sums[q - 1])