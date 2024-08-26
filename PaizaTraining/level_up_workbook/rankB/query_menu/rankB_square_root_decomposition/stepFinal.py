import math

N = 10000
K = int(input())
A = [int(input()) for _ in range(N)]
x = int(math.sqrt(N))
if x ** 2 < N:
    x += 1
max_nums = [0] * x
ans = []

for i in range(x):
    start, end = x * i, x * (i+1)
    max_nums[i] = max(A[start:end])

for _ in range(K):
    left, right = map(lambda x: int(x) - 1, input().split())

    max_val = A[left]
    current = left
    while current <= right:
        if current % x == 0 and current + x - 1 <= right:
            max_val = max(max_val, max_nums[current // x])
            current += x
        else:
            max_val = max(max_val, A[current])
            current += 1
    ans.append(max_val)

for i in ans:
    print(i)