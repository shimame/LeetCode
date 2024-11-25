N, M = [int(x) for x in input().split()]
A = [int(n) for n in input().split()]
sums = [0 for _ in range(N+1)]

for n in range(N):
    sums[n+1] = sums[n] + A[n]

length = 10 ** 5
start, end = 0, 0

# しゃくとり法
while end < N:
    if sums[end+1] - sums[start] >= M:
        if end - start + 1 < length:
            length = end - start + 1
        start += 1
    else:
        end += 1

if length == 10 ** 5:
    print(-1)
else:
    print(length)