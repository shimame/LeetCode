N, K = [int(x) for x in input().split()]
P = [int(input()) for _ in range(N)]
P = P + P[:K]
max_sum = 0
for i in range(N):
    sum = 0
    for j in range(K):
        sum += P[i + j]
    if max_sum < sum:
        max_sum = sum
print(max_sum)