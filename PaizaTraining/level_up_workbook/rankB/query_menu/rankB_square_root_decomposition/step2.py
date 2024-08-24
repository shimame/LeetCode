N, K = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
sums = [0] * N
sums[0] = A[0]
ans = []
for i in range(1, N):
    sums[i] = sums[i - 1] + A[i]
for i in range(K):
    left, right = map(int, input().split())
    if left == 1:
        ans.append(sums[right-1])
    else:
        ans.append(sums[right-1] - sums[left-2])

for j in ans:
    print(j)