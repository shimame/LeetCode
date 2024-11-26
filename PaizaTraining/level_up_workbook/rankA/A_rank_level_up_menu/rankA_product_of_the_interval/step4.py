N, M = [int(x) for x in input().split()]
A = [int(n) for n in input().split()]
sums = [0 for _ in range(N+1)]

for n in range(N):
    sums[n+1] = sums[n] + A[n]

length = 0
start, end = 0, 0

while end < N:
    if sums[end+1] - sums[start] <= M:
        if end - start + 1 > length:
            length = end - start + 1
        end += 1
    else:
        start += 1

print(length)