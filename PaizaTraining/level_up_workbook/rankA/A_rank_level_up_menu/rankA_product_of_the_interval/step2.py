N = int(input())
A = [int(x) for x in input().split()]
n = int(input())
sums = [A[0]] + [0 for _ in range(N-1)]
for i in range(1, N):
    sums[i] = sums[i-1] + A[i]

for _ in range(n):
    l, u = [int(n) for n in input().split()]
    print(sums[u] - sums[l] + A[l])